# FigureAtlas

**English** | [中文说明](README_ZH.md)

> **300 verified figure types for papers, slides, posters, and video frames.**

[![Figures](https://img.shields.io/badge/figures-300-blue.svg)](CATALOG.md)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Agent skill](https://img.shields.io/badge/Agent%20skill-ready-emerald.svg)](skills/visual-storyboard-designer/SKILL.md)

FigureAtlas is a figure catalog for people and coding agents. A paper, a slide, and a poster often need the same result in different frames. The catalog names the figure once. The frame is chosen separately.

The old project name was Scientific Visual Studio. The repository is now `figureatlas`, which is easier to say and easier to search.

## What is in the box

- **300 figure types** across 15 families. The full index is [CATALOG.md](CATALOG.md).
- **A screenshot for every type.** Verification writes the PNG before the figure is added to the gallery. See [GALLERY.md](GALLERY.md).
- **26 specialized scientific renderers** from the previous release: Bloch sphere, Bode plot, sequence logo, reaction scheme, Feynman diagram, and the rest.
- **One call for the whole catalog.**

```python
from figureatlas import render_figure
html = render_figure("161")  # volcano plot
```

## Families

| Family | Figures | Start here |
|---|---:|---|
| Format adapters | 18 | Journal column, 16:9 slide, A0 poster |
| Distribution and comparison | 28 | Histogram, box plot, forest plot |
| Correlation and dimension reduction | 20 | Scatter, heatmap, PCA |
| Time and process | 16 | Line, Kaplan-Meier, Gantt |
| Part-to-whole and sets | 14 | Treemap, Venn, UpSet |
| Networks and systems | 25 | Sankey, sequence, C4 |
| Mathematics and derivation | 18 | Basis map, slope field, proof |
| Model structure and evaluation | 20 | Confusion matrix, SHAP, U-Net |
| Life science and omics | 37 | Volcano, Circos, UMAP |
| Chemistry and materials | 17 | Reaction scheme, NMR, unit cell |
| Physics, engineering, and signals | 28 | Bode, Smith chart, waveform |
| Maps and space | 16 | Choropleth, flow map, trajectory |
| Scientific illustration | 20 | Mechanism, apparatus, graphical abstract |
| Tables, code, and legends | 8 | Three-line table, code block |
| Clinical and epidemiology | 15 | CONSORT, swimmer, nomogram |

The gallery screenshots live in `assets/gallery/atlas/`. The staging copies used for the pass/fail check stay in `assets/gallery/_staging/`.

## License

[Apache 2.0](LICENSE).
