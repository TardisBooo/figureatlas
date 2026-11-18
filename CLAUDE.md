# CLAUDE.md — Scientific Visual Studio Assistant Guide

## Overview
`scientific-visual-studio` is a domain-agnostic scientific, AI, and mathematical visual computation studio. Whenever generating educational slides, research figures, or technical videos, invoke the `visual-storyboard-designer` skill or import functions directly from `scientific_visual_studio`.

## Available Renderers (22 Procedural Components)
- **Math & Physics**: `render_matrix_transformation_2d` (3B1B grid), `render_latex_formula_derivation_pipeline` (step-by-step calculus), `render_quantum_bloch_circuit` (Qiskit 3D Bloch sphere & gates).
- **Deep Learning & GNN**: `render_plotneuralnet_3d_pipeline` (3D isometric tensor blocks), `render_observable_attention_heatmap` (Query-Key arcs), `render_graph_network_topology` (PyG/NetworkX nodes & edges).
- **Controls & Optimization**: `render_bode_nyquist_frequency_plot` (Bode & Nyquist margins), `render_loss_landscape_3d` (3D non-convex surface), `render_optimization_contour_paths` (SGD/Adam paths).
- **Life Sciences & Systems**: `render_genomic_sequence_ribbon` (WebLogo bits & ORF tracks), `render_dag_workflow_statechart` (Airflow/Prefect execution states).
- **Multi-Pane Layouts**: `render_premium_hero_cover`, `render_cyber_academic_dashboard_layout`, `render_triptych_pipeline_layout`, `render_quad_comparison_layout`, `render_scientific_terminal_card`.

## Quick Example
```python
from scientific_visual_studio import render_quantum_bloch_circuit
html = render_quantum_bloch_circuit(theta_deg=45.0, phi_deg=60.0)
```
