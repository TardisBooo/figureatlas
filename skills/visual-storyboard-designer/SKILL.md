---
name: visual-storyboard-designer
description: Semantic visual storyboard designer and abstract component library. Map slide/lesson intents into SciencePlots academic charts, 3B1B mathematical animations, Qiskit quantum circuits, Control Bode/Nyquist curves, PlotNeuralNet 3D tensor volumes, PyVista vector streamlines, or system architecture layouts with zero business hardcoding.
---

# Visual Storyboard Designer Skill 🧪✨

Use this skill when designing technical presentations, educational videos, or academic slide decks. It provides a formal system for mapping educational semantics into **abstract visual primitives** and **diverse layout templates**, completely decoupled from specific course domains.

## 1. Visual Intent Classification Matrix

When authoring a slide/scene, first classify its pedagogical intent:

| Intent Category | Cognitive Goal | Recommended Layout | Recommended Abstract Component |
| :--- | :--- | :--- | :--- |
| `INTENT_COVER` | High-impact cinematic entrance | `HeroPanoramicLayout` | `render_premium_hero_cover` |
| `INTENT_INTUITION` | Physical metaphor & real-world mapping | `SplitCardVisualLayout` | `render_teachable_reservoir_valve` |
| `INTENT_AXIOM_MATH` | Mathematical deduction & geometric truth | `TopFormulaBottomDynamicLayout` | `render_matrix_transformation_2d` / `render_latex_formula_derivation_pipeline` |
| `INTENT_QUANTUM` | Qubit state rotation & gate operations | `CyberAcademicDashboardLayout` | `render_quantum_bloch_circuit` |
| `INTENT_TENSOR_ARCH` | 3D Deep Learning & Transformer weights | `CyberAcademicDashboardLayout` | `render_plotneuralnet_3d_pipeline` / `render_observable_attention_heatmap` |
| `INTENT_GRAPH_TOPO` | Heterogeneous GNN message passing | `CyberAcademicDashboardLayout` | `render_graph_network_topology` |
| `INTENT_CONTROL_FREQ` | Frequency response & asymptotic stability | `CyberAcademicDashboardLayout` | `render_bode_nyquist_frequency_plot` |
| `INTENT_GENOMICS` | Information entropy & open reading frames | `TopFormulaBottomDynamicLayout` | `render_genomic_sequence_ribbon` |
| `INTENT_3D_SPATIAL` | Multi-dim physics & robotic kinematics | `CyberAcademicDashboardLayout` | `render_pyvista_streamlines_vector_field` |
| `INTENT_OPTIMIZE` | Non-convex loss landscape & optimizer | `CyberAcademicDashboardLayout` | `render_loss_landscape_3d` / `render_optimization_contour_paths` |
| `INTENT_ARCHITECTURE` | Internal system wiring & dataflow | `render_triptych_pipeline_layout` | `render_dag_workflow_statechart` |
| `INTENT_CHEMISTRY` | Molecular skeletal reaction & catalysis | `TopFormulaBottomDynamicLayout` | `render_molecule_reaction_scheme` |
| `INTENT_CELESTIAL` | CR3BP rotating frame & orbital balance | `CyberAcademicDashboardLayout` | `render_synodic_lagrange_orbit` |
| `INTENT_RF_MICROWAVE` | Transmission line impedance & eye mask | `CyberAcademicDashboardLayout` | `render_smith_eye_pair` |
| `INTENT_PARTICLE_PHYSICS` | Perturbative quantum field interactions | `TopFormulaBottomDynamicLayout` | `render_feynman_diagram_interaction` |
| `INTENT_CODE_RUNTIME` | Implementation vs memory state | `DualInspectionLayout` | `render_dual_code_inspector` |
| `INTENT_BENCHMARK` | Empirical proof, convergence & ablation | `render_quad_comparison_layout` | `render_convergence_band_plot` / `render_multi_metric_radar` |

---

## 2. Abstract Component Registry & Prop Schemas

Every visual component is purely data-driven, accepting structured JSON props.

### 2.1 Mathematical & Linear Algebra Animation (`Manim` / `3B1B`)
- **`render_matrix_transformation_2d`**: Coordinate grid deformation under affine matrix $A$, basis vectors $T(\hat{i}), T(\hat{j})$, determinant scaling patch.
- **`render_latex_formula_derivation_pipeline`**: Multi-stage formula derivation sequence with active step highlight and theorem notes.

### 2.2 Quantum Computing & Physics (`Qiskit` / `QuTiP`)
- **`render_quantum_bloch_circuit`**: Isometric 3D Bloch sphere ($|0\rangle, |1\rangle, |\psi\rangle$) paired with styled multi-qubit quantum gate wire (H, X, CNOT, Phase, Measure).

### 2.3 Deep Learning & Graph Networks (`PlotNeuralNet` / `PyG` / `Observable`)
- **`render_plotneuralnet_3d_pipeline`**: 3D isometric stacked cuboid tensor volumes $[B, C, H, W]$ and receptive field projection cones.
- **`render_observable_attention_heatmap`**: Query-Key pairwise softmax matrix with dynamic interaction arcs.
- **`render_graph_network_topology`**: Force-directed heterogeneous graph node-edge topology with radiant hub nodes.

### 2.4 Control Systems & Optimization (`Control` / `SciencePlots`)
- **`render_bode_nyquist_frequency_plot`**: Dual Bode gain/phase curves paired with complex s-plane Nyquist contour encircling $(-1, 0)$.
- **`render_loss_landscape_3d`**: 3D non-convex parameter manifold with saddle points and momentum ball trajectory.
- **`render_optimization_contour_paths`**: 2D contour paths comparing SGD vs Momentum vs Adam.
- **`render_convergence_band_plot`**: 95% confidence variance bands across independent runs.
- **`render_multi_metric_radar`**: Orthogonal N-dimensional evaluation radar normalized against baselines.

### 2.5 Bioinformatics & Workflow Orchestration (`WebLogo` / `Biopython` / `Airflow`)
- **`render_genomic_sequence_ribbon`**: Information-entropy sequence logo (bits) paired with annotated linear open reading frame tracks.
- **`render_dag_workflow_statechart`**: Distributed DAG pipeline with lifecycle states (`queued`, `running`, `success`, `failed`).

### 2.6 Chemistry, Celestial Mechanics, Microwave & High-Energy Physics (`RDKit` / `Astropy` / `scikit-rf` / `TikZ-Feynman`)
- **`render_molecule_reaction_scheme`**: 2D Kekule 30°/90° skeletal formulas, wedge/dash stereochemistry, CPK atom colors, reaction conditions & yield.
- **`render_synodic_lagrange_orbit`**: Circular Restricted Three-Body Problem (CR3BP) synodic rotating frame, L1–L5 Lagrange equilibrium points & Lyapunov halo orbit.
- **`render_smith_eye_pair`**: scikit-rf Smith chart with constant resistance/reactance circles & reflection coefficient paired with 2-UI eye diagram mask.
- **`render_feynman_diagram_interaction`**: TikZ-Feynman QED s-channel fermion lines, virtual photon transverse sinusoidal propagator wave & interaction vertices.

### 2.7 Multi-Pane Cyber-Academic Layout Engines
- **`render_premium_hero_cover`**: Cinematic widescreen title cover with glowing gradients and module badges.
- **`render_cyber_academic_dashboard_layout`**: Split analytical dashboard (3D/dynamic visual + deduction card + telemetry bus).
- **`render_triptych_pipeline_layout`**: 3-stage modular pipeline layout.
- **`render_quad_comparison_layout`**: 2x2 ablation/benchmark quad matrix.
- **`render_scientific_terminal_card`**: Sci-fi telemetry card container.
