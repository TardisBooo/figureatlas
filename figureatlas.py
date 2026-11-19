# -*- coding: utf-8 -*-
"""Public FigureAtlas entry points."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "incoming"))

from catalog_data import FIGURES  # noqa: E402
from render_atlas import page, render_new  # noqa: E402

BY_ID = {fig["id"]: fig for fig in FIGURES}
BY_SLUG = {fig["slug"]: fig for fig in FIGURES}


def get_figure(figure_id):
    key = str(figure_id).zfill(3) if str(figure_id).isdigit() else str(figure_id)
    fig = BY_ID.get(key) or BY_SLUG.get(key)
    if fig is None:
        raise KeyError(figure_id)
    return fig


def render_figure(figure_id):
    """Return a standalone HTML page for one verified catalog figure."""
    fig = get_figure(figure_id)
    if fig["legacy"]:
        html_path = ROOT / "assets" / "gallery" / f"{fig['legacy']}.html"
        return html_path.read_text(encoding="utf-8")
    return page(render_new(fig))


def list_figures(family=None):
    rows = FIGURES if family is None else [fig for fig in FIGURES if fig["family"] == family]
    return [dict(fig) for fig in rows]
