# -*- coding: utf-8 -*-
"""Render the 300-figure catalog to a staging folder and keep screenshots."""

import hashlib
import json
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
INCOMING = Path(__file__).resolve().parent
sys.path.insert(0, str(INCOMING))

from catalog_data import FAMILIES, FIGURES  # noqa: E402
from render_atlas import page, render_legacy, render_new  # noqa: E402

STAGING = ROOT / "assets" / "gallery" / "_staging"
GALLERY = ROOT / "assets" / "gallery"
REPORT = STAGING / "verification.json"


def check_image(path, fig):
    im = Image.open(path).convert("RGB")
    w, h = im.size
    min_w = 400 if fig["legacy"] else 640
    if w < min_w or h < 240:
        return False, f"too small {w}x{h}"
    pixels = list(im.resize((48, 27)).getdata())
    colors = len(set(pixels))
    dark = sum(1 for r, g, b in pixels if r < 12 and g < 14 and b < 20)
    if colors < 8:
        return False, f"only {colors} colors"
    if dark > len(pixels) * 0.92:
        return False, "mostly empty"
    return True, f"{w}x{h} colors={colors}"


def main():
    STAGING.mkdir(parents=True, exist_ok=True)
    from playwright.sync_api import sync_playwright

    results = []
    hashes = {}
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page_obj = browser.new_page(viewport={"width": 1100, "height": 760})
        only = set(sys.argv[1:])
        for i, fig in enumerate(FIGURES, 1):
            if only and fig["id"] not in only and fig["slug"] not in only:
                continue
            fid = fig["id"]
            html_path = STAGING / f"{fid}_{fig['slug']}.html"
            png_path = STAGING / f"{fid}_{fig['slug']}.png"
            if fig["legacy"]:
                raw, legacy_png = render_legacy(fig, GALLERY)
                html_path.write_text(raw, encoding="utf-8")
                png_path.write_bytes(legacy_png.read_bytes())
                ok, detail = check_image(png_path, fig)
                source = "legacy-screenshot"
            else:
                html = page(render_new(fig))
                if "<svg" not in html or "NaN" in html:
                    ok, detail = False, "invalid svg"
                    source = "new"
                else:
                    html_path.write_text(html, encoding="utf-8")
                    page_obj.set_content(html, wait_until="networkidle")
                    target = page_obj.query_selector(".atlas-card")
                    target.screenshot(path=str(png_path))
                    ok, detail = check_image(png_path, fig)
                    source = "new-screenshot"
            digest = hashlib.sha256(png_path.read_bytes()).hexdigest() if png_path.exists() else ""
            if digest in hashes and not fig["legacy"]:
                ok = False
                detail = f"duplicate of {hashes[digest]}"
            elif digest:
                hashes[digest] = fid
            results.append({
                "id": fid, "slug": fig["slug"], "family": fig["family"],
                "kind": fig["kind"], "source": source, "pass": ok, "detail": detail,
                "png": str(png_path),
            })
            if i % 25 == 0 or not ok:
                print(f"{i:03d} {fid} {'PASS' if ok else 'FAIL'} {detail}", flush=True)
        browser.close()

    failed = [row for row in results if not row["pass"]]
    summary = {
        "product": "FigureAtlas",
        "expected": 300,
        "rendered": len(results),
        "passed": len(results) - len(failed),
        "failed": len(failed),
        "families": {fam: sum(1 for f in FIGURES if f["family"] == fam) for fam, _, _ in FAMILIES},
        "failures": failed,
    }
    REPORT.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k: summary[k] for k in ("expected", "rendered", "passed", "failed")}, ensure_ascii=False))
    if failed and not only:
        raise SystemExit(1)
    if not only:
        passed = len(results) - len(failed)
        if passed != 300:
            raise SystemExit(passed)


if __name__ == "__main__":
    main()
