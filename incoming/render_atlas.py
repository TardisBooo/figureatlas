# -*- coding: utf-8 -*-
"""Render one self-contained HTML card per FigureAtlas entry."""

import math
from random import Random

from catalog_data import FIGURES

PAL = ["#38BDF8", "#10B981", "#818CF8", "#F59E0B", "#FB7185", "#22D3EE", "#A3E635", "#C084FC"]
INK = "#E2E8F0"
MUTED = "#94A3B8"
GRID = "rgba(148,163,184,0.16)"
AXIS = "#64748B"
BG = "#080C14"


def esc(text):
    return (str(text).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def rng_for(fig):
    return Random(7000 + int(fig["id"]) * 17)


def clamp(v, lo, hi):
    return max(lo, min(hi, v))


class Card:
    def __init__(self, fig):
        self.fig = fig
        self.parts = []
        self.rng = rng_for(fig)

    def add(self, fragment):
        self.parts.append(fragment)

    def text(self, x, y, value, size=12, fill=MUTED, anchor="start", weight="500"):
        x, y = clamp(x, 8, 908), clamp(y, 14, 508)
        self.add(
            f'<text x="{x:.1f}" y="{y:.1f}" fill="{fill}" font-size="{size}" '
            f'font-family="Segoe UI, Microsoft YaHei, sans-serif" text-anchor="{anchor}" '
            f'font-weight="{weight}">{esc(value)}</text>'
        )

    def line(self, x1, y1, x2, y2, stroke=AXIS, width=1.4, dash=""):
        extra = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{stroke}" stroke-width="{width}"{extra}/>'
        )

    def rect(self, x, y, w, h, fill, rx=2, opacity=1, stroke="none"):
        self.add(
            f'<rect x="{x:.1f}" y="{y:.1f}" width="{max(w, 0):.1f}" height="{max(h, 0):.1f}" '
            f'rx="{rx}" fill="{fill}" fill-opacity="{opacity}" stroke="{stroke}"/>'
        )

    def circle(self, cx, cy, r, fill, opacity=1, stroke="none", sw=1):
        self.add(
            f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{max(r, 0.6):.1f}" fill="{fill}" '
            f'fill-opacity="{opacity}" stroke="{stroke}" stroke-width="{sw}"/>'
        )

    def poly(self, points, fill="none", stroke=PAL[0], width=2.2, opacity=1, close=False):
        cmd = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
        tag = "polygon" if close else "polyline"
        self.add(
            f'<{tag} points="{cmd}" fill="{fill}" stroke="{stroke}" stroke-width="{width}" '
            f'stroke-linejoin="round" stroke-linecap="round" fill-opacity="{opacity}"/>'
        )

    def path(self, d, fill="none", stroke="none", width=1.5, opacity=1):
        self.add(
            f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{width}" '
            f'fill-opacity="{opacity}" stroke-linejoin="round"/>'
        )

    def axes(self, x0=64, y0=36, x1=880, y1=456, xlabel="", ylabel=""):
        self.line(x0, y0, x0, y1, AXIS, 1.2)
        self.line(x0, y1, x1, y1, AXIS, 1.2)
        for i in range(1, 5):
            y = y0 + (y1 - y0) * i / 5
            self.line(x0, y, x1, y, GRID, 1)
        if xlabel:
            self.text((x0 + x1) / 2, y1 + 28, xlabel, 12, MUTED, "middle")
        if ylabel:
            self.text(18, (y0 + y1) / 2, ylabel, 12, MUTED, "middle")

    def finish(self):
        title = esc(self.fig["en"])
        desc = esc(f'{self.fig["zh"]}。{self.fig["family_en"]} figure {self.fig["id"]}.')
        fid = self.fig["id"]
        body = "".join(self.parts)
        svg = (
            f'<svg viewBox="0 0 920 520" role="img" aria-labelledby="t{fid} d{fid}">'
            f'<title id="t{fid}">{title}</title><desc id="d{fid}">{desc}</desc>'
            f'<rect width="920" height="520" fill="{BG}"/>{body}</svg>'
        )
        return (
            f'<article class="atlas-card" data-kind="{esc(self.fig["kind"])}" '
            f'data-id="{fid}">'
            f'<header><p class="kicker">{fid} · {esc(self.fig["family_en"])}</p>'
            f'<h2>{title}</h2><p class="zh">{esc(self.fig["zh"])}</p></header>'
            f'<div class="plot">{svg}</div></article>'
        )


def series(rng, n, lo=0.15, hi=0.92, trend=-0.4):
    raw = []
    level = rng.uniform(0.35, 0.7)
    for i in range(n):
        level += trend / n + rng.uniform(-0.08, 0.08)
        raw.append(clamp(level, lo, hi))
    return raw


def forest_plot(card):
    card.line(470, 40, 470, 470, AXIS, 1.2, "4 4")
    for i in range(7):
        y = 70 + i * 52
        lo = 300 + (i % 3) * 28
        hi = 560 + (i % 4) * 24
        card.line(lo, y, hi, y, PAL[i % 5], 2)
        card.rect((lo + hi) / 2 - 5, y - 5, 10, 10, PAL[i % 5], 1)
        card.text(70, y + 4, f"Study {i+1}", 12, MUTED)
    card.text(470, 500, "No effect", 12, MUTED, "middle")


def draw_bars(card, mode):
    rng = card.rng
    labels = ["A", "B", "C", "D", "E", "F", "G", "H"]
    groups = 4 if mode in {"grouped", "stacked", "percent"} else 6
    series_n = 3 if mode in {"grouped", "stacked", "percent"} else 1
    vals = [[rng.uniform(0.2, 0.95) for _ in range(groups)] for _ in range(series_n)]
    if mode == "waterfall":
        vals = [[0.72, -0.18, 0.11, -0.22, 0.08, -0.09]]
        groups = 6
    card.axes(xlabel="Group", ylabel="Value")
    x0, y0, x1, y1 = 64, 36, 880, 456
    gap = (x1 - x0) / groups
    if mode == "horizontal":
        for i, v in enumerate(vals[0]):
            y = 58 + i * 58
            card.rect(90, y, 640 * v, 28, PAL[i % 6], 4)
            card.text(78, y + 20, labels[i], 12, MUTED, "end")
        return
    if mode == "pyramid":
        left = [rng.uniform(0.3, 0.9) for _ in range(6)]
        right = [rng.uniform(0.3, 0.9) for _ in range(6)]
        for i, (a, b) in enumerate(zip(left, right)):
            y = 70 + i * 58
            card.rect(450 - 280 * a, y, 280 * a, 32, PAL[0], 3)
            card.rect(470, y, 280 * b, 32, PAL[4], 3)
            card.text(460, y + 22, f"{i+1}", 11, INK, "middle")
        card.text(250, 40, "Group A", 12, PAL[0], "middle")
        card.text(670, 40, "Group B", 12, PAL[4], "middle")
        return
    for g in range(groups):
        if mode == "percent":
            total = sum(vals[s][g] for s in range(series_n)) or 1
            acc = 0
            for s in range(series_n):
                h = 360 * vals[s][g] / total
                card.rect(x0 + g * gap + 18, y1 - acc - h, gap - 36, h, PAL[s], 2)
                acc += h
        elif mode == "stacked":
            acc = 0
            for s in range(series_n):
                h = 300 * vals[s][g] / series_n
                card.rect(x0 + g * gap + 22, y1 - acc - h, gap - 44, h, PAL[s], 2)
                acc += h
        elif mode == "grouped":
            bw = (gap - 24) / series_n
            for s in range(series_n):
                h = 340 * vals[s][g]
                card.rect(x0 + g * gap + 10 + s * bw, y1 - h, bw - 4, h, PAL[s], 2)
        elif mode == "waterfall":
            v = vals[0][g]
            running = 0.55 if g == 0 else None
            base = 0.25 + 0.08 * g
            h = abs(v) * 280
            y = y1 - (0.35 + max(v, 0)) * 280
            color = PAL[1] if v >= 0 else PAL[4]
            card.rect(x0 + g * gap + 24, y, gap - 48, h, color, 3)
        else:
            h = 340 * vals[0][g]
            card.rect(x0 + g * gap + 18, y1 - h, gap - 36, h, PAL[g % 6], 3)
        card.text(x0 + g * gap + gap / 2, y1 + 22, labels[g], 12, MUTED, "middle")


def draw_lines(card, mode):
    rng = card.rng
    card.axes(xlabel="Step", ylabel="Measure")
    x0, y0, x1, y1 = 64, 36, 880, 456
    n = 24
    count = {"one": 1, "many": 3, "area": 1, "stack": 3, "stream": 4, "step": 1, "fan": 1, "band": 2}.get(mode, 1)
    xs = [x0 + (x1 - x0) * i / (n - 1) for i in range(n)]
    if mode == "stack":
        acc = [0] * n
        for s in range(count):
            raw = [rng.uniform(0.08, 0.22) for _ in range(n)]
            top = [acc[i] + raw[i] for i in range(n)]
            pts = [(xs[i], y1 - top[i] * 380) for i in range(n)]
            base = [(xs[i], y1 - acc[i] * 380) for i in range(n)]
            card.poly(pts + base[::-1], PAL[s], "none", 0, 0.85, True)
            acc = top
        return
    if mode == "stream":
        center = [0.5] * n
        for s in range(count):
            w = [rng.uniform(0.05, 0.12) for _ in range(n)]
            upper = [(xs[i], y1 - (center[i] + w[i]) * 360) for i in range(n)]
            lower = [(xs[i], y1 - (center[i] - w[i]) * 360) for i in range(n)]
            card.poly(upper + lower[::-1], PAL[s], "none", 0, 0.8, True)
            center = [center[i] + rng.uniform(-0.02, 0.03) for i in range(n)]
        return
    for s in range(count):
        ys = series(rng, n, 0.18, 0.9, trend=-0.35 + s * 0.15)
        pts = []
        for i, v in enumerate(ys):
            x = xs[i]
            y = y0 + (1 - v) * (y1 - y0 - 10)
            if mode == "step" and pts:
                pts.append((x, pts[-1][1]))
            pts.append((x, y))
        if mode == "area":
            card.poly(pts + [(x1, y1), (x0, y1)], PAL[0], "none", 0, 0.28, True)
        if mode == "fan" and s == 0:
            hi = [(xs[i], pts[i][1] - 18 - i * 0.6) for i in range(n)]
            lo = [(xs[i], pts[i][1] + 18 + i * 0.8) for i in range(n)]
            card.poly(hi + lo[::-1], PAL[3], "none", 0, 0.25, True)
        if mode == "band" and s == 1:
            band = [(pts[i][0], pts[i][1] - 16) for i in range(n)] + [
                (pts[i][0], pts[i][1] + 16) for i in range(n - 1, -1, -1)]
            card.poly(band, PAL[0], "none", 0, 0.22, True)
        card.poly(pts, "none", PAL[s], 2.6)


def draw_dist(card, mode):
    rng = card.rng
    card.axes(xlabel="Group", ylabel="Value")
    x0, y1 = 90, 456
    for g in range(5):
        cx = x0 + g * 150
        center = 180 + rng.randint(-40, 70)
        if mode in {"box", "notch", "jitter", "rain"}:
            q1, q3 = center - 48, center + 42
            card.rect(cx - 28, q1, 56, q3 - q1, PAL[g], 3, 0.85)
            card.line(cx - 28, center, cx + 28, center, "#041018", 2)
            card.line(cx, q1, cx, q1 - 36, INK, 1.2)
            card.line(cx, q3, cx, q3 + 30, INK, 1.2)
            if mode == "notch":
                card.poly([(cx - 28, center - 10), (cx - 8, center), (cx - 28, center + 10)], BG, "none", 0, 1, True)
                card.poly([(cx + 28, center - 10), (cx + 8, center), (cx + 28, center + 10)], BG, "none", 0, 1, True)
        if mode in {"violin", "rain"}:
            body = []
            for k in range(21):
                t = k / 20
                y = center - 90 + t * 180
                w = 34 * math.sin(math.pi * t) * (0.7 + 0.3 * math.sin(t * 9 + g))
                body.append((cx - w, y))
            for k in range(20, -1, -1):
                t = k / 20
                y = center - 90 + t * 180
                w = 34 * math.sin(math.pi * t) * (0.7 + 0.3 * math.sin(t * 9 + g))
                body.append((cx + w, y))
            card.poly(body, PAL[g], "none", 0, 0.45, True)
        if mode in {"bee", "jitter", "rain"}:
            for k in range(18):
                card.circle(cx + rng.uniform(-22, 22), center + rng.uniform(-70, 70), 3.2, INK, 0.85)
        if mode == "ridge":
            base = 80 + g * 78
            pts = []
            for i in range(40):
                x = 120 + i * 18
                y = base - 58 * math.exp(-((i - 18 - g) ** 2) / 30)
                pts.append((x, y))
            card.poly(pts + [(840, base), (120, base)], PAL[g], PAL[g], 1.5, 0.35, True)
        if mode == "ecdf":
            pass
        card.text(cx, 484, f"G{g+1}", 12, MUTED, "middle")
    if mode == "ecdf":
        card.parts.clear()
        card.axes(xlabel="Value", ylabel="F(x)")
        pts = []
        y = 440
        for i in range(20):
            x = 80 + i * 40
            y -= rng.uniform(8, 22)
            pts.append((x, y))
            pts.append((x + 40, y))
        card.poly(pts, "none", PAL[0], 2.6)
    if mode == "qq":
        card.parts.clear()
        card.axes(xlabel="Theoretical quantile", ylabel="Sample quantile")
        card.line(90, 430, 840, 80, AXIS, 1.2, "6 4")
        for i in range(28):
            x = 100 + i * 26
            card.circle(x, 430 - i * 12 + rng.uniform(-12, 12), 4, PAL[0])


def draw_points(card, mode):
    rng = card.rng
    card.axes(xlabel="X", ylabel="Y")
    if mode == "roc":
        pts = [(64, 456)]
        x = 64
        y = 456
        for _ in range(12):
            x += rng.uniform(30, 70)
            y -= rng.uniform(20, 55)
            pts.append((min(x, 860), max(y, 50)))
        pts.append((880, 40))
        card.line(64, 456, 880, 40, AXIS, 1.2, "5 4")
        card.poly(pts, "none", PAL[0], 2.8)
        return
    if mode == "pr":
        pts = [(70, 70)]
        for i in range(16):
            pts.append((80 + i * 48, 80 + i * 18 + rng.uniform(-8, 10)))
        card.poly(pts, "none", PAL[1], 2.8)
        return
    if mode == "calibration":
        card.line(80, 440, 840, 70, AXIS, 1.2, "5 4")
        pts = [(80 + i * 50, 430 - i * 22 + rng.uniform(-16, 16)) for i in range(16)]
        card.poly(pts, "none", PAL[3], 2.6)
        return
    if mode == "bland":
        card.line(64, 246, 880, 246, PAL[4], 1.2, "4 3")
        for i in range(36):
            card.circle(90 + i * 21, 246 + rng.uniform(-70, 70), 4, PAL[0])
        return
    if mode == "residual":
        card.line(64, 246, 880, 246, AXIS, 1.2)
        for i in range(40):
            card.circle(80 + i * 20, 246 + rng.uniform(-90, 90) * (0.4 + i / 80), 3.5, PAL[2])
        return
    for i in range(42):
        x = rng.uniform(90, 860)
        y = rng.uniform(60, 430)
        group = 0 if x + y < 700 else 1
        r = rng.uniform(6, 18) if mode == "bubble" else 4.5
        card.circle(x, y, r, PAL[group], 0.8)


def draw_matrix(card, mode):
    rng = card.rng
    n = 6
    labels = ["V1", "V2", "V3", "V4", "V5", "V6"]
    cell = 58
    x0, y0 = 120, 70
    if mode == "clustermap":
        card.line(70, 40, 110, 78, PAL[2], 1.4)
        card.line(70, 40, 96, 40, PAL[2], 1.4)
        card.line(96, 40, 110, 78, PAL[2], 1.4)
    for r in range(n):
        card.text(108, y0 + r * cell + 34, labels[r], 12, MUTED, "end")
        card.text(x0 + r * cell + 24, 58, labels[r], 12, MUTED, "middle")
        for c in range(n):
            if mode == "tri" and c > r:
                continue
            v = rng.random() if mode != "confusion" else (0.8 if r == c else rng.uniform(0, 0.25))
            if mode == "confusion" and r == c:
                v = 0.75 + rng.random() * 0.2
            color = PAL[0] if v > 0.5 else PAL[4]
            card.rect(x0 + c * cell, y0 + r * cell, cell - 6, cell - 6, color, 3, 0.25 + 0.7 * v)
            if mode in {"annot", "confusion"}:
                card.text(x0 + c * cell + 24, y0 + r * cell + 32, f"{v:.2f}", 10, INK, "middle")
    if mode == "confusion":
        card.text(500, 470, "Predicted", 12, MUTED, "middle")
        card.text(36, 250, "Actual", 12, MUTED, "middle")


def draw_hierarchy(card, mode):
    rng = card.rng
    weights = [rng.uniform(0.6, 1.4) for _ in range(5)]
    total = sum(weights)
    if mode in {"pie", "donut", "nested"}:
        start = -math.pi / 2
        for i, w in enumerate(weights):
            ang = 2 * math.pi * w / total
            end = start + ang
            large = 1 if ang > math.pi else 0
            r_out, r_in = (150, 0) if mode == "pie" else (150, 78)
            x1, y1 = 360 + r_out * math.cos(start), 250 + r_out * math.sin(start)
            x2, y2 = 360 + r_out * math.cos(end), 250 + r_out * math.sin(end)
            if mode == "pie":
                d = f"M 360 250 L {x1:.1f} {y1:.1f} A {r_out} {r_out} 0 {large} 1 {x2:.1f} {y2:.1f} Z"
            else:
                ix1, iy1 = 360 + r_in * math.cos(end), 250 + r_in * math.sin(end)
                ix2, iy2 = 360 + r_in * math.cos(start), 250 + r_in * math.sin(start)
                d = (f"M {x1:.1f} {y1:.1f} A {r_out} {r_out} 0 {large} 1 {x2:.1f} {y2:.1f} "
                     f"L {ix1:.1f} {iy1:.1f} A {r_in} {r_in} 0 {large} 0 {ix2:.1f} {iy2:.1f} Z")
            card.path(d, PAL[i])
            start = end
        if mode == "nested":
            card.circle(360, 250, 60, BG)
            card.circle(360, 250, 42, PAL[2], 0.8)
        for i in range(5):
            card.rect(620, 90 + i * 48, 16, 16, PAL[i], 3)
            card.text(646, 103 + i * 48, f"Part {i+1}", 13, INK)
        return
    if mode == "sunburst":
        start = -math.pi / 2
        for i, w in enumerate(weights):
            ang = 2 * math.pi * w / total
            for ring, rad in enumerate((70, 120, 168)):
                a0, a1 = start + 0.03, start + ang - 0.03
                x1, y1 = 430 + rad * math.cos(a0), 260 + rad * math.sin(a0)
                x2, y2 = 430 + rad * math.cos(a1), 260 + rad * math.sin(a1)
                card.path(
                    f"M {430 + (rad-36)*math.cos(a0):.1f} {260 + (rad-36)*math.sin(a0):.1f} "
                    f"L {x1:.1f} {y1:.1f} A {rad} {rad} 0 0 1 {x2:.1f} {y2:.1f} "
                    f"L {430 + (rad-36)*math.cos(a1):.1f} {260 + (rad-36)*math.sin(a1):.1f} Z",
                    PAL[(i + ring) % 6], opacity=0.9)
            start += ang
        return
    if mode == "treemap":
        x, y = 50, 40
        sizes = [220, 160, 140, 180, 120, 90]
        cursor = 50
        for i, w in enumerate(sizes):
            h = 200 if i < 3 else 150
            row_y = 40 if i < 3 else 270
            card.rect(cursor if i < 3 else 50 + (i - 3) * 200, row_y, w if i < 3 else 180, h, PAL[i % 6], 6, 0.85)
            card.text((cursor if i < 3 else 50 + (i - 3) * 200) + 16, row_y + 28, f"N{i+1}", 14, "#041018", "start", "700")
            if i < 2:
                cursor += w + 12
        return
    if mode == "icicle":
        y = 40
        spans = [5, 3, 2]
        for depth, count in enumerate(spans):
            x = 40
            width = 840 / count
            for i in range(count):
                card.rect(x + 4, y, width - 8, 90, PAL[(depth + i) % 6], 4, 0.9)
                card.text(x + 16, y + 50, f"L{depth+1}.{i+1}", 13, "#041018")
                x += width
            y += 110
        return
    if mode == "pack":
        spots = [(250, 230, 90), (470, 180, 70), (620, 300, 80), (390, 360, 54), (180, 380, 40)]
        for i, (x, y, r) in enumerate(spots):
            card.circle(x, y, r, PAL[i], 0.85)
            card.text(x, y + 4, f"S{i+1}", 13, "#041018", "middle", "700")
        return
    if mode == "waffle":
        for i in range(100):
            filled = i < 62
            card.rect(80 + (i % 10) * 42, 50 + (i // 10) * 42, 34, 34, PAL[0] if filled else "#1E293B", 3)
        card.text(560, 250, "62%", 42, INK, "start", "700")
        return
    if mode == "mosaic":
        card.rect(60, 40, 360, 250, PAL[0], 0, 0.9)
        card.rect(60, 300, 360, 160, PAL[1], 0, 0.9)
        card.rect(430, 40, 420, 120, PAL[3], 0, 0.9)
        card.rect(430, 170, 420, 290, PAL[4], 0, 0.9)
        card.text(80, 70, "A × yes", 14, "#041018")
        return
    if mode == "mekko":
        x = 50
        widths = [180, 120, 220, 150, 140]
        for i, w in enumerate(widths):
            y = 40
            bits = [rng.uniform(0.15, 0.4) for _ in range(3)]
            s = sum(bits)
            for b, bit in enumerate(bits):
                h = 400 * bit / s
                card.rect(x, y, w - 8, h, PAL[b], 0, 0.9)
                y += h
            x += w
        return
    if mode == "venn":
        card.circle(360, 250, 120, PAL[0], 0.45)
        card.circle(470, 250, 120, PAL[1], 0.45)
        card.circle(415, 340, 120, PAL[3], 0.4)
        card.text(330, 180, "A", 16, INK, "middle")
        card.text(520, 180, "B", 16, INK, "middle")
        card.text(415, 430, "C", 16, INK, "middle")
        return
    if mode == "euler":
        card.circle(400, 260, 150, PAL[0], 0.35)
        card.circle(470, 280, 70, PAL[3], 0.55)
        card.text(330, 180, "All samples", 14, INK)
        card.text(450, 284, "Subset", 13, INK, "middle")
        return
    if mode == "upset":
        sets = ["S1", "S2", "S3", "S4"]
        for i, name in enumerate(sets):
            card.text(70, 300 + i * 36, name, 13, MUTED, "start")
            for j in range(6):
                on = rng.random() > 0.45
                card.circle(160 + j * 36, 294 + i * 36, 7, PAL[0] if on else "#334155")
                if i < 3:
                    card.line(160 + j * 36, 294 + i * 36, 160 + j * 36, 294 + (i + 1) * 36, "#334155", 2)
        for j in range(6):
            h = rng.uniform(40, 180)
            card.rect(148 + j * 36, 230 - h, 22, h, PAL[2], 2)
        return
    if mode == "proparea":
        for i, r in enumerate((40, 70, 110, 150)):
            card.circle(140 + i * 190, 270, r, PAL[i], 0.8)
            card.text(140 + i * 190, 450, f"{(i+1)*12}", 13, MUTED, "middle")


def draw_network(card, mode):
    rng = card.rng
    if mode == "sankey":
        bands = [(80, 60, 120, PAL[0]), (80, 200, 90, PAL[1]), (80, 330, 110, PAL[3])]
        rights = [(760, 50, 80), (760, 160, 100), (760, 290, 70), (760, 390, 70)]
        for i, (x, y, h, color) in enumerate(bands):
            card.rect(x, y, 18, h, color, 2)
            y2 = rights[i][1]
            card.path(
                f"M 98 {y} C 400 {y}, 480 {y2}, 760 {y2} L 760 {y2+rights[i][2]} "
                f"C 480 {y2+40}, 400 {y+h}, 98 {y+h} Z",
                color, opacity=0.45)
        for x, y, h in rights:
            card.rect(x, y, 18, h, PAL[2], 2)
        return
    if mode == "alluvial":
        xs = [80, 340, 600]
        for col, x in enumerate(xs):
            y = 50
            for i in range(4):
                h = rng.randint(50, 90)
                card.rect(x, y, 22, h, PAL[(col + i) % 5], 2)
                if col < 2:
                    card.path(f"M {x+22} {y+10} C {x+120} {y}, {xs[col+1]-80} {80+i*90}, {xs[col+1]} {80+i*90}",
                              "none", PAL[i], 8, 0.35)
                y += h + 16
        return
    if mode == "chord":
        nodes = []
        for i in range(6):
            a = -math.pi / 2 + i * math.pi / 3
            nodes.append((460 + 170 * math.cos(a), 260 + 170 * math.sin(a)))
            card.circle(*nodes[-1], 16, PAL[i])
        for i in range(6):
            j = (i + 2) % 6
            card.path(f"M {nodes[i][0]:.1f} {nodes[i][1]:.1f} Q 460 260 {nodes[j][0]:.1f} {nodes[j][1]:.1f}",
                      "none", PAL[i], 6, 0.45)
        return
    if mode == "arc":
        for i in range(8):
            card.circle(90 + i * 100, 400, 10, PAL[i % 4])
            card.text(90 + i * 100, 440, str(i + 1), 12, MUTED, "middle")
        for i in range(6):
            span = rng.randint(1, 4)
            x1 = 90 + i * 80
            x2 = x1 + span * 100
            r = (x2 - x1) / 2
            card.path(f"M {x1} 400 A {r:.1f} {r:.1f} 0 0 1 {min(x2, 860)} 400", "none", PAL[i % 5], 2)
        return
    if mode == "flow":
        steps = ["Input", "Clean", "Model", "Check", "Export"]
        for i, name in enumerate(steps):
            x = 40 + i * 176
            card.rect(x, 200, 140, 64, "#0F172A", 8, 1, PAL[i % 5])
            card.text(x + 70, 238, name, 16, INK, "middle", "700")
            if i < 4:
                card.line(x + 140, 232, x + 176, 232, PAL[0], 2)
        return
    if mode == "swim":
        lanes = ["Lab", "Review", "Archive"]
        for i, name in enumerate(lanes):
            y = 50 + i * 140
            card.rect(40, y, 840, 120, "#0F172A", 8, 1, "#1E293B")
            card.text(56, y + 28, name, 14, PAL[i], "start", "700")
            for j in range(3):
                card.rect(180 + j * 200, y + 48, 140, 42, PAL[(i + j) % 5], 6, 0.85)
        return
    if mode == "sequence":
        actors = ["Agent", "Atlas", "Slide"]
        for i, name in enumerate(actors):
            x = 140 + i * 250
            card.rect(x - 50, 36, 120, 36, PAL[i], 6)
            card.text(x + 10, 60, name, 14, "#041018", "middle", "700")
            card.line(x + 10, 80, x + 10, 470, AXIS, 1.2, "4 4")
        card.line(150, 140, 400, 140, INK, 1.6)
        card.line(400, 210, 650, 210, INK, 1.6)
        card.line(650, 280, 150, 280, PAL[3], 1.6, "5 3")
        card.text(250, 130, "render(id)", 12, MUTED, "middle")
        card.text(520, 200, "svg", 12, MUTED, "middle")
        card.text(400, 270, "place on slide", 12, MUTED, "middle")
        return
    if mode == "state":
        states = [(160, 220, "Idle"), (420, 120, "Run"), (680, 220, "Hold"), (420, 360, "Fail")]
        for x, y, name in states:
            card.rect(x, y, 130, 54, "#0F172A", 27, 1, PAL[0])
            card.text(x + 65, y + 33, name, 15, INK, "middle", "700")
        card.line(290, 247, 420, 147, PAL[1], 1.8)
        card.line(550, 147, 680, 247, PAL[1], 1.8)
        card.line(680, 274, 500, 360, PAL[4], 1.8)
        return
    if mode == "mind":
        card.rect(390, 220, 140, 54, PAL[0], 8)
        card.text(460, 252, "Topic", 16, "#041018", "middle", "700")
        for i, name in enumerate(["Data", "Model", "Slide", "Paper"]):
            y = 60 + i * 110
            card.rect(80 if i % 2 == 0 else 680, y, 130, 44, PAL[i + 1], 6)
            card.line(460, 247, 145 if i % 2 == 0 else 680, y + 22, PAL[i + 1], 1.6)
            card.text(145 if i % 2 == 0 else 745, y + 28, name, 14, "#041018", "middle")
        return
    if mode == "fish":
        card.line(80, 260, 820, 260, INK, 3)
        card.path("M 820 260 L 870 230 L 870 290 Z", PAL[0])
        for i, name in enumerate(["Method", "Sample", "Instrument", "Operator"]):
            y = 80 if i % 2 == 0 else 400
            x = 180 + i * 140
            card.line(x, y, x + 80, 260, PAL[i % 4], 2)
            card.text(x - 10, y, name, 13, INK)
        return
    if mode == "tree":
        nodes = [(460, 60), (260, 180), (660, 180), (160, 320), (320, 320), (560, 320), (760, 320)]
        links = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]
        for a, b in links:
            card.line(*nodes[a], *nodes[b], PAL[0], 1.8)
        for i, (x, y) in enumerate(nodes):
            card.rect(x - 36, y - 16, 72, 34, "#0F172A", 6, 1, PAL[i % 4])
            card.text(x, y + 6, f"N{i}", 12, INK, "middle")
        return
    if mode == "c4":
        title = card.fig["en"]
        card.rect(70, 50, 780, 410, "none", 8, 1, PAL[0])
        card.text(90, 78, title, 16, PAL[0], "start", "700")
        boxes = 3 if "component" in card.fig["slug"] else 2
        for i in range(boxes + 1):
            card.rect(120 + i * 180, 180, 150, 90, "#0F172A", 8, 1, PAL[i % 4])
            card.text(195 + i * 180, 230, f"Box {i+1}", 14, INK, "middle")
        return
    if mode == "wire":
        card.rect(70, 190, 130, 64, "#0F172A", 8, 1, PAL[0])
        card.rect(395, 190, 130, 64, "#0F172A", 8, 1, PAL[1])
        card.rect(720, 190, 130, 64, "#0F172A", 8, 1, PAL[3])
        card.text(135, 228, "Pin A", 14, INK, "middle")
        card.text(460, 228, "Bus", 14, INK, "middle")
        card.text(785, 228, "Pin B", 14, INK, "middle")
        for y, color in ((204, PAL[0]), (222, PAL[1]), (240, PAL[3])):
            card.line(200, y, 395, y, color, 2)
            card.line(525, y, 720, y, color, 2)
        return
    if mode in {"deploy", "er", "lineage", "bpmn"}:
        labels = {
            "deploy": ["Browser", "API", "Store"],
            "er": ["Sample", "Assay", "Figure"],
            "lineage": ["Raw", "Clean", "Model", "Chart"],
            "bpmn": ["Start", "Task", "Gate", "End"],
        }[mode]
        for i, name in enumerate(labels):
            x = 70 + i * (760 / max(len(labels) - 1, 1))
            card.rect(x, 200, 130, 70, "#0F172A", 8, 1, PAL[i % 5])
            card.text(x + 65, 242, name, 14, INK, "middle")
            if i:
                card.line(x - 40, 235, x, 235, PAL[1], 2)
        return
    # force / bundle / default nodes
    nodes = [(rng.uniform(120, 800), rng.uniform(70, 450)) for _ in range(9)]
    hub = (460, 250)
    for i, (x, y) in enumerate(nodes):
        target = hub if mode == "bundle" else nodes[(i + 3) % 9]
        card.line(x, y, target[0], target[1], PAL[i % 5], 1.4, "0")
    card.circle(*hub, 18, PAL[3])
    for i, (x, y) in enumerate(nodes):
        card.circle(x, y, 9, PAL[i % 5])


def draw_math(card, mode):
    rng = card.rng
    if mode == "numline":
        card.line(60, 260, 860, 260, INK, 2)
        for i, lab in enumerate(["-2", "-1", "0", "1", "2", "3"]):
            x = 100 + i * 130
            card.line(x, 248, x, 272, INK, 1.5)
            card.text(x, 300, lab, 13, MUTED, "middle")
        card.rect(230, 248, 390, 24, PAL[0], 12, 0.35)
        card.text(425, 200, "[-1, 2)", 16, PAL[0], "middle")
        return
    if mode == "complex":
        card.line(80, 260, 860, 260, AXIS, 1.2)
        card.line(460, 40, 460, 480, AXIS, 1.2)
        card.line(460, 260, 680, 120, PAL[0], 2.4)
        card.circle(680, 120, 5, PAL[0])
        card.text(690, 112, "2+i", 14, INK)
        card.text(820, 284, "Re", 12, MUTED)
        card.text(472, 58, "Im", 12, MUTED)
        return
    if mode in {"vfield", "slopefield"}:
        for i in range(12):
            for j in range(8):
                x, y = 80 + i * 68, 50 + j * 54
                ang = math.atan2(y - 260, x - 460) if mode == "vfield" else math.sin(i / 2) - j / 8
                card.line(x, y, x + 18 * math.cos(ang), y + 18 * math.sin(ang), PAL[0], 1.5)
        return
    if mode == "phase":
        card.axes()
        pts = []
        for t in range(80):
            a = t / 12
            pts.append((460 + 160 * math.cos(a) * math.exp(-t / 90),
                        250 + 110 * math.sin(a) * math.exp(-t / 90)))
        card.poly(pts, "none", PAL[0], 2.2)
        return
    if mode == "riemann":
        card.axes(xlabel="x", ylabel="f(x)")
        for i in range(12):
            x = 80 + i * 60
            h = 40 + 180 * math.sin(i / 11 * math.pi)
            card.rect(x, 440 - h, 52, h, PAL[0], 0, 0.45, PAL[0])
        pts = [(80 + i * 8, 430 - 220 * math.sin(i / 88 * math.pi)) for i in range(89)]
        card.poly(pts, "none", PAL[3], 2.4)
        return
    if mode == "taylor":
        card.axes(xlabel="x", ylabel="y")
        true = [(70 + i * 8, 300 - 80 * math.sin(i / 8)) for i in range(90)]
        approx = [(70 + i * 8, 300 - 80 * (i / 20 - (i / 20) ** 3 / 6)) for i in range(50)]
        card.poly(true, "none", INK, 2.2)
        card.poly(approx, "none", PAL[0], 2.4)
        return
    if mode == "fourier":
        card.axes(xlabel="t", ylabel="sum")
        pts = []
        for i in range(100):
            t = i / 8
            y = 250 - 70 * math.sin(t) - 30 * math.sin(3 * t) - 16 * math.sin(5 * t)
            pts.append((60 + i * 8, y))
        card.poly(pts, "none", PAL[0], 2.4)
        return
    if mode == "eigen":
        card.line(180, 400, 760, 80, AXIS, 1)
        card.line(180, 80, 760, 400, AXIS, 1)
        card.path("M 460 250 m -180 0 a 180 90 20 1 0 360 0 a 180 90 20 1 0 -360 0", "none", PAL[0], 2.4)
        card.line(460, 250, 680, 180, PAL[3], 2)
        card.text(690, 176, "v1", 13, PAL[3])
        return
    if mode == "svd":
        card.path("M 160 170 L 300 130 L 300 330 L 160 370 Z", PAL[0], opacity=0.7)
        card.path("M 390 210 L 500 190 L 500 300 L 390 320 Z", PAL[1], opacity=0.8)
        card.path("M 590 150 L 780 190 L 780 360 L 590 320 Z", PAL[3], opacity=0.7)
        card.text(200, 430, "U", 16, INK, "middle")
        card.text(445, 430, "Σ", 16, INK, "middle")
        card.text(680, 430, "Vᵀ", 16, INK, "middle")
        return
    if mode == "lsq":
        card.line(80, 420, 820, 120, PAL[0], 2)
        card.line(80, 420, 820, 420, AXIS, 1.2)
        for i in range(8):
            x = 140 + i * 80
            y = 390 - i * 28 + rng.uniform(-24, 24)
            card.circle(x, y, 5, PAL[3])
            card.line(x, y, x, 420 - (x - 80) * 0.42, AXIS, 1, "3 3")
        return
    if mode == "conv":
        card.axes(xlabel="t", ylabel="signal")
        kernel = [(200 + i * 16, 300 - (20 if 2 < i < 8 else 0)) for i in range(12)]
        card.poly([(80 + i * 10, 360 - 40 * math.exp(-((i - 30) ** 2) / 80)) for i in range(70)], "none", INK, 2)
        card.rect(360, 250, 90, 70, PAL[0], 2, 0.35)
        card.text(405, 240, "window", 12, PAL[0], "middle")
        return
    if mode == "ptree":
        card.circle(460, 70, 8, PAL[0])
        for x in (250, 670):
            card.line(460, 78, x, 190, PAL[1], 1.6)
            card.circle(x, 200, 8, PAL[1])
        for x in (160, 340, 580, 780):
            parent = 250 if x < 460 else 670
            card.line(parent, 208, x, 340, PAL[3], 1.4)
            card.circle(x, 350, 7, PAL[3])
            card.text(x, 378, f"{rng.uniform(0.1, 0.4):.2f}", 11, MUTED, "middle")
        return
    if mode == "bayes":
        for i, (name, v) in enumerate([("Prior", 0.3), ("Likelihood", 0.8), ("Posterior", 0.62)]):
            card.text(80, 110 + i * 110, name, 14, INK)
            card.rect(230, 86 + i * 110, 560 * v, 36, PAL[i], 6)
        return
    if mode == "unitcircle":
        card.circle(430, 270, 150, "none", 1, AXIS, 1.4)
        card.line(430, 270, 430 + 150 * math.cos(0.8), 270 - 150 * math.sin(0.8), PAL[0], 2.2)
        card.line(430, 270, 580, 270, AXIS, 1)
        card.line(430, 120, 430, 420, AXIS, 1)
        card.text(560, 180, "θ", 16, PAL[0])
        return
    if mode == "proof":
        steps = ["Given AB ∥ CD", "Alternate angles equal", "Triangle congruence", "Therefore AD = BC"]
        for i, step in enumerate(steps):
            card.rect(70, 50 + i * 110, 780, 80, "#0F172A", 8, 1, PAL[i])
            card.text(96, 98 + i * 110, f"{i+1}  {step}", 18, INK)
        return


def draw_specialty(card):
    kind = card.fig["kind"]
    rng = card.rng
    slug = card.fig["slug"]
    if kind in {"volcano", "ma"}:
        card.axes(xlabel="log2 fold change" if kind == "volcano" else "mean expression",
                  ylabel="-log10 p" if kind == "volcano" else "log2 fold change")
        for _ in range(80):
            x = rng.uniform(90, 860)
            y = rng.uniform(80, 430)
            hot = abs(x - 460) > 180 and y < 220 if kind == "volcano" else abs(y - 246) > 80
            card.circle(x, y, 3.4, PAL[4] if hot else "#64748B", 0.85)
        return
    if kind == "manhattan":
        card.axes(xlabel="Chromosome", ylabel="-log10 p")
        x = 80
        for chrom in range(8):
            for _ in range(28):
                card.circle(x + rng.uniform(0, 80), 440 - rng.uniform(10, 280 if rng.random() > 0.92 else 80),
                            2.6, PAL[chrom % 2])
            x += 95
        card.line(70, 120, 880, 120, PAL[4], 1, "4 3")
        return
    if kind in {"enrichbub", "markerdot"}:
        for i in range(8):
            for j in range(4):
                r = rng.uniform(4, 16)
                card.circle(140 + j * 160, 70 + i * 50, r, PAL[j], 0.85)
            card.text(40, 76 + i * 50, f"P{i+1}", 12, MUTED)
        return
    if kind in {"enrichbar", "importance", "ablation", "alphadiv"}:
        draw_bars(card, "horizontal")
        return
    if kind == "gsea":
        card.axes(xlabel="Rank", ylabel="ES")
        pts = []
        y = 300
        for i in range(40):
            y -= 6 if i < 16 else -3
            pts.append((70 + i * 20, y))
        card.poly(pts, "none", PAL[0], 2.6)
        card.line(70, 300, 860, 300, AXIS, 1)
        return
    if kind in {"pathway", "signal", "wetlab", "process"}:
        draw_network(card, "flow")
        return
    if kind in {"godag", "cooccur"}:
        draw_network(card, "force")
        return
    if kind in {"circos", "plasmid"}:
        card.circle(460, 260, 150, "none", 1, PAL[0], 10)
        card.circle(460, 260, 120, "none", 1, PAL[1], 6)
        for i in range(7):
            a = i * math.pi / 3.5
            b = a + 0.5
            card.path(
                f"M {460+168*math.cos(a):.1f} {260+168*math.sin(a):.1f} "
                f"Q 460 260 {460+168*math.cos(b):.1f} {260+168*math.sin(b):.1f}",
                "none", PAL[i % 5], 2, 0.8)
        return
    if kind == "ideogram":
        for i in range(6):
            card.rect(80 + i * 130, 80, 36, 320, "#1E293B", 18, 1, PAL[i % 4])
            card.rect(80 + i * 130, 200, 36, 8, PAL[3], 0)
            card.text(98 + i * 130, 430, f"chr{i+1}", 12, MUTED, "middle")
        return
    if kind in {"gtrack", "coverage"}:
        card.axes(xlabel="Position", ylabel="Depth" if kind == "coverage" else "Signal")
        pts = [(70 + i * 12, 400 - rng.uniform(20, 220)) for i in range(64)]
        card.poly([(70, 440)] + pts + [(838, 440)], PAL[0], "none", 0, 0.35, True)
        card.rect(300, 70, 180, 18, PAL[3], 2, 0.8)
        return
    if kind in {"phylo", "timetree"}:
        draw_network(card, "tree")
        if kind == "timetree":
            card.line(80, 470, 840, 470, AXIS, 1.2)
            card.text(460, 498, "Million years", 12, MUTED, "middle")
        return
    if kind in {"treeheat", "cnv", "annotheat", "onco"}:
        draw_matrix(card, "annot" if kind == "onco" else "heat")
        return
    if kind in {"scumap", "pcoa", "embed"}:
        centers = [(250, 180), (520, 150), (680, 300), (360, 340)]
        for i, (cx, cy) in enumerate(centers):
            for _ in range(16):
                card.circle(cx + rng.uniform(-50, 50), cy + rng.uniform(-40, 40), 4, PAL[i], 0.85)
        return
    if kind in {"stackviolin", "violin"}:
        draw_dist(card, "violin")
        return
    if kind in {"pseudotime", "animal", "cohort"}:
        draw_lines(card, "one")
        return
    if kind == "velocity":
        draw_math(card, "vfield")
        return
    if kind in {"domlolli", "lollipop"}:
        for i in range(7):
            y = 70 + i * 56
            card.line(120, y, 120 + rng.uniform(200, 640), y, PAL[i % 5], 2)
            card.circle(120 + rng.uniform(200, 640), y, 7, PAL[i % 5])
            card.text(40, y + 4, f"G{i+1}", 12, MUTED)
        return
    if kind == "micro":
        draw_bars(card, "stacked")
        return
    if kind == "domains":
        card.rect(80, 220, 740, 36, "#1E293B", 6)
        for i, (x, w) in enumerate([(100, 120), (280, 180), (520, 90), (650, 140)]):
            card.rect(x, 212, w, 52, PAL[i], 8)
        return
    if kind == "organelle":
        card.circle(460, 260, 150, "none", 1, PAL[0], 3)
        card.path("M 400 220 C 430 180, 500 180, 520 230 C 500 250, 430 250, 400 220", PAL[1], opacity=0.7)
        card.circle(430, 300, 28, PAL[3], 0.8)
        card.text(460, 450, "Schematic cell", 13, MUTED, "middle")
        return
    if kind == "western":
        for lane in range(6):
            card.rect(90 + lane * 120, 60, 70, 380, "#0F172A", 4, 1, "#334155")
            for _ in range(rng.randint(2, 4)):
                card.rect(98 + lane * 120, rng.randint(90, 360), 54, 10, INK, 1)
        return
    if kind == "microscopy":
        for i in range(4):
            x, y = 50 + (i % 2) * 430, 40 + (i // 2) * 230
            card.rect(x, y, 400, 210, "#020617", 6, 1, PAL[i])
            for _ in range(12):
                card.circle(x + rng.randint(30, 360), y + rng.randint(30, 180), rng.uniform(4, 12), PAL[i], 0.8)
        card.line(80, 450, 180, 450, INK, 3)
        card.text(190, 454, "20 μm", 12, INK)
        return
    if kind in {"nmr", "ms", "ir", "xrd", "spectrum"}:
        card.axes(xlabel="ppm" if kind == "nmr" else "m/z" if kind == "ms" else "Shift", ylabel="Intensity")
        for i in range(18):
            x = 90 + i * 42
            h = rng.uniform(20, 300 if rng.random() > 0.7 else 80)
            card.line(x, 440, x, 440 - h, PAL[0] if kind != "ir" else PAL[3], 2)
        if kind == "ir":
            pts = [(70 + i * 8, 300 + 40 * math.sin(i / 3) - rng.uniform(0, 30)) for i in range(90)]
            card.poly(pts, "none", PAL[3], 1.8)
        return
    if kind in {"energy", "doseresp"}:
        pts = [(80 + i * 40, 360 - 180 * math.exp(-((i - 8) ** 2) / 18) + (20 if i in {4, 12} else 0)) for i in range(18)]
        card.axes(xlabel="Coordinate" if kind == "energy" else "Dose", ylabel="Energy" if kind == "energy" else "Response")
        card.poly(pts, "none", PAL[0], 2.6)
        return
    if kind in {"ballstick", "spacefill", "polymer"}:
        atoms = [(280, 250), (430, 170), (430, 330), (590, 250), (720, 170)]
        bonds = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]
        for a, b in bonds:
            card.line(*atoms[a], *atoms[b], INK, 4 if kind != "spacefill" else 16)
        for i, (x, y) in enumerate(atoms):
            card.circle(x, y, 28 if kind == "spacefill" else 14, PAL[i % 4])
        return
    if kind in {"esp", "orbital"}:
        card.path("M 250 260 C 300 80, 620 80, 680 260 C 620 440, 300 440, 250 260", PAL[0], opacity=0.35)
        card.path("M 360 250 C 400 160, 540 160, 580 260 C 540 340, 400 340, 360 250", PAL[4], opacity=0.45)
        return
    if kind in {"cycle", "catalytic-cycle"}:
        for i in range(5):
            a = -math.pi / 2 + i * 2 * math.pi / 5
            x, y = 460 + 150 * math.cos(a), 270 + 150 * math.sin(a)
            card.rect(x - 40, y - 22, 90, 44, "#0F172A", 8, 1, PAL[i])
            na = -math.pi / 2 + (i + 1) * 2 * math.pi / 5
            card.line(x, y, 460 + 150 * math.cos(na), 270 + 150 * math.sin(na), PAL[i], 1.6)
        return
    if kind in {"phasediag", "phase"}:
        card.line(80, 440, 840, 80, PAL[0], 2)
        card.line(80, 440, 500, 80, PAL[1], 2)
        card.line(500, 80, 840, 80, PAL[3], 2)
        card.text(200, 200, "Solid", 14, MUTED)
        card.text(620, 300, "Liquid", 14, MUTED)
        return
    if kind in {"cell", "unit-cell"}:
        card.path("M 250 300 L 460 200 L 690 300 L 460 400 Z", "none", PAL[0], 2)
        card.path("M 250 180 L 460 80 L 690 180 L 460 280 Z", "none", PAL[1], 2)
        card.line(250, 180, 250, 300, PAL[3], 1.6)
        card.line(460, 80, 460, 200, PAL[3], 1.6)
        card.line(690, 180, 690, 300, PAL[3], 1.6)
        return
    if kind == "battery":
        card.rect(180, 80, 560, 340, "none", 8, 1, INK)
        for i, color in enumerate([PAL[0], PAL[3], PAL[1], PAL[4], PAL[2]]):
            card.rect(230 + i * 90, 120, 48, 260, color, 2, 0.85)
        return
    if kind == "dosestruct":
        draw_points(card, "scatter")
        return
    if kind in {"rootlocus", "polezero", "poincare"}:
        card.line(80, 260, 860, 260, AXIS, 1.2)
        card.line(460, 40, 460, 480, AXIS, 1.2)
        for i in range(12):
            card.circle(200 + i * 40, 260 - math.sin(i) * 120, 5, PAL[0] if kind != "polezero" else PAL[4])
        if kind == "polezero":
            card.text(700, 80, "o zero   x pole", 12, MUTED)
        return
    if kind in {"stepresp", "wave", "spc", "changepoint"}:
        draw_lines(card, "one")
        if kind == "spc":
            card.line(64, 120, 880, 120, PAL[4], 1, "4 3")
            card.line(64, 360, 880, 360, PAL[4], 1, "4 3")
        return
    if kind == "nichols":
        pts = [(120 + i * 18, 360 - i * 6 + 30 * math.sin(i / 2)) for i in range(30)]
        card.poly(pts, "none", PAL[0], 2.4)
        card.circle(120, 360, 4, PAL[3])
        return
    if kind in {"spectrogram", "scalogram", "geoheat", "gridfield"}:
        for i in range(18):
            for j in range(10):
                v = abs(math.sin(i / 3) * math.cos(j / 2))
                card.rect(70 + i * 44, 40 + j * 42, 40, 38, PAL[0] if v > 0.4 else PAL[4], 1, 0.2 + v)
        return
    if kind == "constellation":
        for x in (-1, 1):
            for y in (-1, 1):
                for _ in range(10):
                    card.circle(460 + x * 120 + rng.uniform(-16, 16), 260 + y * 90 + rng.uniform(-16, 16), 3, PAL[0])
        return
    if kind == "antenna":
        card.circle(460, 270, 160, "none", 1, AXIS, 1)
        pts = []
        for i in range(60):
            a = i / 59 * 2 * math.pi
            r = 40 + 110 * abs(math.cos(a)) ** 2
            pts.append((460 + r * math.cos(a), 270 + r * math.sin(a)))
        card.poly(pts, PAL[0], PAL[0], 1.4, 0.35, True)
        return
    if kind in {"mesh", "stress", "stream2d", "isoslice"}:
        for i in range(8):
            for j in range(5):
                x, y = 80 + i * 100, 60 + j * 80
                card.path(f"M {x} {y} L {x+80} {y+16} L {x+60} {y+70} Z", "none", PAL[int(j) % 4], 1.2)
        return
    if kind == "optics":
        card.line(60, 260, 860, 260, AXIS, 1)
        card.path("M 300 140 L 340 260 L 300 380", "none", PAL[0], 3)
        card.line(60, 200, 320, 250, PAL[3], 1.6)
        card.line(340, 260, 800, 180, PAL[3], 1.6)
        return
    if kind == "circuit":
        card.line(80, 300, 200, 300, INK, 2)
        card.rect(200, 270, 80, 60, "none", 0, 1, INK)
        card.line(280, 300, 430, 300, INK, 2)
        card.circle(500, 300, 28, "none", 1, PAL[0], 2)
        card.line(528, 300, 760, 300, INK, 2)
        card.text(240, 250, "R", 14, MUTED, "middle")
        return
    if kind == "timing":
        for row in range(4):
            y = 80 + row * 100
            card.text(30, y + 20, f"D{row}", 12, MUTED)
            x = 80
            high = False
            while x < 860:
                w = rng.randint(40, 90)
                card.line(x, y + (10 if high else 40), x + w, y + (10 if high else 40), PAL[row % 4], 2)
                card.line(x + w, y + 10, x + w, y + 40, PAL[row % 4], 2)
                x += w
                high = not high
        return
    if kind == "bytefield":
        x = 40
        for i, w in enumerate([80, 120, 160, 90, 140, 180]):
            card.rect(x, 180, w, 80, PAL[i % 5], 2, 0.85)
            card.text(x + 8, 226, f"{w//10}b", 12, "#041018")
            x += w
        return
    if kind == "rack":
        for i in range(6):
            card.rect(260, 40 + i * 72, 400, 60, "#0F172A", 4, 1, PAL[i % 4])
            card.text(280, 76 + i * 72, f"U{i+1}  module", 14, INK)
        return
    if kind == "rigid":
        card.line(200, 360, 760, 360, PAL[0], 2)
        card.line(200, 360, 200, 80, PAL[1], 2)
        card.line(200, 360, 520, 160, PAL[3], 2)
        card.text(740, 384, "x", 14, PAL[0])
        card.text(180, 70, "y", 14, PAL[1])
        return
    if kind == "bifurcation":
        for x in range(40):
            for _ in range(6):
                card.circle(80 + x * 18, 260 + math.sin(x / 3) * rng.uniform(-80, 80), 1.8, PAL[0], 0.8)
        return
    if kind == "frame":
        draw_frame(card)
        return
    if kind in {"threeline", "coeftab", "basetab", "league", "risktab", "diag"}:
        draw_table(card)
        return
    if kind in {"codeblock", "pseudocode", "terminal"}:
        draw_code(card)
        return
    if kind in {"colorkey", "colorbar"}:
        for i in range(20):
            card.rect(80 + i * 36, 200, 36, 28, PAL[0], 0, i / 20)
        card.text(80, 260, "low", 12, MUTED)
        card.text(790, 260, "high", 12, MUTED, "end")
        return
    if kind in {"consort", "prisma", "enroll"}:
        labels = ["Screened", "Excluded", "Randomized", "Arm A", "Arm B", "Analyzed"]
        for i, name in enumerate(labels):
            x = 340 if i < 3 else 140 + (i - 3) * 240
            y = 40 + i * 70 if i < 3 else 280
            card.rect(x, y, 180, 46, "#0F172A", 6, 1, PAL[i % 4])
            card.text(x + 90, y + 28, name, 13, INK, "middle")
        return
    if kind in {"nomogram", "dca", "biasfunnel", "spider", "swimmer", "tumorfall"}:
        draw_clinical(card)
        return
    if kind in {"pointmap", "choropleth", "propsym", "flowmap", "geohex", "isomap", "voronoi",
                "trajmap", "terrain", "section", "mapframe", "smallmaps", "od", "admin"}:
        draw_map(card)
        return
    if kind in {"cellsig", "apparatus", "organs", "ladder", "mechpair", "icontime", "iconflow",
                "cmpboard", "hypothesis", "absquad", "coverlay", "hmscale", "pipette",
                "instrument", "hazard", "spring", "bridge", "methods"}:
        draw_illustration(card)
        return
    if kind in {"acf", "pacf", "spark", "km", "cuminc", "gantt", "seasonal"}:
        draw_time_extra(card)
        return
    if kind in {"density", "hist"}:
        draw_bars(card, "basic")
        return
    if kind in {"hexbin", "density2d", "contour"}:
        draw_matrix(card, "heat")
        return
    if kind in {"confusion", "learncurve", "valcurve", "multiroc", "shapbee", "shapfall",
                "pdp", "ice", "nnblock", "unet", "transformer", "tokenflow", "hparam", "gradcam"}:
        draw_ml(card)
        return
    # Last-resort visible chart so a missed kind still renders data, then QA can reject sameness.
    card.axes(xlabel=slug, ylabel=kind)
    draw_lines(card, "many")


def draw_frame(card):
    slug = card.fig["slug"]
    if slug == "journal-single":
        card.rect(250, 30, 420, 460, "none", 4, 1, PAL[0])
        card.text(460, 60, "85 mm", 14, PAL[0], "middle")
    elif slug == "journal-double":
        card.rect(40, 40, 400, 440, "none", 4, 1, PAL[0])
        card.rect(470, 40, 400, 440, "none", 4, 1, PAL[1])
    elif slug == "panel-labels":
        for i, lab in enumerate("ABCDEF"):
            x, y = 40 + (i % 3) * 290, 40 + (i // 3) * 230
            card.rect(x, y, 270, 210, "#0F172A", 6, 1, "#334155")
            card.text(x + 12, y + 28, lab, 18, PAL[0], "start", "700")
    elif slug == "slide-16x9":
        card.rect(40, 70, 840, 380, "none", 4, 1, PAL[0])
        card.text(460, 50, "16:9 safe area", 14, PAL[0], "middle")
    elif slug == "slide-4x3":
        card.rect(130, 30, 660, 460, "none", 4, 1, PAL[3])
    elif slug == "poster-a0":
        for i in range(3):
            card.rect(40 + i * 290, 30, 270, 460, "#0F172A", 6, 1, PAL[i])
    elif slug == "graphical-slot":
        card.rect(40, 120, 840, 280, "none", 6, 1, PAL[1])
        card.text(460, 260, "Graphical abstract", 18, INK, "middle")
    elif slug == "video-lower-third":
        card.rect(30, 30, 860, 460, "none", 4, 1, AXIS)
        card.rect(30, 380, 860, 110, PAL[0], 0, 0.25)
    elif slug == "inset-zoom":
        card.rect(40, 40, 520, 440, "#0F172A", 6, 1, AXIS)
        card.rect(180, 160, 90, 70, "none", 2, 1, PAL[3])
        card.line(270, 195, 600, 80, PAL[3], 1.4)
        card.rect(600, 40, 270, 200, "#0F172A", 6, 1, PAL[3])
    elif slug == "before-after":
        card.rect(40, 40, 400, 440, "#0F172A", 6, 1, PAL[4])
        card.rect(480, 40, 400, 440, "#0F172A", 6, 1, PAL[1])
        card.text(240, 70, "Before", 16, PAL[4], "middle")
        card.text(680, 70, "After", 16, PAL[1], "middle")
    elif slug == "caption-scale":
        card.rect(40, 40, 840, 320, "#0F172A", 6)
        card.text(50, 400, "Figure 1. Caption sits outside the plot box.", 14, INK)
        card.line(50, 450, 180, 450, INK, 3)
        card.text(190, 454, "1 cm", 12, MUTED)
    elif slug == "method-rail":
        card.rect(40, 40, 560, 440, "#0F172A", 6, 1, AXIS)
        card.rect(630, 40, 250, 440, "#0F172A", 6, 1, PAL[0])
        card.text(650, 70, "Methods", 16, PAL[0])
    else:
        for i in range(6):
            card.rect(40 + (i % 3) * 290, 40 + (i // 3) * 230, 270, 210, "#0F172A", 4, 1, "#334155")


def draw_table(card):
    headers = ["Term", "Estimate", "Interval", "n"]
    rows = [("Intercept", "0.42", "0.31–0.53", "128"),
            ("Dose", "1.16", "0.94–1.38", "128"),
            ("Site B", "-0.22", "-0.41–-0.03", "64"),
            ("Batch", "0.07", "-0.05–0.19", "128")]
    for i, head in enumerate(headers):
        card.text(60 + i * 200, 70, head, 13, PAL[0], "start", "700")
    card.line(50, 84, 860, 84, INK, 1.4)
    for r, row in enumerate(rows):
        for i, cell in enumerate(row):
            card.text(60 + i * 200, 130 + r * 64, cell, 15, INK)
    card.line(50, 400, 860, 400, INK, 1.4)


def draw_code(card):
    card.rect(40, 30, 840, 460, "#020617", 8, 1, "#1E293B")
    lines = [
        "atlas.render(figure_id)",
        "frame = atlas.fit(column='single')",
        "frame.export('figure.svg')",
        "# caption stays outside the axes",
    ] if card.fig["kind"] != "terminal" else [
        "$ figureatlas render 042",
        "wrote assets/gallery/atlas/042.svg",
        "check: labels inside viewBox",
        "status: pass",
    ]
    for i, line in enumerate(lines):
        card.text(30, 80 + i * 48, f"{i+1:02}", 14, "#475569")
        card.text(80, 80 + i * 48, line, 16, PAL[1] if line.startswith("#") or line.startswith("$") else INK)


def draw_clinical(card):
    kind = card.fig["kind"]
    rng = card.rng
    if kind == "nomogram":
        for i, name in enumerate(["Points", "Age", "Stage", "Total", "Risk"]):
            y = 60 + i * 80
            card.text(40, y, name, 13, MUTED)
            card.line(140, y - 6, 860, y - 6, AXIS, 1.2)
            for t in range(6):
                card.line(160 + t * 110, y - 14, 160 + t * 110, y + 2, INK, 1)
        return
    if kind == "dca":
        card.axes(xlabel="Threshold", ylabel="Net benefit")
        card.poly([(70 + i * 20, 400 - i * 4) for i in range(30)], "none", AXIS, 1.4)
        card.poly([(70 + i * 20, 380 - 80 * math.sin(i / 10)) for i in range(30)], "none", PAL[0], 2.4)
        return
    if kind == "biasfunnel":
        card.axes(xlabel="Effect", ylabel="Precision")
        for i in range(24):
            y = 80 + i * 12
            card.circle(460 + rng.uniform(-1, 1) * (240 - i * 8), y, 4, PAL[0])
        return
    if kind == "spider":
        card.line(80, 300, 860, 300, AXIS, 1)
        for s in range(4):
            pts = [(80 + i * 40, 300 - (i - 8) * rng.uniform(-8, 8)) for i in range(18)]
            card.poly(pts, "none", PAL[s], 1.8)
        return
    if kind == "swimmer":
        for i in range(7):
            y = 60 + i * 58
            card.rect(120, y, rng.uniform(180, 640), 24, PAL[i % 5], 12)
            card.circle(120 + rng.uniform(40, 200), y + 12, 6, INK)
        return
    if kind == "tumorfall":
        vals = sorted([rng.uniform(-0.7, 0.55) for _ in range(18)])
        for i, v in enumerate(vals):
            x = 70 + i * 44
            h = abs(v) * 280
            y = 250 - h if v >= 0 else 250
            card.rect(x, y, 28, h, PAL[4] if v >= 0 else PAL[1], 2)
        card.line(60, 250, 870, 250, AXIS, 1.2)


def draw_map(card):
    kind = card.fig["kind"]
    rng = card.rng
    coast = [(80, 300), (160, 180), (280, 120), (420, 160), (520, 110),
             (690, 180), (820, 150), (860, 280), (760, 390), (540, 430),
             (300, 400), (120, 360)]
    card.poly(coast, "#102033", PAL[0], 2, 1, True)
    if kind == "choropleth":
        card.path("M 160 180 L 300 150 L 280 300 L 150 320 Z", PAL[1], opacity=0.55)
        card.path("M 420 160 L 620 140 L 640 300 L 430 320 Z", PAL[3], opacity=0.5)
    elif kind == "propsym":
        for x, y, r in ((240, 220, 10), (500, 200, 22), (700, 250, 16)):
            card.circle(x, y, r, PAL[3], 0.8)
    elif kind == "flowmap":
        card.path("M 200 240 C 360 80, 560 80, 720 220", "none", PAL[3], 3, 0.8)
    elif kind == "geohex":
        for i in range(8):
            for j in range(4):
                card.circle(180 + i * 70, 160 + j * 60, 16, PAL[(i + j) % 4], 0.7)
    elif kind == "trajmap":
        card.poly([(180, 340), (300, 260), (460, 220), (640, 250), (760, 180)], "none", PAL[3], 2.4)
    elif kind == "terrain":
        card.path("M 120 360 L 250 200 L 400 280 L 560 140 L 760 320 L 120 360", PAL[1], opacity=0.4)
    elif kind == "section":
        card.poly([(60, 300), (200, 180), (360, 240), (560, 120), (860, 260), (860, 460), (60, 460)],
                  PAL[0], "none", 0, 0.35, True)
    elif kind == "smallmaps":
        for i in range(4):
            card.rect(40 + (i % 2) * 440, 40 + (i // 2) * 230, 400, 200, "#0F172A", 6, 1, PAL[i])
            card.circle(180 + (i % 2) * 440, 140 + (i // 2) * 230, 8, PAL[3])
    elif kind == "od":
        for i in range(5):
            card.line(rng.randint(140, 300), rng.randint(160, 380),
                      rng.randint(560, 800), rng.randint(150, 360), PAL[i % 4], 1.6)
    elif kind == "isomap":
        for ring, rad in enumerate((46, 86, 126)):
            card.path(
                f"M {430-rad} 250 C {430-rad} {250-rad*0.62}, {430+rad} {250-rad*0.62}, {430+rad} 250 "
                f"C {430+rad} {250+rad*0.5}, {430-rad} {250+rad*0.5}, {430-rad} 250",
                "none", PAL[ring % 3], 1.8)
        card.circle(430, 250, 4, PAL[3])
    elif kind == "admin":
        card.line(300, 140, 300, 400, PAL[0], 1.4)
        card.line(140, 260, 760, 260, PAL[1], 1.4)
        card.text(180, 180, "North", 13, MUTED)
        card.text(520, 330, "South", 13, MUTED)
    elif kind == "mapframe":
        card.line(70, 430, 190, 430, INK, 3)
        card.text(200, 434, "100 km", 12, INK)
        card.path("M 800 80 L 800 140 L 830 100 Z", PAL[3])
        card.text(780, 70, "N", 12, INK)
    else:
        for _ in range(18):
            card.circle(rng.uniform(160, 780), rng.uniform(150, 380), 4, PAL[3])
    card.text(70, 40, "Schematic study region", 13, MUTED)


def draw_illustration(card):
    kind = card.fig["kind"]
    if kind == "cellsig":
        card.circle(180, 260, 70, PAL[0], 0.8)
        card.rect(360, 220, 140, 80, PAL[1], 8)
        card.circle(700, 260, 50, PAL[3], 0.85)
        card.line(250, 260, 360, 260, INK, 2)
        card.line(500, 260, 650, 260, INK, 2)
    elif kind == "apparatus":
        card.rect(140, 200, 80, 180, "none", 4, 1, INK)
        card.rect(300, 120, 200, 260, "none", 4, 1, PAL[0])
        card.line(220, 250, 300, 220, INK, 2)
    elif kind == "organs":
        for i, name in enumerate(["Heart", "Lung", "Liver", "Kidney"]):
            card.circle(140 + i * 190, 220, 48, PAL[i], 0.85)
            card.text(140 + i * 190, 320, name, 14, INK, "middle")
    elif kind == "ladder":
        for i, name in enumerate(["Molecule", "Cell", "Tissue", "Organ"]):
            card.rect(80, 60 + i * 100, 180 + i * 120, 64, PAL[i], 6, 0.85)
            card.text(100, 100 + i * 100, name, 16, "#041018")
    elif kind == "mechpair":
        card.circle(250, 250, 70, PAL[4], 0.8)
        card.circle(670, 250, 70, PAL[1], 0.8)
        card.line(340, 250, 560, 250, INK, 2)
    elif kind in {"icontime", "iconflow"}:
        for i in range(4):
            card.rect(50 + i * 210, 200, 160, 70, PAL[i], 8)
            card.text(130 + i * 210, 242, f"Step {i+1}", 14, "#041018", "middle")
    elif kind == "cmpboard":
        card.rect(60, 80, 360, 320, "#0F172A", 8, 1, PAL[4])
        card.rect(500, 80, 360, 320, "#0F172A", 8, 1, PAL[1])
    elif kind == "hypothesis":
        card.rect(360, 40, 200, 60, PAL[0], 8)
        card.line(460, 100, 220, 220, INK, 1.6)
        card.line(460, 100, 700, 220, INK, 1.6)
        card.rect(120, 220, 180, 54, PAL[1], 6)
        card.rect(610, 220, 180, 54, PAL[3], 6)
    elif kind in {"absquad", "coverlay"}:
        for i in range(4):
            card.rect(40 + (i % 2) * 440, 40 + (i // 2) * 230, 410, 200, "#0F172A", 8, 1, PAL[i])
    elif kind == "hmscale":
        card.rect(180, 80, 70, 320, PAL[0], 8, 0.8)
        card.rect(460, 220, 46, 180, PAL[3], 6, 0.8)
        card.text(215, 430, "Human", 13, MUTED, "middle")
        card.text(483, 430, "Mouse", 13, MUTED, "middle")
    elif kind == "pipette":
        for i in range(4):
            card.rect(80 + i * 200, 80, 40, 220, PAL[i], 4, 0.8)
            card.rect(70 + i * 200, 300, 80, 36, "#1E293B", 4)
    elif kind == "instrument":
        card.rect(80, 80, 760, 340, "#0F172A", 10, 1, PAL[0])
        for i in range(5):
            card.circle(180 + i * 120, 250, 28, PAL[i])
    elif kind == "hazard":
        for i, name in enumerate(["Control", "Heat", "Solvent", "Sharps"]):
            card.rect(60 + i * 210, 160, 180, 140, "#0F172A", 8, 1, PAL[i])
            card.text(150 + i * 210, 236, name, 16, INK, "middle")
    elif kind == "spring":
        pts = [(80, 260)]
        for i in range(12):
            pts.append((120 + i * 40, 200 if i % 2 == 0 else 320))
        pts.append((760, 260))
        card.poly(pts, "none", PAL[0], 2.4)
        card.rect(760, 230, 70, 60, PAL[3], 4)
    elif kind == "bridge":
        card.rect(60, 180, 240, 90, PAL[0], 8)
        card.rect(620, 180, 240, 90, PAL[1], 8)
        card.line(300, 225, 620, 225, INK, 2)
        card.text(180, 232, "Concept", 16, "#041018", "middle")
        card.text(740, 232, "Formula", 16, "#041018", "middle")
    else:
        card.rect(40, 180, 840, 80, "#0F172A", 6, 1, PAL[0])
        card.text(60, 228, "Methods credit  ·  renderer  ·  palette  ·  export", 16, INK)


def draw_time_extra(card):
    kind = card.fig["kind"]
    rng = card.rng
    if kind in {"acf", "pacf"}:
        card.axes(xlabel="Lag", ylabel="Correlation")
        card.line(64, 180, 880, 180, PAL[4], 1, "4 3")
        for i in range(16):
            h = rng.uniform(-120, 140) * math.exp(-i / 6)
            y = 246 - max(h, 0)
            card.rect(80 + i * 48, y if h > 0 else 246, 16, abs(h), PAL[0], 1)
        return
    if kind == "spark":
        for i in range(6):
            pts = [(140 + k * 16, 70 + i * 70 - rng.uniform(0, 30)) for k in range(24)]
            card.text(40, 74 + i * 70, f"S{i+1}", 12, MUTED)
            card.poly(pts, "none", PAL[i % 4], 1.8)
        return
    if kind == "km":
        card.axes(xlabel="Time", ylabel="Survival")
        y = 70
        x = 70
        pts = [(70, 70)]
        for _ in range(8):
            x += 90
            pts.append((x, y))
            y += rng.randint(24, 48)
            pts.append((x, y))
        card.poly(pts, "none", PAL[0], 2.6)
        return
    if kind == "cuminc":
        draw_lines(card, "area")
        return
    if kind == "gantt":
        for i, name in enumerate(["Design", "Acquire", "Fit", "Review", "Export"]):
            card.text(40, 90 + i * 70, name, 13, MUTED)
            card.rect(180 + i * 30, 68 + i * 70, 160 + i * 40, 28, PAL[i], 6)
        return
    if kind == "seasonal":
        for row in range(3):
            pts = [(80 + i * 18, 80 + row * 140 + 30 * math.sin(i / 2 + row)) for i in range(40)]
            card.poly(pts, "none", PAL[row], 2)
        return


def draw_ml(card):
    kind = card.fig["kind"]
    rng = card.rng
    if kind == "confusion":
        draw_matrix(card, "confusion")
    elif kind in {"learncurve", "valcurve", "pdp"}:
        draw_lines(card, "many" if kind != "pdp" else "one")
    elif kind == "multiroc":
        draw_points(card, "roc")
        draw_lines(card, "many")
    elif kind == "shapbee":
        draw_dist(card, "bee")
    elif kind == "shapfall":
        draw_bars(card, "waterfall")
    elif kind == "ice":
        draw_lines(card, "many")
    elif kind == "hparam":
        for s in range(5):
            pts = [(80 + i * 150, rng.uniform(60, 440)) for i in range(5)]
            card.poly(pts, "none", PAL[s], 1.6)
            for x, y in pts:
                card.circle(x, y, 4, PAL[s])
    elif kind == "gradcam":
        card.rect(80, 50, 760, 400, "#020617", 6, 1, AXIS)
        card.rect(280, 140, 220, 180, PAL[4], 4, 0.45)
        card.rect(340, 180, 90, 80, PAL[3], 4, 0.7)
    elif kind == "unet":
        for i, w in enumerate([40, 70, 100, 70, 40]):
            x = 80 + i * 150
            card.rect(x, 260 - w, 50, w * 2, PAL[i % 4], 3, 0.85)
            if i < 4:
                card.line(x + 50, 260, x + 150, 260, INK, 1.4)
        card.path("M 130 180 C 300 40, 620 40, 760 180", "none", PAL[3], 1.6)
    elif kind == "transformer":
        blocks = ["Norm", "Attention", "Norm", "MLP"]
        for i, name in enumerate(blocks):
            card.rect(250, 40 + i * 110, 420, 70, "#0F172A", 8, 1, PAL[i])
            card.text(460, 82 + i * 110, name, 16, INK, "middle")
    elif kind == "tokenflow":
        for i in range(6):
            card.rect(40 + i * 145, 200, 110, 48, PAL[i % 4], 6)
            card.text(95 + i * 145, 230, f"t{i}", 14, "#041018", "middle")
        card.path("M 90 248 C 200 360, 500 80, 800 248", "none", INK, 1.6)
    else:
        for i, name in enumerate(["Input", "Hidden", "Hidden", "Output"]):
            for j in range(3 if i not in {0, 3} else 2):
                card.circle(140 + i * 200, 140 + j * 90, 16, PAL[i])
            if i < 3:
                card.line(160 + i * 200, 230, 320 + i * 200, 230, AXIS, 1.2)


KIND_ROUTE = {
    "hist": ("bars", "basic"), "gbar": ("bars", "grouped"), "sbar": ("bars", "stacked"),
    "pbar": ("bars", "percent"), "waterfall": ("bars", "waterfall"), "shapfall": ("bars", "waterfall"),
    "funnel": ("bars", "basic"), "bullet": ("bars", "grouped"), "errorbar": ("bars", "grouped"),
    "pointrange": ("bars", "grouped"), "brackets": ("bars", "grouped"), "pyramid": ("bars", "pyramid"),
    "lollipop": ("bars", "horizontal"), "cleveland": ("bars", "horizontal"),
    "dumbbell": ("bars", "horizontal"), "slope": ("bars", "horizontal"),
    "enrichbar": ("bars", "horizontal"), "importance": ("bars", "horizontal"),
    "ablation": ("bars", "horizontal"), "alphadiv": ("bars", "horizontal"),
    "box": ("dist", "box"), "notchbox": ("dist", "notch"), "violin": ("dist", "violin"),
    "raincloud": ("dist", "rain"), "beeswarm": ("dist", "bee"), "jitterbox": ("dist", "jitter"),
    "ridge": ("dist", "ridge"), "ecdf": ("dist", "ecdf"), "qq": ("dist", "qq"),
    "shapbee": ("dist", "bee"), "stackviolin": ("dist", "violin"),
    "density": ("lines", "area"), "line": ("lines", "one"), "multiline": ("lines", "many"),
    "area": ("lines", "area"), "stackarea": ("lines", "stack"), "stream": ("lines", "stream"),
    "step": ("lines", "step"), "fan": ("lines", "fan"), "learncurve": ("lines", "many"),
    "valcurve": ("lines", "many"), "pdp": ("lines", "one"), "ice": ("lines", "many"),
    "pseudotime": ("lines", "one"), "animal": ("lines", "one"), "cohort": ("lines", "one"),
    "scatter": ("points", "scatter"), "bubble": ("points", "bubble"),
    "residual": ("points", "residual"), "bland": ("points", "bland"),
    "roc": ("points", "roc"), "pr": ("points", "pr"), "calibration": ("points", "calibration"),
    "multiroc": ("points", "roc"), "pca": ("points", "scatter"), "splom": ("points", "scatter"),
    "dosestruct": ("points", "scatter"),
    "corrmat": ("matrix", "heat"), "clustermap": ("matrix", "clustermap"),
    "annotheat": ("matrix", "annot"), "tricorr": ("matrix", "tri"),
    "confusion": ("matrix", "confusion"), "adjmat": ("matrix", "heat"),
    "treeheat": ("matrix", "heat"), "cnv": ("matrix", "heat"), "onco": ("matrix", "annot"),
    "pie": ("hier", "pie"), "donut": ("hier", "donut"), "sunburst": ("hier", "sunburst"),
    "treemap": ("hier", "treemap"), "icicle": ("hier", "icicle"), "circlepack": ("hier", "pack"),
    "waffle": ("hier", "waffle"), "mosaic": ("hier", "mosaic"), "mekko": ("hier", "mekko"),
    "venn": ("hier", "venn"), "upset": ("hier", "upset"), "euler": ("hier", "euler"),
    "proparea": ("hier", "proparea"), "nesteddonut": ("hier", "nested"),
    "sankey": ("net", "sankey"), "alluvial": ("net", "alluvial"), "chord": ("net", "chord"),
    "arc": ("net", "arc"), "force": ("net", "force"), "bundle": ("net", "bundle"),
    "flow": ("net", "flow"), "swimlane": ("net", "swim"), "sequence": ("net", "sequence"),
    "state": ("net", "state"), "mindmap": ("net", "mind"), "fishbone": ("net", "fish"),
    "dtree": ("net", "tree"), "c4": ("net", "c4"), "deploy": ("net", "deploy"),
    "er": ("net", "er"), "lineage": ("net", "lineage"), "bpmn": ("net", "bpmn"),
    "wire": ("net", "wire"), "corrnet": ("net", "force"), "godag": ("net", "force"),
    "cooccur": ("net", "force"), "pathway": ("net", "flow"), "signal": ("net", "flow"),
    "wetlab": ("net", "flow"), "process": ("net", "flow"),
    "numline": ("math", "numline"), "complex": ("math", "complex"), "vfield": ("math", "vfield"),
    "phase": ("math", "phase"), "slopefield": ("math", "slopefield"), "riemann": ("math", "riemann"),
    "taylor": ("math", "taylor"), "fourier": ("math", "fourier"), "eigen": ("math", "eigen"),
    "svd": ("math", "svd"), "lsq": ("math", "lsq"), "conv": ("math", "conv"),
    "ptree": ("math", "ptree"), "bayes": ("math", "bayes"), "unitcircle": ("math", "unitcircle"),
    "proof": ("math", "proof"), "velocity": ("math", "vfield"),
}


def render_new(fig):
    card = Card(fig)
    kind = fig["kind"]
    route = KIND_ROUTE.get(kind)
    if route:
        family, mode = route
        {"bars": draw_bars, "dist": draw_dist, "lines": draw_lines, "points": draw_points,
         "matrix": draw_matrix, "hier": draw_hierarchy, "net": draw_network,
         "math": draw_math}[family](card, mode)
    elif kind == "frame":
        draw_frame(card)
    elif kind == "forest":
        forest_plot(card)
    else:
        draw_specialty(card)
    svg = card.finish()
    if "NaN" in svg or "Infinity" in svg:
        raise ValueError(f"{fig['id']} produced a non-finite coordinate")
    return svg


def render_legacy(fig, gallery):
    from pathlib import Path
    stem = fig["legacy"]
    html_path = Path(gallery) / f"{stem}.html"
    png_path = Path(gallery) / f"{stem}.png"
    if not html_path.is_file() or not png_path.is_file():
        raise FileNotFoundError(stem)
    return html_path.read_text(encoding="utf-8"), png_path


def page(inner):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>FigureAtlas</title>
<style>
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: #060911; font-family: "Segoe UI", "Microsoft YaHei", sans-serif; }}
.atlas-card {{ width: 960px; background: #0d121f; border: 1px solid rgba(255,255,255,.08); border-radius: 12px; padding: 16px 16px 12px; }}
.kicker {{ margin: 0; color: #38BDF8; font-size: 12px; letter-spacing: .08em; text-transform: uppercase; }}
h2 {{ margin: 4px 0 0; color: #F8FAFC; font-size: 22px; font-weight: 700; }}
.zh {{ margin: 2px 0 10px; color: #94A3B8; font-size: 14px; }}
.plot svg {{ width: 100%; height: auto; display: block; border-radius: 8px; }}
</style>
</head>
<body>{inner}</body>
</html>"""


if __name__ == "__main__":
    print(len(FIGURES))
