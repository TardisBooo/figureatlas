# Scientific Visual Studio 🧪✨

> **Domain-Agnostic Scientific, AI & Mathematical Visual Computation Studio for Agents, Slides, and Video Productions.**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-Ready-emerald.svg)](skills/visual-storyboard-designer/SKILL.md)
[![Style: Cyber--Academic](https://img.shields.io/badge/Style-Cyber--Academic-indigo.svg)](GALLERY.md)

---

## 🌟 Overview

**Scientific Visual Studio** is an open-source, domain-agnostic scientific visualization library and autonomous agent skill. Inspired by tools like **3Blue1Brown's Manim**, **SciencePlots**, **PlotNeuralNet**, and **Observable D3**, it provides a modular suite of 17+ procedural visual components and multi-pane cyber-academic layout engines.

Unlike static image generators or ad-hoc plotting scripts, Scientific Visual Studio renders **crisp, responsive HTML/SVG components** with embedded dynamic styling, mathematical notation, and interactive telemetry—ready to be embedded into Remotion video timelines, Reveal.js slides, web applications, or saved directly as publication-quality graphics.

---

## 🎨 Visual Component Gallery

| Component | Visual Preview | Category | Description |
|---|---|---|---|
| **01. Hero Cover** | <img src="assets/gallery/01_hero_cover.png" width="320"/> | Layout | High-impact cinematic cover with glowing mesh gradients & telemetry badges |
| **02. 2D Linear Basis Mapping** | <img src="assets/gallery/02_matrix_transformation.png" width="320"/> | 3B1B Math | Dynamic affine grid deformation, eigenvector highlights, and determinant telemetry |
| **03. Formula Derivation** | <img src="assets/gallery/03_formula_derivation.png" width="320"/> | Analytic | Step-by-step mathematical deduction pipeline with LaTeX rendering & justification |
| **04. PlotNeuralNet 3D Topology** | <img src="assets/gallery/04_plotneuralnet_3d.png" width="320"/> | Deep Learning | Isometric multi-channel tensor blocks, feature maps, and cross-layer receptive cones |
| **05. Attention Heatmap** | <img src="assets/gallery/05_attention_heatmap.png" width="320"/> | Attention | Interactive token query-key pairwise softmax matrix with dynamic connection arcs |
| **06. Vector Field Streamlines** | <img src="assets/gallery/06_pyvista_streamlines.png" width="320"/> | Scientific 3D | 3D continuous vector field with colormap-coded magnitude streamlines & grid box |
| **07. Non-Convex Optimization** | <img src="assets/gallery/07_optimization_contours.png" width="320"/> | Optimization | Multi-path contour convergence comparing SGD, Momentum, and Adam trajectories |
| **08. Confidence Band Plot** | <img src="assets/gallery/08_confidence_band.png" width="320"/> | SciencePlots | Academic-grade convergence curves with empirical 95% confidence variance bands |
| **09. Multi-Metric Radar** | <img src="assets/gallery/09_radar_chart.png" width="320"/> | Benchmarking | Orthogonal N-dimensional evaluation radar normalized against baseline targets |
| **10. Dual Code & Memory Inspector** | <img src="assets/gallery/10_dual_code_inspector.png" width="320"/> | Code Telemetry | Synchronized syntax-highlighted source execution pointer & live heap symbol table |
| **11. Cyber-Academic Dashboard** | <img src="assets/gallery/11_cyber_dashboard.png" width="320"/> | Multi-Pane | Split-screen analytical dashboard combining 3D manifolds, deduction notes & telemetry |
| **12. Triptych Pipeline Architecture** | <img src="assets/gallery/12_triptych_pipeline.png" width="320"/> | System Topology | 3-stage modular pipeline layout connected via synchronous high-speed data buses |

*Explore the full parameter references and code examples in [GALLERY.md](GALLERY.md).*

---

## ⚡ Quick Start

### Installation

Clone and install in editable mode:

```bash
git clone https://github.com/TardisBooo/scientific-visual-studio.git
cd scientific-visual-studio
pip install -e .
```

### Python API Example

```python
from scientific_visual_studio import (
    render_loss_landscape_3d,
    render_cyber_academic_dashboard_layout,
    render_multi_metric_radar
)

# 1. Render an isometric 3D loss surface
loss_surface = render_loss_landscape_3d(
    title="NON-CONVEX OBJECTIVE MANIFOLD",
    subtitle="Parametric Loss Surface with Saddle-Point Trajectories",
    contour_levels=14
)

# 2. Embed into a cyber-academic dashboard
dashboard_html = render_cyber_academic_dashboard_layout(
    scene_kicker="TELEMETRY // OPTIMIZATION RUNTIME",
    scene_title="Hamiltonian Energy Landscape Evolution",
    status_badge="STATUS: STABLE // 1000Hz",
    main_component_html=loss_surface,
    side_panel_html="""
    <div style="color: #94A3B8; font-size: 13px; line-height: 1.6;">
        <h4 style="color: #38BDF8;">Analytic Observation</h4>
        <p>Hessian spectrum indicates positive-definite curvature along principal manifold.</p>
    </div>
    """,
    bottom_telemetry_html="<span>EIGENVALUE: λ1 = 2.45</span><span>CONDITION: κ = 1.18</span>"
)

# Save to an HTML file or pass directly to Remotion/Slide Deck
with open("dashboard_preview.html", "w", encoding="utf-8") as f:
    f.write(dashboard_html)
```

---

## 🤖 AI Agent Integration

This repository is packaged with an **Agent Skill** (`skills/visual-storyboard-designer/SKILL.md`) compatible with **Antigravity**, **Claude Code**, and **Cursor**.

### When to use
Whenever an LLM agent designs educational lessons, presentation slides, or algorithmic videos, it invokes this skill to map conceptual ideas to verified scientific visual components instead of generating generic bullet lists.

```markdown
<!-- Antigravity / Agent Invocation -->
"Design an educational slide on Transformer Multi-Head Attention using scientific-visual-studio."
```

The agent will automatically select:
- Component: `render_observable_attention_heatmap`
- Layout: `render_top_formula_bottom_dynamic_layout`
- Accent palette: Cyber-academic Cyan & Deep Indigo

---

## 📁 Repository Structure

```
scientific-visual-studio/
├── scientific_visual_studio/          # Core Python library
│   ├── __init__.py                    # Package exports
│   ├── visual_studio.py               # Core components & layout renderers
│   └── visual_studio_extensions.py    # SciencePlots & specialized math engines
├── skills/                            # Autonomous Agent Skills
│   └── visual-storyboard-designer/    # SKILL.md specification
├── assets/
│   └── gallery/                       # Pre-rendered PNG & HTML visual showcases
├── generate_gallery_assets.py         # Automated headless Playwright renderer
├── pyproject.toml                     # Modern package metadata
├── setup.py                           # Setup script
├── GALLERY.md                         # Detailed component & props documentation
├── CONTRIBUTING.md                    # Contribution guidelines
└── LICENSE                            # Apache 2.0 License
```

---

## 🤝 Contributing

Contributions are welcome! If you'd like to add new scientific visualization components (such as quantum circuit diagrams, graph neural networks, or Voronoi partitioning), please check out our [CONTRIBUTING.md](CONTRIBUTING.md).

---

## 📄 License

Licensed under the [Apache 2.0 License](LICENSE).
