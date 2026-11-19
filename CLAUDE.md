# CLAUDE.md — FigureAtlas

FigureAtlas is a catalog of 300 verified figure types for papers, slides, posters, and video frames. The repository was previously called Scientific Visual Studio.

When a prompt asks for a figure, read `skills/visual-storyboard-designer/SKILL.md`, choose one id from `CATALOG.md`, and render it:

```python
from figureatlas import render_figure
html = render_figure("161")
```

Screenshots used on the gallery page are the files checked in `assets/gallery/atlas/`.
Do not add a figure id that is not already in `CATALOG.md`.
