---
name: visual-storyboard-designer
description: Semantic visual storyboard designer and abstract component library. Map slide/lesson intents into SciencePlots academic charts, 3B1B mathematical animations, Teachable Figures intuition models, PlotNeuralNet 3D tensor volumes, PyVista vector streamlines, or system architecture layouts with zero business hardcoding.
---

# Visual Storyboard Designer Skill

Use this skill when designing technical presentations, educational videos, or academic slide decks. It provides a formal system for mapping educational semantics into **abstract visual primitives** and **diverse layout templates**, completely decoupled from specific course domains.

## 1. Visual Intent Classification Matrix

When authoring a slide/scene, first classify its pedagogical intent:

| Intent Category | Cognitive Goal | Recommended Layout | Recommended Abstract Component |
| :--- | :--- | :--- | :--- |
| `INTENT_COVER` | High-impact cinematic entrance | `HeroPanoramicLayout` | `render_premium_hero_cover` |
| `INTENT_INTUITION` | Physical metaphor & real-world mapping | `SplitCardVisualLayout` | `render_teachable_reservoir_valve` / `SpringDamper` |
| `INTENT_AXIOM_MATH` | Mathematical deduction & geometric truth | `TopFormulaBottomDynamicLayout` | `render_matrix_transformation_2d` / `render_latex_formula_derivation_pipeline` |
| `INTENT_TENSOR_ARCH` | 3D Deep Learning & Transformer weights | `CyberAcademicDashboardLayout` | `render_plotneuralnet_3d_pipeline` / `render_observable_attention_heatmap` |
| `INTENT_3D_SPATIAL` | Multi-dim physics & robotic kinematics | `CyberAcademicDashboardLayout` | `render_pyvista_streamlines_vector_field` / `render_viser_robotics_kinematic_chain` |
| `INTENT_OPTIMIZE` | Non-convex loss landscape & optimizer | `CyberAcademicDashboardLayout` | `render_loss_landscape_3d` / `render_optimization_contour_paths` |
| `INTENT_ARCHITECTURE` | Internal system wiring & dataflow | `render_triptych_pipeline_layout` | `PipelinedDataflowStream` / `DAGGraph` |
| `INTENT_CODE_RUNTIME` | Implementation vs memory state | `DualInspectionLayout` | `render_dual_code_inspector` |
| `INTENT_BENCHMARK` | Empirical proof, convergence & ablation | `render_quad_comparison_layout` | `render_convergence_band_plot` / `render_multi_metric_radar` |

---

## 2. Abstract Component Registry & Prop Schemas

Every visual component is purely data-driven, accepting structured JSON props.

### 2.1 Mathematical & Linear Algebra Animation (`Manim` / `JAnim` / `Motion Canvas`)
- **`render_matrix_transformation_2d`**:
  - Purpose: 2D coordinate grid deformation under $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$, showing transformed basis vectors $T(\hat{i}), T(\hat{j})$, determinant area scaling patch, and orientation indicator.
  - Props: `{ matrix: [[float, float], [float, float]], basis_labels: (str, str), title: str, subtitle: str }`
- **`render_latex_formula_derivation_pipeline`**:
  - Purpose: Multi-stage formula derivation sequence (TransformMatchingTex style) with active step highlight, modified term callouts, and mathematical notes.
  - Props: `{ steps: [{ num: int, math: str, badge: str, note: str }], active_step: int, title: str }`

### 2.2 Neural Network & Tensor Architecture (`PlotNeuralNet` / `ManimML` / `Observable Plot`)
- **`render_plotneuralnet_3d_pipeline`**:
  - Purpose: 3D isometric stacked cuboid tensor volumes representing Conv3D/Attention/Dense layers, with dimension tags $[B, C, H, W]$ and connective receptive field projection cones.
  - Props: `{ layers: [{ name: str, dim: str, w: int, h: int, d: int, color: str }], title: str, subtitle: str }`
- **`render_observable_attention_heatmap`**:
  - Purpose: Observable Plot / D3-style attention weight matrix heatmap with token labels, numerical values, focus crosshairs, and color gradient.
  - Props: `{ tokens_q: str[], tokens_k: str[], weights: float[][], focus_idx: int, title: str }`

### 2.3 3D Spatial & Scientific Simulation (`PyVista` / `Viser` / `Three.js`)
- **`render_pyvista_streamlines_vector_field`**:
  - Purpose: 3D continuous velocity field streamlines inside an isometric bounding box, with scientific colormap and colorbar.
  - Props: `{ title: str, subtitle: str, width: int, height: int }`
- **`render_loss_landscape_3d`**:
  - Purpose: 3D parametric optimization surface with contour level rings, gradient descent ball trajectory, and saddle points.
  - Props: `{ title: str, subtitle: str, width: int, height: int }`

### 2.4 General Scientific Computing & Optimization (`Plotly` / `Matplotlib + Celluloid`)
- **`render_optimization_contour_paths`**:
  - Purpose: 2D non-convex contour map comparing optimizer convergence paths (e.g. SGD vs Momentum vs Adam) converging to global minimum $\theta^*$.
  - Props: `{ title: str, subtitle: str, width: int, height: int }`
- **`render_convergence_band_plot`**:
  - Purpose: Empirical multi-agent/model training curves with shaded 95% confidence variance bands.
  - Props: `{ title: str, subtitle: str, x_label: str, y_label: str, series: [...] }`
- **`render_multi_metric_radar`**:
  - Purpose: $K$-dimensional orthogonal radar chart comparing architectures across Accuracy, Latency, Memory, Throughput, and Robustness.
  - Props: `{ title: str, axes: str[], datasets: [...] }`

---

## 3. Cyber-Academic HUD Layout System (Slide & Video Aesthetics)

To achieve dense, high-end, compact, and flexible presentation slides outside the cover:
1. **`render_scientific_terminal_card`**:
   - High-tech terminal card with precision corner crosshairs `+`, micro-tick coordinate rulers, status indicator, and streaming telemetry dictionary.
2. **`render_cyber_academic_dashboard_layout`**:
   - Asymmetric layout (68% main interactive visual + 32% side deduction/parameter panel + bottom monospace telemetry band).
3. **`render_triptych_pipeline_layout`**:
   - 3-column compact architecture flow with glowing synchronous data bus.
4. **`render_top_formula_bottom_dynamic_layout`**:
   - Top formal analytic equation card + bottom dynamic manifold.
5. **`render_quad_comparison_layout`**:
   - 2x2 multi-dimensional experimental ablation grid.
