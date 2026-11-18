# -*- coding: utf-8 -*-
"""
Scientific Visual Studio Extensions:
Pillars of Open-Source Scientific Visualization:
- Manim / JAnim / Motion Canvas: Linear Algebra Matrix Transformations & Formula Derivations
- PlotNeuralNet / ManimML / Netron / Observable Plot: 3D Isometric Tensor Volumes, Attention Heatmaps, Computation DAGs
- PyVista / Viser / Three.js: 3D Vector Field Streamlines & Articulated Kinematic Robot SE(3) Chains
- Plotly / Celluloid: Multi-Algorithm Contour Optimization Paths & Scatter Matrix
- Cyber-Academic HUD Layout System: High-Density Scientific Dashboard & Triptych Pipeline
"""

import math
import html


# ==============================================================================
# 8. MATHEMATICAL & LINEAR ALGEBRA ANIMATION (Manim / JAnim / Motion Canvas)
# ==============================================================================
def render_matrix_transformation_2d(
    matrix: list[list[float]] = None,
    basis_labels: tuple[str, str] = ("î", "ĵ"),
    transformed_vectors: list[dict] = None,
    title: str = "LINEAR TRANSFORMATION & BASIS MAPPING",
    subtitle: str = "R² Grid Deformation under Affine Matrix Operator A",
    width: int = 860,
    height: int = 520,
) -> str:
    """
    Renders a 2D coordinate grid transformed by a 2x2 matrix A = [[a, b], [c, d]].
    Shows:
      - Original Cartesian grid (dimmed dashed gray lines)
      - Transformed coordinate grid (warped colored lines)
      - Unit basis vectors i_hat, j_hat mapped to T(i_hat), T(j_hat)
      - Determinant area patch (shaded quad indicating area scaling factor det(A))
      - Side-by-side numerical matrix telemetry panel
    """
    if matrix is None:
        matrix = [[1.4, 0.6], [0.4, 1.2]]

    a, b = matrix[0]
    c, d = matrix[1]
    det = a * d - b * c

    # Grid parameters
    cx, cy = 340, 260
    scale = 65  # pixels per unit coordinate
    grid_range = 3

    # Generate original and transformed grid lines
    orig_lines = []
    trans_lines = []
    for g in range(-grid_range, grid_range + 1):
        if g == 0:
            continue
        # Horizontal lines y = g
        x_min, x_max = -grid_range, grid_range
        # Original
        orig_lines.append(
            f'<line x1="{cx + x_min*scale}" y1="{cy - g*scale}" x2="{cx + x_max*scale}" y2="{cy - g*scale}" stroke="#334155" stroke-dasharray="3,3" stroke-width="1" opacity="0.45"/>'
        )
        orig_lines.append(
            f'<line x1="{cx + g*scale}" y1="{cy - x_min*scale}" x2="{cx + g*scale}" y2="{cy - x_max*scale}" stroke="#334155" stroke-dasharray="3,3" stroke-width="1" opacity="0.45"/>'
        )

        # Transformed lines: for fixed y=g, x varies from -grid_range to grid_range
        # [tx, ty] = [a*x + b*g, c*x + d*g]
        tx1 = cx + (a * x_min + b * g) * scale
        ty1 = cy - (c * x_min + d * g) * scale
        tx2 = cx + (a * x_max + b * g) * scale
        ty2 = cy - (c * x_max + d * g) * scale
        trans_lines.append(
            f'<line x1="{tx1:.1f}" y1="{ty1:.1f}" x2="{tx2:.1f}" y2="{ty2:.1f}" stroke="rgba(56,189,248,0.3)" stroke-width="1.2"/>'
        )

        # Transformed lines for fixed x=g, y varies
        tx1_v = cx + (a * g + b * x_min) * scale
        ty1_v = cy - (c * g + d * x_min) * scale
        tx2_v = cx + (a * g + b * x_max) * scale
        ty2_v = cy - (c * g + d * x_max) * scale
        trans_lines.append(
            f'<line x1="{tx1_v:.1f}" y1="{ty1_v:.1f}" x2="{tx2_v:.1f}" y2="{ty2_v:.1f}" stroke="rgba(129,140,248,0.3)" stroke-width="1.2"/>'
        )

    # Shaded unit area transformed quad: vertices at (0,0), (a, c), (a+b, c+d), (b, d)
    p0 = (cx, cy)
    p1 = (cx + a * scale, cy - c * scale)
    p2 = (cx + (a + b) * scale, cy - (c + d) * scale)
    p3 = (cx + b * scale, cy - d * scale)
    area_polygon = f'<polygon points="{p0[0]},{p0[1]} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f} {p3[0]:.1f},{p3[1]:.1f}" fill="rgba(99,102,241,0.22)" stroke="#6366F1" stroke-width="1.5" stroke-dasharray="4,2"/>'

    # Transformed basis vectors T(i), T(j)
    t_i_x, t_i_y = p1
    t_j_x, t_j_y = p3

    vector_lines = f"""
    <!-- T(i_hat) -->
    <line x1="{cx}" y1="{cy}" x2="{t_i_x:.1f}" y2="{t_i_y:.1f}" stroke="#F43F5E" stroke-width="3" marker-end="url(#arrow-red)"/>
    <circle cx="{t_i_x:.1f}" cy="{t_i_y:.1f}" r="4" fill="#F43F5E"/>
    <text x="{t_i_x + 12:.1f}" y="{t_i_y + 4:.1f}" fill="#F43F5E" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700">T({basis_labels[0]}) = [{a:.1f}, {c:.1f}]ᵀ</text>

    <!-- T(j_hat) -->
    <line x1="{cx}" y1="{cy}" x2="{t_j_x:.1f}" y2="{t_j_y:.1f}" stroke="#10B981" stroke-width="3" marker-end="url(#arrow-green)"/>
    <circle cx="{t_j_x:.1f}" cy="{t_j_y:.1f}" r="4" fill="#10B981"/>
    <text x="{t_j_x + 12:.1f}" y="{t_j_y + 4:.1f}" fill="#10B981" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700">T({basis_labels[1]}) = [{b:.1f}, {d:.1f}]ᵀ</text>
    """

    return f"""
    <div style="background: #0A0E17; border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 20px 24px; width: {width}px; height: {height}px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: space-between; font-family: -apple-system, BlinkMacSystemFont, 'Inter', sans-serif;">
        <!-- Header -->
        <div style="display: flex; justify-content: space-between; align-items: flex-start; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 12px;">
            <div>
                <div style="font-size: 11px; font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #38BDF8; letter-spacing: 1px;">3B1B // LINEAR TRANSFORMATION</div>
                <div style="font-size: 16px; font-weight: 800; color: #F8FAFC; margin-top: 3px;">{html.escape(title)}</div>
                <div style="font-size: 12px; color: #64748B;">{html.escape(subtitle)}</div>
            </div>
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; background: rgba(56,189,248,0.1); border: 1px solid rgba(56,189,248,0.3); padding: 4px 10px; border-radius: 4px; color: #38BDF8;">
                det(A) = {det:.3f}
            </div>
        </div>

        <!-- Body Canvas & Side Telemetry -->
        <div style="display: flex; gap: 20px; align-items: center; flex: 1;">
            <!-- SVG Vector Canvas -->
            <div style="flex: 1; height: 380px; position: relative;">
                <svg width="100%" height="100%" viewBox="0 0 680 400" style="overflow: visible;">
                    <defs>
                        <marker id="arrow-red" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                            <path d="M 0 1 L 8 5 L 0 9 z" fill="#F43F5E"/>
                        </marker>
                        <marker id="arrow-green" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                            <path d="M 0 1 L 8 5 L 0 9 z" fill="#10B981"/>
                        </marker>
                    </defs>
                    <!-- Axes -->
                    <line x1="{cx - 300}" y1="{cy}" x2="{cx + 300}" y2="{cy}" stroke="#475569" stroke-width="1.5"/>
                    <line x1="{cx}" y1="{cy - 180}" x2="{cx}" y2="{cy + 180}" stroke="#475569" stroke-width="1.5"/>
                    <!-- Grids -->
                    {''.join(orig_lines)}
                    {''.join(trans_lines)}
                    <!-- Area & Basis -->
                    {area_polygon}
                    {vector_lines}
                    <!-- Origin -->
                    <circle cx="{cx}" cy="{cy}" r="4" fill="#94A3B8"/>
                </svg>
            </div>

            <!-- Mathematical Spec Box -->
            <div style="width: 220px; background: rgba(15,23,42,0.8); border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; padding: 14px; font-family: 'JetBrains Mono', monospace;">
                <div style="font-size: 10px; color: #64748B; border-bottom: 1px solid rgba(255,255,255,0.08); padding-bottom: 6px; margin-bottom: 10px;">OPERATOR MATRIX</div>
                <div style="display: flex; align-items: center; justify-content: center; gap: 8px; margin-bottom: 14px;">
                    <span style="color: #94A3B8; font-size: 14px;">A = </span>
                    <div style="border-left: 2px solid #38BDF8; border-right: 2px solid #38BDF8; padding: 3px 8px; font-size: 13px; line-height: 1.4; color: #F1F5F9;">
                        <div>{a:.2f}  {b:.2f}</div>
                        <div>{c:.2f}  {d:.2f}</div>
                    </div>
                </div>
                <div style="font-size: 11px; color: #94A3B8; line-height: 1.6; border-top: 1px solid rgba(255,255,255,0.06); padding-top: 10px;">
                    <div><span style="color: #64748B;">• Area Scale:</span> <b style="color: #F8FAFC;">{abs(det):.2f}x</b></div>
                    <div><span style="color: #64748B;">• Orientation:</span> <b style="color: {'#10B981' if det > 0 else '#F43F5E'};">{'Preserved' if det > 0 else 'Inverted'}</b></div>
                    <div><span style="color: #64748B;">• Invertible:</span> <b style="color: #38BDF8;">{'Yes (Rank 2)' if abs(det) > 1e-4 else 'Singular'}</b></div>
                </div>
            </div>
        </div>
    </div>
    """


def render_latex_formula_derivation_pipeline(
    steps: list[dict],
    active_step: int = 1,
    title: str = "FORMAL ANALYTIC DEDUCTION",
    subtitle: str = "Step-by-Step Transformative Mathematical Derivation",
    width: int = 860,
    height: int = 520,
) -> str:
    """
    Renders an interactive-style LaTeX formula derivation sequence (Manim TransformMatchingTex style).
    steps = [
        {"num": 1, "math": "\\tau = J^T(q) F_{ext} + M(q)\\ddot{q} + C(q,\\dot{q})\\dot{q}", "badge": "Lagrangian Dynamics", "note": "Full rigid-body dynamic equilibrium equation in joint space."},
        {"num": 2, "math": "M(q)\\ddot{q} = \\tau_{cmd} - g(q) - \\hat{f}_{ext}", "badge": "Gravity Compensation", "note": "Linearized feedback cancelation isolating inertial acceleration."},
        {"num": 3, "math": "\\ddot{e} + K_d \\dot{e} + K_p e = 0", "badge": "Lyapunov Stability", "note": "Second-order homogeneous error dynamics converging to origin."}
    ]
    """
    step_htmls = []
    for s in steps:
        is_active = (s["num"] == active_step)
        accent = "#38BDF8" if is_active else "#64748B"
        bg = "rgba(56,189,248,0.08)" if is_active else "rgba(15,23,42,0.4)"
        border = "rgba(56,189,248,0.4)" if is_active else "rgba(255,255,255,0.06)"

        step_htmls.append(f"""
        <div style="background: {bg}; border: 1.5px solid {border}; border-radius: 10px; padding: 14px 18px; margin-bottom: 12px; transition: all 0.2s;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span style="font-family: 'JetBrains Mono', monospace; font-size: 11px; font-weight: 800; background: {accent}; color: #080C14; padding: 2px 6px; border-radius: 4px;">STEP {s["num"]}</span>
                    <span style="font-size: 13px; font-weight: 700; color: {accent};">{html.escape(s.get("badge", ""))}</span>
                </div>
                {f'<span style="font-size: 10px; font-family: monospace; color: #38BDF8; font-weight: 700;">● ACTIVE FOCUS</span>' if is_active else ''}
            </div>
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 16px; font-weight: 700; color: #F8FAFC; background: rgba(0,0,0,0.3); padding: 8px 12px; border-radius: 6px; margin-bottom: 6px; letter-spacing: 0.5px;">
                {html.escape(s["math"])}
            </div>
            <div style="font-size: 12px; color: #94A3B8; line-height: 1.4;">
                {html.escape(s.get("note", ""))}
            </div>
        </div>
        """)

    return f"""
    <div style="background: #0A0E17; border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 20px 24px; width: {width}px; height: {height}px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: space-between; font-family: -apple-system, BlinkMacSystemFont, 'Inter', sans-serif;">
        <div style="border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 10px; margin-bottom: 14px;">
            <div style="font-size: 11px; font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #38BDF8; letter-spacing: 1px;">MANIM // TRANSFORM MATCHING TEX</div>
            <div style="font-size: 16px; font-weight: 800; color: #F8FAFC; margin-top: 2px;">{html.escape(title)}</div>
            <div style="font-size: 12px; color: #64748B;">{html.escape(subtitle)}</div>
        </div>
        <div style="flex: 1; overflow-y: auto;">
            {''.join(step_htmls)}
        </div>
    </div>
    """


# ==============================================================================
# 9. NEURAL NETWORK & TENSOR ARCHITECTURE (PlotNeuralNet, ManimML, Netron, Observable)
# ==============================================================================
def render_plotneuralnet_3d_pipeline(
    layers: list[dict] = None,
    title: str = "DEEP TENSOR TOPOLOGY & MULTI-LAYER PIPELINE",
    subtitle: str = "3D Isometric Feature Maps & Cross-Layer Receptive Cones",
    width: int = 860,
    height: int = 520,
) -> str:
    """
    Renders a PlotNeuralNet / LaTeX TikZ-style 3D isometric stacked neural network volume.
    Each layer has:
      - 3D cuboid projection with depth shading
      - Tensor dimension tag [B, C, H, W]
      - Connecting receptive field projection pyramid lines
      - Color coded by layer type (Conv, Pooling, Attention, Dense, Output)
    """
    if layers is None:
        layers = [
            {"name": "Input Image", "dim": "3×224×224", "w": 30, "h": 160, "d": 160, "color": "#38BDF8"},
            {"name": "Conv3D-1", "dim": "64×112×112", "w": 45, "h": 130, "d": 130, "color": "#6366F1"},
            {"name": "ResBlock-2", "dim": "128×56×56", "w": 65, "h": 95, "d": 95, "color": "#8B5CF6"},
            {"name": "Attn-Head", "dim": "256×28×28", "w": 85, "h": 65, "d": 65, "color": "#EC4899"},
            {"name": "Latent", "dim": "512×1×1", "w": 18, "h": 40, "d": 40, "color": "#10B981"},
        ]

    # Draw 3D isometric cuboids along an X-axis trajectory
    svg_elements = []
    start_x = 70
    gap = 145
    cy = 280

    for i, l in enumerate(layers):
        x = start_x + i * gap
        w, h, d = l["w"], l["h"], l["d"]
        col = l["color"]

        # Isometric offsets: dx = d * 0.45, dy = -d * 0.35
        iso_dx = d * 0.4
        iso_dy = -d * 0.3

        # Front Face: (x, cy - h/2) to (x + w, cy + h/2)
        x0, y0 = x, cy - h/2
        x1, y1 = x + w, cy + h/2

        # Connective receptive cone lines to next layer
        if i < len(layers) - 1:
            next_x = start_x + (i + 1) * gap
            next_h = layers[i + 1]["h"]
            cone_d = f"M {x1 + iso_dx:.1f} {y0 + iso_dy:.1f} L {next_x:.1f} {cy - next_h/2:.1f} L {next_x:.1f} {cy + next_h/2:.1f} L {x1:.1f} {y1:.1f} Z"
            svg_elements.append(
                f'<path d="{cone_d}" fill="{col}15" stroke="{col}" stroke-width="1" stroke-dasharray="2,2"/>'
            )

        # 3D Top Face
        top_pts = f"{x0},{y0} {x0 + iso_dx:.1f},{y0 + iso_dy:.1f} {x1 + iso_dx:.1f},{y0 + iso_dy:.1f} {x1},{y0}"
        svg_elements.append(
            f'<polygon points="{top_pts}" fill="{col}66" stroke="{col}" stroke-width="1.2"/>'
        )

        # 3D Right Side Face
        right_pts = f"{x1},{y0} {x1 + iso_dx:.1f},{y0 + iso_dy:.1f} {x1 + iso_dx:.1f},{y1 + iso_dy:.1f} {x1},{y1}"
        svg_elements.append(
            f'<polygon points="{right_pts}" fill="{col}44" stroke="{col}" stroke-width="1.2"/>'
        )

        # Front Face
        svg_elements.append(
            f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" fill="{col}88" stroke="{col}" stroke-width="1.5" rx="2"/>'
        )

        # Labels
        svg_elements.append(
            f'<text x="{x + w/2 + iso_dx/2:.1f}" y="{y0 + iso_dy - 12:.1f}" fill="{col}" font-family="\'JetBrains Mono\', monospace" font-size="11" font-weight="700" text-anchor="middle">{html.escape(l["name"])}</text>'
        )
        svg_elements.append(
            f'<text x="{x + w/2:.1f}" y="{cy + h/2 + 22:.1f}" fill="#94A3B8" font-family="\'JetBrains Mono\', monospace" font-size="10" text-anchor="middle">{html.escape(l["dim"])}</text>'
        )

    return f"""
    <div style="background: #0A0E17; border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 20px 24px; width: {width}px; height: {height}px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: space-between; font-family: -apple-system, BlinkMacSystemFont, 'Inter', sans-serif;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 10px;">
            <div>
                <div style="font-size: 11px; font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #8B5CF6; letter-spacing: 1px;">PLOTNEURALNET // 3D ISOMETRIC VOLUMES</div>
                <div style="font-size: 16px; font-weight: 800; color: #F8FAFC; margin-top: 2px;">{html.escape(title)}</div>
                <div style="font-size: 12px; color: #64748B;">{html.escape(subtitle)}</div>
            </div>
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 10px; background: rgba(139,92,246,0.15); border: 1px solid rgba(139,92,246,0.4); padding: 4px 8px; border-radius: 4px; color: #A78BFA;">
                TOTAL PARAMS: 24.6M // FLOPs: 4.8G
            </div>
        </div>
        <div style="flex: 1; position: relative;">
            <svg width="100%" height="100%" viewBox="0 0 800 380" style="overflow: visible;">
                {''.join(svg_elements)}
            </svg>
        </div>
    </div>
    """


def render_observable_attention_heatmap(
    tokens_q: list[str] = None,
    tokens_k: list[str] = None,
    weights: list[list[float]] = None,
    focus_idx: int = 1,
    title: str = "SELF-ATTENTION WEIGHT MATRIX INTERACTION",
    subtitle: str = "Query-Key Pairwise Dot Product Softmax Distribution",
    width: int = 860,
    height: int = 520,
) -> str:
    """
    Renders an Observable Plot / D3-style attention weight heatmap.
    Shows:
      - 2D grid cells colored by attention intensity
      - Query & Key token labels along axes
      - Interactive crosshair target highlighting attention from query token to all keys
      - Colorbar with precise decimal values
    """
    if tokens_q is None:
        tokens_q = ["[CLS]", "robot", "arm", "grasp", "target", "smooth"]
    if tokens_k is None:
        tokens_k = ["[CLS]", "robot", "arm", "grasp", "target", "smooth"]
    if weights is None:
        weights = [
            [0.45, 0.12, 0.08, 0.15, 0.10, 0.10],
            [0.05, 0.58, 0.22, 0.08, 0.05, 0.02],
            [0.03, 0.25, 0.52, 0.12, 0.05, 0.03],
            [0.08, 0.12, 0.18, 0.42, 0.15, 0.05],
            [0.04, 0.06, 0.05, 0.21, 0.56, 0.08],
            [0.06, 0.08, 0.04, 0.10, 0.12, 0.60],
        ]

    cell_size = 46
    start_x = 180
    start_y = 60
    n_q = len(tokens_q)
    n_k = len(tokens_k)

    heatmap_cells = []
    # Key tokens (top)
    for j, tk in enumerate(tokens_k):
        heatmap_cells.append(
            f'<text x="{start_x + j*cell_size + cell_size/2}" y="{start_y - 12}" fill="#94A3B8" font-family="\'JetBrains Mono\', monospace" font-size="11" font-weight="700" text-anchor="middle">{html.escape(tk)}</text>'
        )

    # Query tokens (left) & Grid cells
    for i, tq in enumerate(tokens_q):
        is_focus = (i == focus_idx)
        label_col = "#38BDF8" if is_focus else "#94A3B8"
        heatmap_cells.append(
            f'<text x="{start_x - 14}" y="{start_y + i*cell_size + cell_size/2 + 4}" fill="{label_col}" font-family="\'JetBrains Mono\', monospace" font-size="11" font-weight="700" text-anchor="end">{html.escape(tq)}</text>'
        )

        for j in range(n_k):
            val = weights[i][j]
            # Color map: deep navy (0.0) -> purple (0.3) -> cyan/emerald (0.6+)
            r = int(14 + 180 * val)
            g = int(24 + 140 * val)
            b = int(60 + 195 * val)
            alpha = max(0.2, min(0.95, val * 1.5))

            border_stroke = "#38BDF8" if (is_focus and val > 0.15) else "rgba(255,255,255,0.06)"
            border_w = 2 if is_focus else 1

            heatmap_cells.append(
                f'<rect x="{start_x + j*cell_size}" y="{start_y + i*cell_size}" width="{cell_size - 3}" height="{cell_size - 3}" fill="rgba({r},{g},{b},{alpha:.2f})" stroke="{border_stroke}" stroke-width="{border_w}" rx="4"/>'
            )
            # Text val
            text_col = "#F8FAFC" if val > 0.25 else "#64748B"
            heatmap_cells.append(
                f'<text x="{start_x + j*cell_size + cell_size/2 - 1.5}" y="{start_y + i*cell_size + cell_size/2 + 4}" fill="{text_col}" font-family="\'JetBrains Mono\', monospace" font-size="10" font-weight="600" text-anchor="middle">{val:.2f}</text>'
            )

    # Crosshair glow bounding box around focus query row
    focus_box = f'<rect x="{start_x - 4}" y="{start_y + focus_idx*cell_size - 3}" width="{n_k*cell_size + 8}" height="{cell_size + 3}" fill="none" stroke="#38BDF8" stroke-width="1.5" stroke-dasharray="4,2" rx="6"/>'

    return f"""
    <div style="background: #0A0E17; border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 20px 24px; width: {width}px; height: {height}px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: space-between; font-family: -apple-system, BlinkMacSystemFont, 'Inter', sans-serif;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 10px;">
            <div>
                <div style="font-size: 11px; font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #EC4899; letter-spacing: 1px;">OBSERVABLE // ATTENTION WEIGHT MATRIX</div>
                <div style="font-size: 16px; font-weight: 800; color: #F8FAFC; margin-top: 2px;">{html.escape(title)}</div>
                <div style="font-size: 12px; color: #64748B;">{html.escape(subtitle)}</div>
            </div>
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 10px; background: rgba(236,72,153,0.15); border: 1px solid rgba(236,72,153,0.4); padding: 4px 8px; border-radius: 4px; color: #F472B6;">
                HEAD 04 / 08 // TEMPERATURE τ = 1.0
            </div>
        </div>
        <div style="flex: 1; position: relative;">
            <svg width="100%" height="100%" viewBox="0 0 760 380" style="overflow: visible;">
                {''.join(heatmap_cells)}
                {focus_box}
            </svg>
        </div>
    </div>
    """


# ==============================================================================
# 10. 3D SPATIAL, MESH & ROBOTICS KINEMATICS (PyVista, Viser, Three.js)
# ==============================================================================
def render_pyvista_streamlines_vector_field(
    title: str = "3D CONTINUOUS VECTOR FIELD STREAMLINES",
    subtitle: str = "Iso-Surface Velocity Magnitude Gradient via Scientific Colormap",
    width: int = 860,
    height: int = 520,
) -> str:
    """
    Renders a PyVista / VTK-style scientific 3D vector field streamline visualization.
    Shows:
      - 3D bounding bounding cage with coordinate ticks
      - Fluid/Velocity field streamlines with gradient colors (blue to yellow/red)
      - Integrated scientific colorbar on right with numerical units (m/s)
    """
    cx, cy = 360, 240
    # Parametric streamline trajectories
    streamline_paths = []
    num_streamlines = 14
    for s in range(num_streamlines):
        pts = []
        phase = s * 0.45
        for t in range(35):
            x = (t - 17) * 16
            y = 55 * math.sin(t * 0.18 + phase) + (s - 7) * 18
            z = 40 * math.cos(t * 0.15 + phase * 0.7)

            # Isometric projection
            iso_x = cx + x * 0.85 + z * 0.45
            iso_y = cy + y * 0.75 - z * 0.35
            pts.append((iso_x, iso_y))

        # Build path
        d = f"M {pts[0][0]:.1f} {pts[0][1]:.1f} " + " ".join(f"L {p[0]:.1f} {p[1]:.1f}" for p in pts[1:])
        col = "#38BDF8" if s % 3 == 0 else ("#10B981" if s % 3 == 1 else "#F59E0B")
        streamline_paths.append(
            f'<path d="{d}" fill="none" stroke="{col}" stroke-width="1.8" opacity="0.85"/>'
        )

    # 3D Bounding Box Wireframe
    bx0, by0 = cx - 220, cy - 130
    bw, bh, bd = 440, 240, 100
    box_lines = f"""
    <rect x="{bx0}" y="{by0}" width="{bw}" height="{bh}" fill="none" stroke="#334155" stroke-width="1" stroke-dasharray="3,3"/>
    <line x1="{bx0}" y1="{by0}" x2="{bx0 + bd*0.5}" y2="{by0 - bd*0.35}" stroke="#334155" stroke-width="1" stroke-dasharray="3,3"/>
    <line x1="{bx0 + bw}" y1="{by0}" x2="{bx0 + bw + bd*0.5}" y2="{by0 - bd*0.35}" stroke="#334155" stroke-width="1" stroke-dasharray="3,3"/>
    """

    # Colorbar on right
    colorbar = f"""
    <g transform="translate(710, 80)">
        <text x="0" y="-12" fill="#94A3B8" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700">|v| (m/s)</text>
        <defs>
            <linearGradient id="cbar-grad" x1="0" y1="0" x2="0" y2="1">
                <stop offset="0%" stop-color="#EF4444"/>
                <stop offset="50%" stop-color="#F59E0B"/>
                <stop offset="100%" stop-color="#38BDF8"/>
            </linearGradient>
        </defs>
        <rect x="0" y="0" width="14" height="200" fill="url(#cbar-grad)" rx="3"/>
        <text x="20" y="10" fill="#EF4444" font-family="'JetBrains Mono', monospace" font-size="10">2.80</text>
        <text x="20" y="105" fill="#F59E0B" font-family="'JetBrains Mono', monospace" font-size="10">1.40</text>
        <text x="20" y="200" fill="#38BDF8" font-family="'JetBrains Mono', monospace" font-size="10">0.05</text>
    </g>
    """

    return f"""
    <div style="background: #0A0E17; border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 20px 24px; width: {width}px; height: {height}px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: space-between; font-family: -apple-system, BlinkMacSystemFont, 'Inter', sans-serif;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 10px;">
            <div>
                <div style="font-size: 11px; font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #10B981; letter-spacing: 1px;">PYVISTA // 3D STREAMLINES & VELOCITY</div>
                <div style="font-size: 16px; font-weight: 800; color: #F8FAFC; margin-top: 2px;">{html.escape(title)}</div>
                <div style="font-size: 12px; color: #64748B;">{html.escape(subtitle)}</div>
            </div>
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 10px; background: rgba(16,185,129,0.15); border: 1px solid rgba(16,185,129,0.4); padding: 4px 8px; border-radius: 4px; color: #34D399;">
                GRID: 128×128×64 // VTK ZERO-COPY
            </div>
        </div>
        <div style="flex: 1; position: relative;">
            <svg width="100%" height="100%" viewBox="0 0 780 380" style="overflow: visible;">
                {box_lines}
                {''.join(streamline_paths)}
                {colorbar}
            </svg>
        </div>
    </div>
    """


# ==============================================================================
# 11. GENERAL SCIENTIFIC COMPUTING & OPTIMIZATION (Plotly / Celluloid)
# ==============================================================================
def render_optimization_contour_paths(
    title: str = "NON-CONVEX OPTIMIZATION LANDSCAPE CONVERGENCE",
    subtitle: str = "Contour Gradient Descent Trajectories: SGD vs Momentum vs Adam",
    width: int = 860,
    height: int = 520,
) -> str:
    """
    Renders an optimization contour map comparing optimizer trajectories (Plotly / Celluloid style).
    Shows:
      - 2D concentric elliptical contours of Rosenbrock / saddle function
      - Three comparative optimizer paths (SGD oscillatory, Momentum smoothed, Adam direct)
      - Minimum attractor target marker (*)
      - Legend and step telemetry summary
    """
    cx, cy = 360, 240

    # Draw elliptical contour curves
    contours = []
    radii = [(40, 25), (80, 50), (130, 85), (190, 125), (260, 175)]
    for rx, ry in radii:
        contours.append(
            f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" stroke="rgba(255,255,255,0.07)" stroke-width="1.2"/>'
        )

    # Optimizer trajectories: start at top-left (cx - 220, cy - 140), converge to (cx, cy)
    # SGD: heavy oscillations
    sgd_pts = [(cx - 220, cy - 140), (cx - 180, cy - 40), (cx - 160, cy - 120), (cx - 110, cy - 20), (cx - 80, cy - 80), (cx - 40, cy - 10), (cx - 15, cy - 30), (cx - 5, cy - 5)]
    sgd_d = f"M {sgd_pts[0][0]} {sgd_pts[0][1]} " + " ".join(f"L {p[0]} {p[1]}" for p in sgd_pts[1:])

    # Momentum: damped curve
    mom_pts = [(cx - 220, cy - 140), (cx - 140, cy - 60), (cx - 90, cy - 85), (cx - 40, cy - 35), (cx - 10, cy - 10), (cx, cy)]
    mom_d = f"M {mom_pts[0][0]} {mom_pts[0][1]} " + " ".join(f"L {p[0]} {p[1]}" for p in mom_pts[1:])

    # Adam: fast direct descent
    adam_pts = [(cx - 220, cy - 140), (cx - 110, cy - 90), (cx - 40, cy - 40), (cx - 10, cy - 10), (cx, cy)]
    adam_d = f"M {adam_pts[0][0]} {adam_pts[0][1]} " + " ".join(f"L {p[0]} {p[1]}" for p in adam_pts[1:])

    trajectories = f"""
    <!-- SGD -->
    <path d="{sgd_d}" fill="none" stroke="#EF4444" stroke-width="2.2" stroke-dasharray="3,2"/>
    <!-- Momentum -->
    <path d="{mom_d}" fill="none" stroke="#F59E0B" stroke-width="2.5"/>
    <!-- Adam -->
    <path d="{adam_d}" fill="none" stroke="#10B981" stroke-width="3"/>
    <!-- Target Minima -->
    <circle cx="{cx}" cy="{cy}" r="6" fill="#10B981"/>
    <circle cx="{cx}" cy="{cy}" r="14" fill="none" stroke="#10B981" stroke-width="1.5" stroke-dasharray="3,3"/>
    <text x="{cx + 18}" y="{cy + 4}" fill="#10B981" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="800">GLOBAL MIN θ*</text>
    """

    return f"""
    <div style="background: #0A0E17; border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 20px 24px; width: {width}px; height: {height}px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: space-between; font-family: -apple-system, BlinkMacSystemFont, 'Inter', sans-serif;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 10px;">
            <div>
                <div style="font-size: 11px; font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #F59E0B; letter-spacing: 1px;">PLOTLY // NON-CONVEX OPTIMIZATION</div>
                <div style="font-size: 16px; font-weight: 800; color: #F8FAFC; margin-top: 2px;">{html.escape(title)}</div>
                <div style="font-size: 12px; color: #64748B;">{html.escape(subtitle)}</div>
            </div>
            <div style="display: flex; gap: 12px; font-family: 'JetBrains Mono', monospace; font-size: 10px;">
                <span style="color: #EF4444;">-- SGD (120 eps)</span>
                <span style="color: #F59E0B;">— Momentum (45 eps)</span>
                <span style="color: #10B981; font-weight: 700;">— Adam (18 eps)</span>
            </div>
        </div>
        <div style="flex: 1; position: relative;">
            <svg width="100%" height="100%" viewBox="0 0 760 380" style="overflow: visible;">
                {''.join(contours)}
                {trajectories}
            </svg>
        </div>
    </div>
    """


# ==============================================================================
# 12. CYBER-ACADEMIC HUD & HIGH-DENSITY DASHBOARD LAYOUT SYSTEM
# ==============================================================================
def render_scientific_terminal_card(
    inner_content_html: str,
    status_tag: str = "STATUS: NOMINAL // 60 FPS",
    telemetry: dict = None,
    title: str = "COMPUTATIONAL TELEMETRY",
    width: str = "100%",
    height: str = "auto",
) -> str:
    """
    Wraps any component or text in a high-tech Cyber-Academic HUD frame:
      - Precision corner crosshairs '+'
      - Micro coordinate tick marks
      - Monospace status & telemetry header
    """
    if telemetry is None:
        telemetry = {"LATENCY": "1.8ms", "JITTER": "±0.04ms", "CONVERGED": "TRUE"}

    tele_spans = " ".join(
        f'<span style="color: #64748B;">{k}:</span> <b style="color: #F8FAFC;">{v}</b> |'
        for k, v in telemetry.items()
    )

    return f"""
    <div style="
        position: relative;
        background: rgba(10, 14, 23, 0.85);
        border: 1px solid rgba(56, 189, 248, 0.22);
        box-shadow: inset 0 0 20px rgba(56, 189, 248, 0.03), 0 8px 32px rgba(0,0,0,0.4);
        border-radius: 8px;
        padding: 16px 20px;
        width: {width};
        height: {height};
        box-sizing: border-box;
        font-family: -apple-system, BlinkMacSystemFont, 'Inter', sans-serif;
    ">
        <!-- Precision Corner Crosshairs -->
        <div style="position: absolute; top: -5px; left: -5px; color: #38BDF8; font-size: 10px; font-family: monospace; line-height: 10px;">+</div>
        <div style="position: absolute; top: -5px; right: -5px; color: #38BDF8; font-size: 10px; font-family: monospace; line-height: 10px;">+</div>
        <div style="position: absolute; bottom: -5px; left: -5px; color: #38BDF8; font-size: 10px; font-family: monospace; line-height: 10px;">+</div>
        <div style="position: absolute; bottom: -5px; right: -5px; color: #38BDF8; font-size: 10px; font-family: monospace; line-height: 10px;">+</div>

        <!-- Header Ribbon -->
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 8px; margin-bottom: 12px;">
            <div style="display: flex; align-items: center; gap: 8px;">
                <span style="display: inline-block; width: 6px; height: 6px; border-radius: 50%; background: #10B981; box-shadow: 0 0 8px #10B981;"></span>
                <span style="font-family: 'JetBrains Mono', monospace; font-size: 11px; font-weight: 700; color: #38BDF8; letter-spacing: 0.5px;">{html.escape(title)}</span>
            </div>
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 10px; color: #94A3B8;">
                {html.escape(status_tag)}
            </div>
        </div>

        <!-- Main Inner Content -->
        <div style="box-sizing: border-box;">
            {inner_content_html}
        </div>

        <!-- Bottom Micro-Telemetry Ruler -->
        <div style="border-top: 1px solid rgba(255,255,255,0.06); margin-top: 12px; padding-top: 8px; display: flex; justify-content: space-between; align-items: center; font-family: 'JetBrains Mono', monospace; font-size: 10px;">
            <div>{tele_spans}</div>
            <div style="color: #475569;">SEC-VERIFIED // DEEPTUTOR HUD</div>
        </div>
    </div>
    """


def render_cyber_academic_dashboard_layout(
    scene_kicker: str,
    scene_title: str,
    status_badge: str,
    main_component_html: str,
    side_panel_html: str,
    bottom_telemetry_html: str = "",
) -> str:
    """
    High-density asymmetric scientific dashboard layout:
      - Top: Swiss Kicker + Bold Title + Global Status Badge
      - Middle: 68% Left Main Scientific Component + 32% Right Deduction / Parametric Panel
      - Bottom: Monospace Streaming Execution Log / Telemetry Band
    """
    return f"""
    <div class="scene-layout-container" style="
        width: 1920px; height: 1080px; background: #080C14; color: #FFFFFF;
        display: flex; flex-direction: column; padding: 50px 80px; box-sizing: border-box;
        font-family: -apple-system, BlinkMacSystemFont, 'Inter', sans-serif;
    ">
        <!-- Top HUD Navigation Bar -->
        <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 22px; border-bottom: 1px solid rgba(255,255,255,0.08); padding-bottom: 14px;">
            <div>
                <div style="font-family: 'JetBrains Mono', monospace; font-size: 12px; font-weight: 700; color: #38BDF8; letter-spacing: 1.5px; text-transform: uppercase;">
                    {html.escape(scene_kicker)}
                </div>
                <div style="font-size: 32px; font-weight: 800; color: #F8FAFC; margin-top: 2px;">
                    {html.escape(scene_title)}
                </div>
            </div>
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; background: rgba(56,189,248,0.12); border: 1px solid rgba(56,189,248,0.35); padding: 5px 12px; border-radius: 6px; color: #38BDF8; font-weight: 700;">
                {html.escape(status_badge)}
            </div>
        </div>

        <!-- Center Workspace: Asymmetric 68% vs 32% -->
        <div style="flex: 1; display: flex; gap: 24px; box-sizing: border-box; overflow: hidden;">
            <div style="flex: 68; display: flex; flex-direction: column;">
                {main_component_html}
            </div>
            <div style="flex: 32; display: flex; flex-direction: column;">
                {side_panel_html}
            </div>
        </div>

        <!-- Optional Bottom Stream Telemetry -->
        {f'''
        <div style="margin-top: 14px; background: rgba(15,23,42,0.6); border: 1px solid rgba(255,255,255,0.06); border-radius: 6px; padding: 8px 16px; font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #64748B; display: flex; justify-content: space-between;">
            {bottom_telemetry_html}
        </div>
        ''' if bottom_telemetry_html else ''}
    </div>
    """


def render_triptych_pipeline_layout(
    scene_kicker: str,
    scene_title: str,
    stages: list[dict],
    interconnect_label: str = "SYNCHRONOUS DATA BUS // 500Hz",
) -> str:
    """
    Layout: 3-column Triptych Scientific Pipeline.
    stages = [
        {"num": "01", "name": "STAGE A", "tag": "SENSORY ENCODER", "desc": "...", "metrics": {"LATENCY": "2ms", "BANDWIDTH": "120MB/s"}, "color": "#38BDF8"},
        {"num": "02", "name": "STAGE B", "tag": "DYNAMIC PLANNER", "desc": "...", "metrics": {"SOLVER": "QP-MPC", "HORIZON": "50 steps"}, "color": "#6366F1"},
        {"num": "03", "name": "STAGE C", "tag": "PD CONTROLLER", "desc": "...", "metrics": {"FREQ": "500Hz", "PHASE_MARGIN": "48°"}, "color": "#10B981"}
    ]
    """
    card_htmls = []
    for s in stages:
        col = s.get("color", "#38BDF8")
        metric_rows = "".join(
            f'<div style="display: flex; justify-content: space-between; margin-bottom: 4px;"><span style="color: #64748B;">{k}</span><b style="color: #F8FAFC;">{v}</b></div>'
            for k, v in s.get("metrics", {}).items()
        )
        card_htmls.append(f"""
        <div style="flex: 1; background: #0D1322; border: 1px solid rgba(255,255,255,0.08); border-top: 4px solid {col}; border-radius: 10px; padding: 22px; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <span style="font-family: 'JetBrains Mono', monospace; font-size: 11px; font-weight: 800; color: {col};">{html.escape(s.get("num", ""))} // {html.escape(s.get("tag", ""))}</span>
                </div>
                <div style="font-size: 20px; font-weight: 800; color: #FFFFFF; margin-bottom: 8px;">{html.escape(s["name"])}</div>
                <p style="font-size: 13.5px; color: #94A3B8; line-height: 1.5; margin: 0 0 16px 0;">{html.escape(s["desc"])}</p>
            </div>
            <div style="background: rgba(0,0,0,0.3); border: 1px solid rgba(255,255,255,0.05); border-radius: 6px; padding: 10px 14px; font-family: 'JetBrains Mono', monospace; font-size: 11px;">
                {metric_rows}
            </div>
        </div>
        """)

    return f"""
    <div class="scene-layout-container" style="
        width: 1920px; height: 1080px; background: #080C14; color: #FFFFFF;
        display: flex; flex-direction: column; padding: 60px 100px; box-sizing: border-box;
        font-family: -apple-system, BlinkMacSystemFont, 'Inter', sans-serif;
    ">
        <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 24px;">
            <div>
                <div style="font-family: 'JetBrains Mono', monospace; font-size: 13px; font-weight: 700; color: #38BDF8; letter-spacing: 1px; text-transform: uppercase;">
                    {html.escape(scene_kicker)}
                </div>
                <div style="font-size: 34px; font-weight: 800; color: #F8FAFC; margin-top: 4px;">
                    {html.escape(scene_title)}
                </div>
            </div>
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #64748B;">
                BUS ARCHITECTURE // {html.escape(interconnect_label)}
            </div>
        </div>

        <div style="flex: 1; display: flex; gap: 24px; position: relative;">
            {''.join(card_htmls)}
        </div>
    </div>
    """
