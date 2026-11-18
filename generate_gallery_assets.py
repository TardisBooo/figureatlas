# -*- coding: utf-8 -*-
"""
Gallery Asset Generator for Scientific Visual Studio:
Renders standalone HTML for each visual component and captures high-res PNG screenshots.
"""

import os
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

# Add package to path
PKG_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(PKG_DIR))

import visual_studio as vs

OUTPUT_DIR = PKG_DIR / "assets" / "gallery"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

HTML_WRAPPER = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
    background: #060911;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    padding: 20px;
    font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', sans-serif;
}}
</style>
</head>
<body>
{content}
</body>
</html>
"""

def generate_assets():
    components = {
        "01_hero_cover.html": vs.render_premium_hero_cover(
            title="SCIENTIFIC VISUAL COMPUTATION STUDIO",
            subtitle="Domain-Agnostic Parametric Geometry, Manifolds, and Visual Primitives for Research Deck & Videos",
            eyebrow_badge="✦ OPEN SOURCE SCIENTIFIC VISUAL ENGINE",
            module_tag="// SPEC: V1.0.0-RELEASE",
            feature_chips=[
                "✦ Manim Geometric Transformation",
                "✦ PlotNeuralNet 3D Tensor Volumes",
                "✦ PyVista Continuous Vector Fields",
                "✦ SciencePlots Empirical Bands",
                "✦ Observable Attention Heatmaps"
            ]
        ),
        "02_matrix_transformation.html": vs.render_matrix_transformation_2d(
            matrix=[[1.6, 0.4], [0.3, 1.3]],
            basis_labels=("î", "ĵ"),
            title="2D AFFINE BASIS MAPPING & EIGENSPACE",
            subtitle="Cartesian Grid Deformation under Linear Matrix Operator A"
        ),
        "03_formula_derivation.html": vs.render_latex_formula_derivation_pipeline(
            steps=[
                {"num": 1, "math": "J = \\frac{1}{2N} \\sum_{i=1}^N \\|y_i - f(x_i; \\theta)\\|^2 + \\lambda \\Omega(\\theta)", "badge": "Regulated Objective", "note": "Mean squared empirical risk regularized by Sobolev penalty norm."},
                {"num": 2, "math": "\\nabla_\\theta J = -\\frac{1}{N} X^T (y - X\\theta) + 2\\lambda \\theta", "badge": "Analytic Gradient", "note": "Closed-form first-order derivative indicating steep descent direction."},
                {"num": 3, "math": "\\theta^* = (X^T X + 2N\\lambda I)^{-1} X^T y", "badge": "Closed-Form Solution", "note": "Ridge-regularized optimal parameter vector bypassing numerical drift."}
            ],
            active_step=2,
            title="STEPWISE MATHEMATICAL DEDUCTION",
            subtitle="TransformMatchingTex Symbolic Equation Pipeline"
        ),
        "04_plotneuralnet_3d.html": vs.render_plotneuralnet_3d_pipeline(
            layers=[
                {"name": "Input Tensor", "dim": "3×256×256", "w": 32, "h": 150, "d": 150, "color": "#38BDF8"},
                {"name": "Conv3D-Stem", "dim": "64×128×128", "w": 48, "h": 120, "d": 120, "color": "#6366F1"},
                {"name": "Transformer Block", "dim": "192×64×64", "w": 72, "h": 85, "d": 85, "color": "#8B5CF6"},
                {"name": "Cross-Attention", "dim": "384×32×32", "w": 96, "h": 60, "d": 60, "color": "#EC4899"},
                {"name": "Latent Manifold", "dim": "512×1×1", "w": 20, "h": 36, "d": 36, "color": "#10B981"}
            ],
            title="3D ISOMETRIC NEURAL TENSOR STACK",
            subtitle="Multi-Layer Volumetric Feature Representations & Receptive Cones"
        ),
        "05_attention_heatmap.html": vs.render_observable_attention_heatmap(
            tokens_q=["Query-1", "Encoder", "Key-Rel", "Attention", "Weight", "Output"],
            tokens_k=["Query-1", "Encoder", "Key-Rel", "Attention", "Weight", "Output"],
            weights=[
                [0.55, 0.10, 0.08, 0.12, 0.08, 0.07],
                [0.08, 0.62, 0.15, 0.06, 0.05, 0.04],
                [0.05, 0.18, 0.54, 0.11, 0.08, 0.04],
                [0.09, 0.07, 0.16, 0.48, 0.14, 0.06],
                [0.04, 0.05, 0.08, 0.19, 0.58, 0.06],
                [0.06, 0.06, 0.05, 0.08, 0.11, 0.64]
            ],
            focus_idx=3,
            title="INTERACTIVE MULTI-HEAD ATTENTION HEATMAP",
            subtitle="Pairwise Softmax Distribution Matrix with Focused Crosshair"
        ),
        "06_pyvista_streamlines.html": vs.render_pyvista_streamlines_vector_field(
            title="3D PHYSICAL FIELD STREAMLINES & GRADIENT",
            subtitle="Continuous Vector Field Flow within Isometric Bounding Grid"
        ),
        "07_optimization_contours.html": vs.render_optimization_contour_paths(
            title="NON-CONVEX CONTOUR OPTIMIZATION",
            subtitle="Comparative Gradient Trajectories: SGD vs Momentum vs Adam"
        ),
        "08_confidence_band.html": vs.render_convergence_band_plot(
            title="EMPIRICAL CONVERGENCE & CONFIDENCE BANDS",
            subtitle="Monte Carlo Empirical Variance Bands Across 100 Independent Runs"
        ),
        "09_radar_chart.html": vs.render_multi_metric_radar(
            title="ORTHOGONAL SYSTEM PERFORMANCE RADAR",
            axes=["Accuracy", "Throughput", "Latency", "Robustness", "Efficiency"]
        ),
        "10_dual_code_inspector.html": vs.render_dual_code_inspector(
            code_snippet='def solve_equilibrium(state, external_force):\n    """Compute adaptive damping torque."""\n    accel = (external_force - state.pos * 9.8) / state.mass\n    torque = Kp * state.error - Kd * state.vel\n    return torque',
            memory_slots=[
                {"name": "state.pos", "val": "1.047 rad", "type": "float64"},
                {"name": "state.vel", "val": "0.002 rad/s", "type": "float64"},
                {"name": "torque_cmd", "val": "13.25 N*m", "type": "float64"},
                {"name": "status", "val": "CONVERGED", "type": "enum"}
            ],
            title="DUAL CODE & RUNTIME MEMORY INSPECTOR",
            active_line=4
        ),
        "11_cyber_dashboard.html": vs.render_cyber_academic_dashboard_layout(
            scene_kicker="TELEMETRY // COMPUTATIONAL DASHBOARD",
            scene_title="Nonlinear Dynamic System Stability Monitor",
            status_badge="STABILITY: ASYMPTOTIC // 500Hz",
            main_component_html=vs.render_loss_landscape_3d("PARAMETRIC LOSS SURFACE", "Non-Convex Gradient Field"),
            side_panel_html="""
            <div style="background: rgba(15,23,42,0.85); border: 1px solid rgba(56,189,248,0.25); border-radius: 8px; padding: 18px; height: 100%; box-sizing: border-box; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <div style="font-family: monospace; font-size: 11px; color: #38BDF8; font-weight: 700; margin-bottom: 6px;">[ANALYTIC DEDUCTION]</div>
                    <div style="font-size: 18px; font-weight: 800; color: #FFFFFF; margin-bottom: 10px;">Eigen-Decomposition</div>
                    <p style="font-size: 13px; color: #94A3B8; line-height: 1.6;">
                        All roots of the characteristic polynomial lie strictly in the negative open half-plane Re(λ) &lt; 0.
                    </p>
                </div>
                <div style="background: rgba(0,0,0,0.4); border: 1px solid rgba(255,255,255,0.06); border-radius: 6px; padding: 10px; font-family: monospace; font-size: 11px; color: #10B981;">
                    ✓ LYAPUNOV CRITERIA SATISFIED
                </div>
            </div>
            """,
            bottom_telemetry_html="<span>BUS FREQ: 500Hz</span><span>PHASE MARGIN: 48.2°</span><span>PACKET LOSS: 0.00%</span>"
        ),
        "12_triptych_pipeline.html": vs.render_triptych_pipeline_layout(
            scene_kicker="ARCHITECTURE // PIPELINE TOPOLOGY",
            scene_title="Sense-Plan-Act Synchronous Computing Architecture",
            stages=[
                {"num": "STAGE 01", "name": "Sensory Acquisition", "tag": "MULTIMODAL ENCODER", "desc": "Sub-millimeter optical joint encoders and 6-axis force-torque sensor array.", "metrics": {"RATE": "500Hz", "PRECISION": "0.01mm"}, "color": "#38BDF8"},
                {"num": "STAGE 02", "name": "Trajectory Planning", "tag": "QP-MPC SOLVER", "desc": "Realtime convex quadratic program trajectory optimization with collision corridors.", "metrics": {"HORIZON": "50 STEPS", "LATENCY": "12ms"}, "color": "#6366F1"},
                {"num": "STAGE 03", "name": "Torque Servo Loop", "tag": "IMPEDANCE CONTROL", "desc": "Hard-realtime joint motor current controller executing compliance reflexes.", "metrics": {"LOOP": "1000Hz", "BANDWIDTH": "1200 rad/s"}, "color": "#10B981"}
            ],
            interconnect_label="SYNCHRONOUS DATA BUS // 500Hz"
        ),
        "13_loss_landscape_3d.html": vs.render_loss_landscape_3d(
            title="3D PARAMETRIC LOSS MANIFOLD",
            subtitle="Non-Convex Energy Surface with Saddle-Point Trajectories",
            contour_levels=14
        ),
        "14_teachable_reservoir_valve.html": vs.render_teachable_reservoir_valve(
            title="HYDRAULIC RESERVOIR & GATED THROTTLE",
            subtitle="Physical Intuition for Gradient Accumulation & Flow Dissipation",
            reservoir_level_pct=68,
            valve_aperture_pct=42
        ),
        "15_top_formula_bottom_dynamic.html": vs.render_top_formula_bottom_dynamic_layout(
            scene_kicker="AXIOM // EQUATIONS OF MOTION",
            scene_title="Lagrangian Mechanics Formulation",
            formula_latex=r"\frac{d}{dt}\left(\frac{\partial \mathcal{L}}{\partial \dot{q}_i}\right) - \frac{\partial \mathcal{L}}{\partial q_i} = \tau_i",
            formula_explanation="The Euler-Lagrange equations establish the fundamental connection between variational stationary action and robotic generalized coordinates.",
            dynamic_component_html=vs.render_matrix_transformation_2d(title="GENERALIZED COORDINATE MAPPING", subtitle="Tangent Space Basis Deformation")
        ),
        "16_quad_comparison_matrix.html": vs.render_quad_comparison_layout(
            scene_kicker="ABLATION // EMPIRICAL BENCHMARK",
            scene_title="Ablation Analysis Across System Architectures",
            quad_cards=[
                {"title": "Baseline Rigid", "badge": "CONFIG A", "desc": "Fixed-gain classical PID with rigid link assumption.", "stat_val": "24.2 ms", "stat_label": "TRACKING ERROR", "color": "#64748B"},
                {"title": "Admittance Hybrid", "badge": "CONFIG B", "desc": "Outer admittance loop with direct velocity feedforward.", "stat_val": "11.8 ms", "stat_label": "SETTLING TIME", "color": "#38BDF8"},
                {"title": "Impedance + MPC", "badge": "CONFIG C", "desc": "Convex quadratic programming with constraint corridor.", "stat_val": "4.1 ms", "stat_label": "SOLVER LATENCY", "color": "#6366F1"},
                {"title": "Full Sensorimotor VLA", "badge": "PROPOSED", "desc": "End-to-end vision-language-action cross-attention token policy.", "stat_val": "98.7%", "stat_label": "SUCCESS RATE", "color": "#10B981"}
            ]
        ),
        "17_scientific_terminal_card.html": vs.render_scientific_terminal_card(
            inner_content_html=vs.render_optimization_contour_paths(title="OPTIMIZER STEP DYNAMICS", subtitle="Realtime Gradient Descent Trace"),
            status_tag="SIMULATION: CONVERGED // 1000 FPS",
            telemetry={"SOLVER": "QP-ACTIVE-SET", "ITERATIONS": "42", "KKT_TOL": "1e-6", "EIGEN_MAX": "8.42"},
            title="TELEMETRY DEBUG TERMINAL"
        ),
        "18_quantum_bloch_circuit.html": vs.render_quantum_bloch_circuit(
            vector=(0.35, 0.61, 0.71),
            theta_deg=45.0,
            phi_deg=60.0,
            title="QUANTUM BLOCH SPHERE & CIRCUIT TELEMETRY",
            subtitle="Unitary State Vector Rotation & Multi-Qubit Gate Sequence"
        ),
        "19_bode_nyquist_frequency.html": vs.render_bode_nyquist_frequency_plot(
            title="BODE GAIN/PHASE & NYQUIST CONTOUR",
            subtitle="Frequency Domain Stability Margins Encircling (-1, 0)",
            gain_margin_db=14.2,
            phase_margin_deg=48.6
        ),
        "20_graph_network_topology.html": vs.render_graph_network_topology(
            title="GNN MESSAGE-PASSING TOPOLOGY",
            subtitle="Heterogeneous Graph Node Embeddings & Directed Attention Flow"
        ),
        "21_genomic_sequence_ribbon.html": vs.render_genomic_sequence_ribbon(
            title="GENOMIC SEQUENCE MOTIF & FEATURE TRACK",
            subtitle="WebLogo Information Bits Stack & Annotated Open Reading Frame Tracks"
        ),
        "22_dag_workflow_statechart.html": vs.render_dag_workflow_statechart(
            title="DISTRIBUTED WORKFLOW DAG PIPELINE",
            subtitle="Layered Task Lifecycle Execution States with Orthogonal Routing"
        ),
        "23_molecule_reaction.html": vs.render_molecule_reaction_scheme(
            title="RDKIT CHEMICAL REACTION & MOLECULAR TOPOLOGY",
            subtitle="2D Kekule Skeletal Bonds with Stereochemical Wedges and Reagent Catalysis"
        ),
        "24_synodic_lagrange_orbit.html": vs.render_synodic_lagrange_orbit(
            title="CR3BP SYNODIC ORBITS & LAGRANGE POINTS",
            subtitle="Rotating Frame with Jacobi Energy Contours, L1-L5 Points & Lyapunov Halo Orbit"
        ),
        "25_smith_eye_pair.html": vs.render_smith_eye_pair(
            title="MICROWAVE SMITH CHART & SERIAL EYE DIAGRAM",
            subtitle="Complex S11 Reflection Trajectory on Unit Circle with 2-UI Serial Eye Mask"
        ),
        "26_feynman_diagram.html": vs.render_feynman_diagram_interaction(
            title="QED FEYNMAN PARTICLE INTERACTION",
            subtitle="s-Channel Electron-Positron Annihilation via Virtual Gauge Boson Propagator"
        )
    }

    # Render HTML and capture screenshots with Playwright
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for filename, comp_html in components.items():
            base_name = filename.replace(".html", "")
            img_name = f"{base_name}.png"
            html_path = OUTPUT_DIR / filename
            img_path = OUTPUT_DIR / img_name

            full_html = HTML_WRAPPER.format(content=comp_html)
            html_path.write_text(full_html, encoding="utf-8")

            # Capture screenshot
            page = browser.new_page(viewport={"width": 1920, "height": 1080})
            page.set_content(full_html)
            page.wait_for_timeout(400)
            
            # Select target element or body
            el = page.query_selector(".scene-layout-container") or page.query_selector(".cover-hero-wrapper") or page.query_selector("body > div")
            if el:
                el.screenshot(path=str(img_path))
            else:
                page.screenshot(path=str(img_path))
            page.close()
            print(f"Rendered: {img_name}")

        browser.close()

    print("All gallery assets generated successfully!")

if __name__ == "__main__":
    generate_assets()
