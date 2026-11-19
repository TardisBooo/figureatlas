# -*- coding: utf-8 -*-
"""Publish a verified FigureAtlas staging run into the public catalog and docs."""

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "incoming"))
from catalog_data import FAMILIES, FIGURES  # noqa: E402

STAGING = ROOT / "assets" / "gallery" / "_staging"
PUBLIC = ROOT / "assets" / "gallery" / "atlas"
REPORT = STAGING / "verification.json"


def require_verification():
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    if data.get("rendered") != 300 or data.get("passed") != 300:
        raise SystemExit(f"Refusing to publish: {data.get('passed')} passed of {data.get('rendered')}")
    missing = [f["id"] for f in FIGURES if not (STAGING / f"{f['id']}_{f['slug']}.png").is_file()]
    if missing:
        raise SystemExit(f"Missing screenshots: {missing[:8]}")
    return data


def publish_files():
    if PUBLIC.exists():
        shutil.rmtree(PUBLIC)
    PUBLIC.mkdir(parents=True)
    for fig in FIGURES:
        stem = f"{fig['id']}_{fig['slug']}"
        shutil.copy2(STAGING / f"{stem}.png", PUBLIC / f"{stem}.png")
        html = STAGING / f"{stem}.html"
        if html.is_file():
            shutil.copy2(html, PUBLIC / f"{stem}.html")


def write_gallery():
    lines = [
        "# FigureAtlas gallery",
        "",
        "Three hundred verified figure types for papers, slides, posters, and video frames.",
        "Each card below is a screenshot captured during verification, not a placeholder.",
        "",
        "The first 26 specialized renderers remain in the original gallery.",
        "The atlas adds the chart, diagram, map, and illustration grammars used to reach 300.",
        "",
    ]
    by_family = {}
    for fig in FIGURES:
        by_family.setdefault(fig["family"], []).append(fig)
    for fam, en, zh in FAMILIES:
        rows = by_family[fam]
        lines += [f"## {en}", "", f"{zh}。{len(rows)} figures.", ""]
        for i in range(0, len(rows), 2):
            pair = rows[i:i + 2]
            cells = []
            for fig in pair:
                src = f"assets/gallery/atlas/{fig['id']}_{fig['slug']}.png"
                cells.append(
                    f'<div align="center"><b>{fig["id"]} {fig["en"]}</b><br/>'
                    f'<img src="{src}" width="360" alt="{fig["en"]}"/><br/>'
                    f'<sub>{fig["zh"]}</sub></div>'
                )
            if len(cells) == 1:
                cells.append(" ")
            lines.append("| " + " | ".join(cells) + " |")
            if i == 0:
                lines.append("|:---:|:---:|")
        lines.append("")
    (ROOT / "GALLERY.md").write_text("\n".join(lines), encoding="utf-8")


def write_index():
    lines = [
        "# FigureAtlas catalog",
        "",
        "| ID | English | 中文 | Family | Screenshot |",
        "|---:|---|---|---|---|",
    ]
    for fig in FIGURES:
        shot = f"assets/gallery/atlas/{fig['id']}_{fig['slug']}.png"
        lines.append(
            f"| {fig['id']} | {fig['en']} | {fig['zh']} | {fig['family_zh']} | "
            f"[png]({shot}) |"
        )
    lines.append("")
    (ROOT / "CATALOG.md").write_text("\n".join(lines), encoding="utf-8")


def write_skill():
    text = """---
name: visual-storyboard-designer
description: Pick a FigureAtlas figure for a paper, slide, poster, or video frame. The catalog has 300 verified figure types across 15 families.
---

# FigureAtlas storyboard skill

Use this skill when an agent needs a figure for a paper, a slide, a poster, or a video frame.

## Selection order

1. Pick the output frame: journal single column, journal double column, 16:9 slide, 4:3 slide, A0 poster, or 1080p video.
2. Pick the family from the table below.
3. Pick one figure id from `CATALOG.md`. Do not invent a 301st type.

## Families

| Family | Use it when | Count |
|---|---|---:|
| Format adapters | The same figure must fit a journal column, a slide, or a poster | 18 |
| Distribution and comparison | Groups, ranks, or uncertainty are the point | 28 |
| Correlation and dimension reduction | Two or more measures move together | 20 |
| Time and process | The horizontal axis is time or sequence | 16 |
| Part-to-whole and sets | Shares, overlap, or hierarchy matter | 14 |
| Networks and systems | The slide explains components and flow | 25 |
| Mathematics and derivation | The lesson shows a geometric reason | 18 |
| Model structure and evaluation | The paper reports a model | 20 |
| Life science and omics | The figure is genomic, cellular, or phylogenetic | 37 |
| Chemistry and materials | The figure is a structure, spectrum, or process | 17 |
| Physics, engineering, and signals | The figure is a field, circuit, orbit, or waveform | 28 |
| Maps and space | Location is part of the claim | 16 |
| Scientific illustration | The reader needs a mechanism, not a statistic | 20 |
| Tables, code, and legends | The claim is a table, listing, or color key | 8 |
| Clinical and epidemiology | The paper follows a clinical reporting diagram | 15 |

## Call

```python
from figureatlas import render_figure
html = render_figure("161")  # volcano plot
```

Legacy specialized renderers such as `render_quantum_bloch_circuit` remain importable.
"""
    path = ROOT / "skills" / "visual-storyboard-designer" / "SKILL.md"
    path.write_text(text, encoding="utf-8")


def main():
    data = require_verification()
    publish_files()
    write_gallery()
    write_index()
    write_skill()
    print(f"Published {data['passed']} screenshots to {PUBLIC}")


if __name__ == "__main__":
    main()
