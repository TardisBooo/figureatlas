"""
Scientific Visual Studio: Abstract Domain-Agnostic Component Library.
Inspired by figures4papers, SciencePlots, 3Blue1Brown/Manim, and Teachable Figures.
Zero hardcoded business/course logic. Purely parameter-driven SVG/HTML visual primitives.
"""

import math
import html


# ==============================================================================
# 1. PREMIUM HERO COVER (High-End Cinema-Grade Cover)
# ==============================================================================
def render_premium_hero_cover(
    title: str,
    subtitle: str,
    eyebrow_badge: str = "✦ ADVANCED ACADEMY CURRICULUM",
    module_tag: str = "// MODULE SPECIFICATION",
    feature_chips: list[str] = None,
    accent_color: str = "#6366F1",
    secondary_accent: str = "#38BDF8",
    footer_text: str = "SCIENTIFIC VISUAL STUDIO · PARAMETRIC SYSTEM · 1080P ULTRA-HD",
) -> str:
    """
    Renders a high-end, luxury tech cinema-grade cover.
    Features:
      - Deep sapphire canvas (#080C14 -> #0B1120)
      - Dual bioluminescent aurora refractive glow fields
      - Parametric 3D Wireframe Mathematical Torus Knot / Manifold on the right
      - Swiss typography hierarchy: Eyebrow badge, monospaced tag, giant gradient title, subtitle, chips
    """
    if feature_chips is None:
        feature_chips = [
            "✦ 17-Scene Pedagogical Pipeline",
            "✦ 3B1B Parametric Dynamic Geometry",
            "✦ Formally Verified Local Codebase",
            "✦ Dual-Pane Synchronized Inspection",
        ]

    # Generate 3D parametric Torus Knot / Manifold SVG paths
    # Center around (1420, 540), radius ~240
    knot_paths = []
    p, q = 3, 7  # Torus knot harmonic frequencies
    num_points = 240
    cx, cy = 1380, 540
    R = 210
    r = 95

    coords_3d = []
    for i in range(num_points):
        phi = 2 * math.pi * i / num_points
        r_current = R + r * math.cos(q * phi)
        x = r_current * math.cos(p * phi)
        y = r_current * math.sin(p * phi)
        z = -r * math.sin(q * phi)

        # 3D isometric projection (rotate around X and Y)
        rot_y = 0.55
        rot_x = 0.45
        x_rot = x * math.cos(rot_y) + z * math.sin(rot_y)
        z_rot = -x * math.sin(rot_y) + z * math.cos(rot_y)
        y_rot = y * math.cos(rot_x) - z_rot * math.sin(rot_x)

        # Screen coordinates
        sx = cx + x_rot * 0.95
        sy = cy + y_rot * 0.95
        coords_3d.append((sx, sy, z_rot))

    # Build wireframe segments with depth-based opacity
    path_d = ""
    for i in range(num_points):
        x1, y1, _ = coords_3d[i]
        x2, y2, _ = coords_3d[(i + 1) % num_points]
        if i == 0:
            path_d += f"M {x1:.1f} {y1:.1f} "
        else:
            path_d += f"L {x1:.1f} {y1:.1f} "
    path_d += "Z"

    # Radial ring harmonics
    ring_lines = []
    for step in range(0, num_points, 8):
        x, y, z = coords_3d[step]
        alpha = max(0.15, min(0.85, 0.5 + z / 220))
        ring_lines.append(
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.5" fill="{secondary_accent}" opacity="{alpha:.2f}"/>'
        )

    chips_html = "".join(
        f'<div class="cover-chip">{html.escape(c)}</div>' for c in feature_chips
    )

    return f"""
    <div class="cover-hero-wrapper" style="
        position: relative;
        width: 1920px;
        height: 1080px;
        background: radial-gradient(circle at 85% 30%, #151d38 0%, #090d16 55%, #05070c 100%);
        overflow: hidden;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        padding: 80px 100px;
        box-sizing: border-box;
        font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif;
        color: #FFFFFF;
    ">
        <!-- Aurora Glow Refractions -->
        <div style="position: absolute; top: -120px; right: 180px; width: 680px; height: 680px; background: radial-gradient(circle, {accent_color}55 0%, transparent 70%); filter: blur(90px); pointer-events: none;"></div>
        <div style="position: absolute; bottom: -80px; right: 480px; width: 540px; height: 540px; background: radial-gradient(circle, {secondary_accent}44 0%, transparent 70%); filter: blur(80px); pointer-events: none;"></div>
        <div style="position: absolute; top: 180px; left: -100px; width: 480px; height: 480px; background: radial-gradient(circle, {accent_color}22 0%, transparent 70%); filter: blur(100px); pointer-events: none;"></div>

        <!-- 3D Geometric Mathematical Wireframe Centerpiece -->
        <svg style="position: absolute; top: 0; left: 0; width: 1920px; height: 1080px; pointer-events: none;" viewBox="0 0 1920 1080">
            <defs>
                <linearGradient id="torusGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="{secondary_accent}" stop-opacity="0.9" />
                    <stop offset="50%" stop-color="{accent_color}" stop-opacity="0.75" />
                    <stop offset="100%" stop-color="#ec4899" stop-opacity="0.5" />
                </linearGradient>
                <filter id="glowFilter" x="-20%" y="-20%" width="140%" height="140%">
                    <feGaussianBlur stdDeviation="8" result="blur" />
                    <feMerge>
                        <feMergeNode in="blur"/>
                        <feMergeNode in="SourceGraphic"/>
                    </feMerge>
                </filter>
            </defs>
            <!-- Orbit rings -->
            <ellipse cx="{cx}" cy="{cy}" rx="320" ry="140" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1.5" stroke-dasharray="6,6" transform="rotate(-15 {cx} {cy})"/>
            <ellipse cx="{cx}" cy="{cy}" rx="380" ry="170" fill="none" stroke="{accent_color}33" stroke-width="1" />
            <!-- Glowing Torus Knot Contour -->
            <path d="{path_d}" fill="none" stroke="url(#torusGrad)" stroke-width="3" filter="url(#glowFilter)" opacity="0.95"/>
            <!-- Coordinate Nodes -->
            {''.join(ring_lines)}
        </svg>

        <!-- Top Header Navigation Bar -->
        <div style="position: relative; z-index: 10; display: flex; justify-content: space-between; align-items: center;">
            <div style="display: flex; align-items: center; gap: 16px;">
                <div style="
                    display: inline-flex;
                    align-items: center;
                    gap: 8px;
                    padding: 8px 18px;
                    background: rgba(99, 102, 241, 0.15);
                    border: 1px solid rgba(99, 102, 241, 0.4);
                    border-radius: 999px;
                    font-size: 13px;
                    font-weight: 700;
                    letter-spacing: 1.5px;
                    color: #A5B4FC;
                    text-transform: uppercase;
                ">
                    {html.escape(eyebrow_badge)}
                </div>
                <span style="font-family: 'JetBrains Mono', monospace; font-size: 13px; color: #64748B; letter-spacing: 1px;">
                    {html.escape(module_tag)}
                </span>
            </div>
            <div style="display: flex; gap: 12px;">
                <span style="padding: 6px 14px; background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.12); border-radius: 6px; font-size: 12px; font-weight: 600; color: #94A3B8; letter-spacing: 0.5px;">1080P UHD</span>
                <span style="padding: 6px 14px; background: rgba(56, 189, 248, 0.12); border: 1px solid rgba(56, 189, 248, 0.35); border-radius: 6px; font-size: 12px; font-weight: 700; color: #38BDF8; letter-spacing: 0.5px;">17 SCENES</span>
            </div>
        </div>

        <!-- Center Content Block -->
        <div style="position: relative; z-index: 10; max-width: 980px; margin-top: 40px; margin-bottom: auto;">
            <h1 style="
                font-size: 68px;
                font-weight: 900;
                line-height: 1.12;
                letter-spacing: -1.5px;
                margin: 0 0 24px 0;
                background: linear-gradient(135deg, #FFFFFF 0%, #F1F5F9 50%, #94A3B8 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                text-shadow: 0 10px 30px rgba(0,0,0,0.5);
            ">
                {html.escape(title)}
            </h1>
            <p style="
                font-size: 24px;
                font-weight: 400;
                line-height: 1.55;
                color: #CBD5E1;
                margin: 0 0 38px 0;
                max-width: 880px;
                text-shadow: 0 2px 10px rgba(0,0,0,0.4);
            ">
                {html.escape(subtitle)}
            </p>

            <!-- Feature Chips Row -->
            <div style="display: flex; flex-wrap: wrap; gap: 14px;">
                {chips_html}
            </div>
        </div>

        <!-- Footer Bar -->
        <div style="
            position: relative;
            z-index: 10;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-top: 1px solid rgba(255,255,255,0.08);
            padding-top: 24px;
            font-size: 12.5px;
            color: #64748B;
            font-family: 'JetBrains Mono', monospace;
            letter-spacing: 1px;
        ">
            <div>{html.escape(footer_text)}</div>
            <div>VERIFIED ARCHITECTURE · MATHEMATICALLY GROUNDED</div>
        </div>
    </div>
    """


# ==============================================================================
# 2. 3B1B & MOTION CANVAS DYNAMIC MATH: 3D LOSS LANDSCAPE
# ==============================================================================
def render_loss_landscape_3d(
    title: str = "3D Optimization Loss Landscape & Gradient Descent Trajectory",
    subtitle: str = "Non-convex parameter manifold with momentum vs vanilla SGD trajectories",
    contour_levels: int = 12,
    accent: str = "#6366F1",
) -> str:
    """
    Renders an abstract 3D loss surface with contour projection and gradient descent trajectories.
    Pure parametric SVG math with perspective isometric projection.
    """
    w, h = 900, 520
    cx, cy = 450, 310

    # Draw perspective mesh lines
    grid_paths = []
    nx, ny = 24, 24
    for ix in range(-nx, nx + 1, 2):
        pts = []
        for iy in range(-ny, ny + 1, 2):
            x_val = ix * 0.15
            y_val = iy * 0.15
            # Non-convex Ackley/Rastrigin-like loss function
            z_val = 0.5 * (x_val**2 + y_val**2) - 0.45 * math.cos(
                2.5 * x_val
            ) - 0.45 * math.cos(2.5 * y_val) + 0.9

            # Isometric 3D to 2D
            px = cx + (ix - iy) * 16.5
            py = cy + (ix + iy) * 7.5 - z_val * 62
            pts.append((px, py))

        d = "M " + " L ".join(f"{p[0]:.1f},{p[1]:.1f}" for p in pts)
        grid_paths.append(
            f'<path d="{d}" fill="none" stroke="rgba(99,102,241,0.22)" stroke-width="1.2" />'
        )

    for iy in range(-ny, ny + 1, 2):
        pts = []
        for ix in range(-nx, nx + 1, 2):
            x_val = ix * 0.15
            y_val = iy * 0.15
            z_val = 0.5 * (x_val**2 + y_val**2) - 0.45 * math.cos(
                2.5 * x_val
            ) - 0.45 * math.cos(2.5 * y_val) + 0.9
            px = cx + (ix - iy) * 16.5
            py = cy + (ix + iy) * 7.5 - z_val * 62
            pts.append((px, py))
        d = "M " + " L ".join(f"{p[0]:.1f},{p[1]:.1f}" for p in pts)
        grid_paths.append(
            f'<path d="{d}" fill="none" stroke="rgba(56,189,248,0.22)" stroke-width="1.2" />'
        )

    # Simulated Optimization Trajectories
    # 1. Momentum Optimizer Trajectory (Emerald curve smoothly rolling to global min)
    mom_pts = [
        (18, 16, 2.8),
        (14, 11, 2.1),
        (9, 6, 1.4),
        (5, 2, 0.8),
        (2, -1, 0.4),
        (0.5, 0, 0.1),
    ]
    mom_coords = []
    for ix, iy, z in mom_pts:
        px = cx + (ix - iy) * 16.5
        py = cy + (ix + iy) * 7.5 - z * 62
        mom_coords.append((px, py))
    mom_path = "M " + " L ".join(f"{p[0]:.1f},{p[1]:.1f}" for p in mom_coords)

    # 2. Vanilla SGD Trajectory (Amber zig-zagging in high-curvature valley)
    sgd_pts = [
        (18, 16, 2.8),
        (12, 18, 2.6),
        (14, 8, 2.2),
        (7, 13, 1.8),
        (8, 4, 1.3),
        (3, 7, 0.9),
        (4, 1, 0.6),
    ]
    sgd_coords = []
    for ix, iy, z in sgd_pts:
        px = cx + (ix - iy) * 16.5
        py = cy + (ix + iy) * 7.5 - z * 62
        sgd_coords.append((px, py))
    sgd_path = "M " + " L ".join(f"{p[0]:.1f},{p[1]:.1f}" for p in sgd_coords)

    return f"""
    <div style="background: #0d121f; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; padding: 22px; color: #FFFFFF; font-family: -apple-system, sans-serif;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
            <div>
                <div style="font-size: 16px; font-weight: 700; color: #F8FAFC;">{html.escape(title)}</div>
                <div style="font-size: 12.5px; color: #94A3B8; margin-top: 3px;">{html.escape(subtitle)}</div>
            </div>
            <div style="display: flex; gap: 14px; font-size: 12px; font-family: 'JetBrains Mono', monospace;">
                <span style="color: #10B981; display: flex; align-items: center; gap: 5px;">
                    <span style="width: 10px; height: 10px; border-radius: 50%; background: #10B981; display: inline-block;"></span>
                    Momentum Accelerated (Smooth)
                </span>
                <span style="color: #F59E0B; display: flex; align-items: center; gap: 5px;">
                    <span style="width: 10px; height: 10px; border-radius: 50%; background: #F59E0B; display: inline-block;"></span>
                    Vanilla SGD (Oscillating)
                </span>
            </div>
        </div>

        <svg viewBox="0 0 {w} {h}" style="width: 100%; height: auto; display: block; background: #080C14; border-radius: 8px; border: 1px solid rgba(255,255,255,0.06);">
            <!-- Contour Mesh -->
            {''.join(grid_paths)}

            <!-- Vanilla SGD Path -->
            <path d="{sgd_path}" fill="none" stroke="#F59E0B" stroke-width="3" stroke-dasharray="6,4" opacity="0.9" />
            {''.join(f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="4.5" fill="#F59E0B" />' for p in sgd_coords)}

            <!-- Momentum Accelerated Path with Glow -->
            <path d="{mom_path}" fill="none" stroke="#10B981" stroke-width="3.5" filter="drop-shadow(0 0 6px rgba(16,185,129,0.7))" />
            {''.join(f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="5" fill="#10B981" stroke="#FFFFFF" stroke-width="1.5" />' for p in mom_coords)}

            <!-- Global Minimum Indicator -->
            <circle cx="{mom_coords[-1][0]:.1f}" cy="{mom_coords[-1][1]:.1f}" r="9" fill="none" stroke="#38BDF8" stroke-width="2" stroke-dasharray="3,3" />
            <text x="{mom_coords[-1][0] + 16:.1f}" y="{mom_coords[-1][1] + 4:.1f}" fill="#38BDF8" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700">Global Minimum (L ≈ 0.00)</text>
        </svg>
    </div>
    """


# ==============================================================================
# 3. ACADEMIC & RESEARCH PLOT: CONVERGENCE BAND (SciencePlots Inspired)
# ==============================================================================
def render_convergence_band_plot(
    title: str = "Empirical Convergence Rate & Variance Bound (SciencePlots Standard)",
    subtitle: str = "Mean loss with 95% confidence interval shaded regions across 5 random seeds",
    x_label: str = "Training Iterations (kSteps)",
    y_label: str = "Empirical Risk / Loss L(θ)",
) -> str:
    """
    Renders a publication-grade convergence curve with shaded variance bands.
    Inspired by SciencePlots and figures4papers.
    """
    w, h = 900, 480
    pad_l, pad_r, pad_t, pad_b = 90, 40, 40, 70
    plot_w = w - pad_l - pad_r
    plot_h = h - pad_t - pad_b

    # Synthetic multi-seed data
    steps = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

    # Baseline Method (slower convergence, wider variance)
    base_mean = [
        3.4,
        2.85,
        2.42,
        2.10,
        1.85,
        1.68,
        1.55,
        1.45,
        1.38,
        1.32,
        1.28,
    ]
    base_std = [
        0.32,
        0.28,
        0.25,
        0.22,
        0.20,
        0.18,
        0.16,
        0.15,
        0.14,
        0.13,
        0.12,
    ]

    # Proposed Method (rapid convergence, narrow variance)
    prop_mean = [
        3.4,
        2.10,
        1.42,
        0.95,
        0.65,
        0.48,
        0.36,
        0.28,
        0.22,
        0.18,
        0.15,
    ]
    prop_std = [
        0.30,
        0.18,
        0.12,
        0.08,
        0.06,
        0.05,
        0.04,
        0.03,
        0.02,
        0.02,
        0.015,
    ]

    max_y, min_y = 3.8, 0.0

    def to_screen(step, val):
        sx = pad_l + (step / 50.0) * plot_w
        sy = pad_t + ((max_y - val) / (max_y - min_y)) * plot_h
        return sx, sy

    # Build shaded band paths
    def make_band_path(means, stds):
        top_pts = [
            to_screen(s, m + st) for s, m, st in zip(steps, means, stds)
        ]
        bot_pts = [
            to_screen(s, max(0, m - st))
            for s, m, st in zip(steps, means, stds)
        ]
        d = "M " + " L ".join(f"{p[0]:.1f},{p[1]:.1f}" for p in top_pts)
        d += " L " + " L ".join(f"{p[0]:.1f},{p[1]:.1f}" for p in reversed(bot_pts))
        d += " Z"
        return d

    def make_line_path(means):
        pts = [to_screen(s, m) for s, m in zip(steps, means)]
        return "M " + " L ".join(f"{p[0]:.1f},{p[1]:.1f}" for p in pts)

    base_band = make_band_path(base_mean, base_std)
    base_line = make_line_path(base_mean)

    prop_band = make_band_path(prop_mean, prop_std)
    prop_line = make_line_path(prop_mean)

    # Grid lines
    grid_lines = []
    for y_tick in [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5]:
        _, sy = to_screen(0, y_tick)
        grid_lines.append(
            f'<line x1="{pad_l}" y1="{sy:.1f}" x2="{w - pad_r}" y2="{sy:.1f}" stroke="rgba(255,255,255,0.08)" stroke-width="1" stroke-dasharray="4,4"/>'
        )
        grid_lines.append(
            f'<text x="{pad_l - 14}" y="{sy + 4:.1f}" fill="#64748B" font-family="monospace" font-size="12" text-anchor="end">{y_tick:.1f}</text>'
        )

    for x_tick in [0, 10, 20, 30, 40, 50]:
        sx, _ = to_screen(x_tick, 0)
        grid_lines.append(
            f'<line x1="{sx:.1f}" y1="{pad_t}" x2="{sx:.1f}" y2="{h - pad_b}" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>'
        )
        grid_lines.append(
            f'<text x="{sx:.1f}" y="{h - pad_b + 24}" fill="#64748B" font-family="monospace" font-size="12" text-anchor="middle">{x_tick}</text>'
        )

    return f"""
    <div style="background: #0d121f; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; padding: 22px; color: #FFFFFF; font-family: -apple-system, sans-serif;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
            <div>
                <div style="font-size: 16px; font-weight: 700; color: #F8FAFC;">{html.escape(title)}</div>
                <div style="font-size: 12.5px; color: #94A3B8; margin-top: 3px;">{html.escape(subtitle)}</div>
            </div>
            <div style="display: flex; gap: 16px; font-size: 12px; font-family: 'JetBrains Mono', monospace;">
                <span style="color: #64748B; display: flex; align-items: center; gap: 6px;">
                    <span style="width: 14px; height: 3px; background: #64748B; display: inline-block;"></span>
                    First-Order Baseline (O(1/√k))
                </span>
                <span style="color: #38BDF8; display: flex; align-items: center; gap: 6px;">
                    <span style="width: 14px; height: 3px; background: #38BDF8; display: inline-block;"></span>
                    Proposed Auto-Engine (O(1/k²))
                </span>
            </div>
        </div>

        <svg viewBox="0 0 {w} {h}" style="width: 100%; height: auto; display: block; background: #080C14; border-radius: 8px; border: 1px solid rgba(255,255,255,0.06);">
            <!-- Grid Lines -->
            {''.join(grid_lines)}

            <!-- Base Shaded Band & Curve -->
            <path d="{base_band}" fill="#64748B" opacity="0.18"/>
            <path d="{base_line}" fill="none" stroke="#94A3B8" stroke-width="2.5" stroke-dasharray="6,4"/>

            <!-- Proposed Shaded Band & Curve -->
            <path d="{prop_band}" fill="#38BDF8" opacity="0.22"/>
            <path d="{prop_line}" fill="none" stroke="#38BDF8" stroke-width="3.5" filter="drop-shadow(0 0 6px rgba(56,189,248,0.5))"/>

            <!-- Axes Lines -->
            <line x1="{pad_l}" y1="{h - pad_b}" x2="{w - pad_r}" y2="{h - pad_b}" stroke="#475569" stroke-width="1.5"/>
            <line x1="{pad_l}" y1="{pad_t}" x2="{pad_l}" y2="{h - pad_b}" stroke="#475569" stroke-width="1.5"/>

            <!-- Axis Labels -->
            <text x="{w / 2}" y="{h - 18}" fill="#94A3B8" font-size="13" font-family="-apple-system, sans-serif" text-anchor="middle" font-weight="600">{html.escape(x_label)}</text>
            <text x="24" y="{h / 2}" fill="#94A3B8" font-size="13" font-family="-apple-system, sans-serif" text-anchor="middle" font-weight="600" transform="rotate(-90 24 {h / 2})">{html.escape(y_label)}</text>
        </svg>
    </div>
    """


# ==============================================================================
# 4. ACADEMIC & RESEARCH PLOT: MULTI-METRIC RADAR CHART
# ==============================================================================
def render_multi_metric_radar(
    title: str = "Orthogonal Benchmark Radar Profile",
    subtitle: str = "Multi-criteria evaluation normalized against industry baseline standards",
    axes: list[str] = None,
    datasets: list[dict] = None,
) -> str:
    """
    Renders a multi-dimensional radar benchmark chart.
    """
    if axes is None:
        axes = [
            "Throughput (TFLOPS)",
            "Memory Efficiency",
            "Autograd Precision",
            "Kernel Fusion",
            "Ecosystem Extensibility",
        ]
    if datasets is None:
        datasets = [
            {
                "name": "Standard Naive Implementation",
                "values": [0.45, 0.40, 0.90, 0.30, 0.50],
                "color": "#94A3B8",
            },
            {
                "name": "Our Optimized Engine",
                "values": [0.92, 0.88, 0.98, 0.85, 0.90],
                "color": "#10B981",
            },
        ]

    w, h = 540, 480
    cx, cy = 270, 240
    radius = 160
    num_axes = len(axes)

    # Grid rings
    rings = []
    for level in [0.25, 0.5, 0.75, 1.0]:
        pts = []
        for i in range(num_axes):
            angle = (2 * math.pi * i / num_axes) - (math.pi / 2)
            rx = cx + radius * level * math.cos(angle)
            ry = cy + radius * level * math.sin(angle)
            pts.append((rx, ry))
        d = "M " + " L ".join(f"{p[0]:.1f},{p[1]:.1f}" for p in pts) + " Z"
        rings.append(
            f'<path d="{d}" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1.2"/>'
        )

    # Axis spokes and labels
    spokes = []
    labels = []
    for i, axis_label in enumerate(axes):
        angle = (2 * math.pi * i / num_axes) - (math.pi / 2)
        rx = cx + radius * math.cos(angle)
        ry = cy + radius * math.sin(angle)
        spokes.append(
            f'<line x1="{cx}" y1="{cy}" x2="{rx:.1f}" y2="{ry:.1f}" stroke="rgba(255,255,255,0.12)" stroke-width="1"/>'
        )

        lx = cx + (radius + 28) * math.cos(angle)
        ly = cy + (radius + 28) * math.sin(angle)
        anchor = (
            "middle"
            if abs(math.cos(angle)) < 0.2
            else ("start" if math.cos(angle) > 0 else "end")
        )
        labels.append(
            f'<text x="{lx:.1f}" y="{ly + 4:.1f}" fill="#CBD5E1" font-size="11.5" font-family="-apple-system, sans-serif" font-weight="600" text-anchor="{anchor}">{html.escape(axis_label)}</text>'
        )

    # Data Polygons
    data_polys = []
    for dset in datasets:
        pts = []
        for i, val in enumerate(dset["values"]):
            angle = (2 * math.pi * i / num_axes) - (math.pi / 2)
            px = cx + radius * val * math.cos(angle)
            py = cy + radius * val * math.sin(angle)
            pts.append((px, py))
        path_str = "M " + " L ".join(f"{p[0]:.1f},{p[1]:.1f}" for p in pts) + " Z"
        data_polys.append(
            f'<path d="{path_str}" fill="{dset["color"]}" fill-opacity="0.22" stroke="{dset["color"]}" stroke-width="2.5" />'
        )
        for p in pts:
            data_polys.append(
                f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="4" fill="{dset["color"]}" stroke="#080C14" stroke-width="1.5" />'
            )

    return f"""
    <div style="background: #0d121f; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; padding: 22px; color: #FFFFFF; font-family: -apple-system, sans-serif;">
        <div style="margin-bottom: 12px;">
            <div style="font-size: 15px; font-weight: 700; color: #F8FAFC;">{html.escape(title)}</div>
            <div style="font-size: 12px; color: #94A3B8; margin-top: 3px;">{html.escape(subtitle)}</div>
        </div>

        <svg viewBox="0 0 {w} {h}" style="width: 100%; height: auto; display: block; background: #080C14; border-radius: 8px; border: 1px solid rgba(255,255,255,0.06);">
            {''.join(rings)}
            {''.join(spokes)}
            {''.join(data_polys)}
            {''.join(labels)}
        </svg>
    </div>
    """


# ==============================================================================
# 5. TEACHABLE FIGURES: DYNAMIC RESERVOIR VALVE (Physical Intuition Model)
# ==============================================================================
def render_teachable_reservoir_valve(
    title: str = "Hydraulic Reservoir & Regulated Throttle (Teachable Model)",
    subtitle: str = "Physical mapping of gradient buffering, flow dissipation, and learning rate gating",
    reservoir_level_pct: int = 68,
    valve_aperture_pct: int = 42,
) -> str:
    """
    Renders a fluid dynamics intuition model (Teachable Figures paradigm).
    Abstract representation of fluid buffering and gated release.
    """
    w, h = 840, 480
    return f"""
    <div style="background: #0d121f; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; padding: 22px; color: #FFFFFF; font-family: -apple-system, sans-serif;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 16px;">
            <div>
                <div style="font-size: 16px; font-weight: 700; color: #F8FAFC;">{html.escape(title)}</div>
                <div style="font-size: 12.5px; color: #94A3B8; margin-top: 3px;">{html.escape(subtitle)}</div>
            </div>
            <div style="display: flex; gap: 12px;">
                <span style="background: rgba(56,189,248,0.15); border: 1px solid #38BDF8; color: #38BDF8; padding: 4px 10px; border-radius: 6px; font-size: 11.5px; font-weight: 600;">Reservoir: {reservoir_level_pct}%</span>
                <span style="background: rgba(245,158,11,0.15); border: 1px solid #F59E0B; color: #F59E0B; padding: 4px 10px; border-radius: 6px; font-size: 11.5px; font-weight: 600;">Throttle: {valve_aperture_pct}%</span>
            </div>
        </div>

        <svg viewBox="0 0 {w} {h}" style="width: 100%; height: auto; display: block; background: #080C14; border-radius: 8px; border: 1px solid rgba(255,255,255,0.06);">
            <!-- Inflow Pipe -->
            <rect x="80" y="80" width="160" height="42" fill="#1E293B" stroke="#475569" stroke-width="2"/>
            <text x="160" y="106" fill="#94A3B8" font-size="12" font-family="monospace" text-anchor="middle">INFLOW Q_in</text>
            <!-- Inflow Stream Flowing Down -->
            <path d="M 240 101 L 320 101 L 320 220" fill="none" stroke="#38BDF8" stroke-width="12" stroke-linecap="round" stroke-dasharray="10,6" opacity="0.85"/>

            <!-- Main Reservoir Tank -->
            <rect x="280" y="140" width="280" height="240" rx="8" fill="rgba(30,41,59,0.5)" stroke="#64748B" stroke-width="2.5"/>
            <!-- Liquid Level Inside Tank -->
            <rect x="284" y="{376 - (reservoir_level_pct * 2.2):.1f}" width="272" height="{reservoir_level_pct * 2.2:.1f}" fill="url(#liquidGrad)" rx="4"/>
            <!-- Liquid Level Measurement Markings -->
            <line x1="280" y1="200" x2="300" y2="200" stroke="#94A3B8" stroke-width="1.5"/>
            <line x1="280" y1="260" x2="300" y2="260" stroke="#94A3B8" stroke-width="1.5"/>
            <line x1="280" y1="320" x2="300" y2="320" stroke="#94A3B8" stroke-width="1.5"/>
            <text x="312" y="204" fill="#64748B" font-size="11" font-family="monospace">Capacity Max (C)</text>
            <text x="312" y="264" fill="#38BDF8" font-size="11" font-family="monospace">Working Level h(t)</text>
            <text x="312" y="324" fill="#64748B" font-size="11" font-family="monospace">Damping Margin</text>

            <!-- Throttle Gating Valve -->
            <rect x="560" y="320" width="120" height="42" fill="#1E293B" stroke="#475569" stroke-width="2"/>
            <!-- Valve Stem & Knob -->
            <line x1="620" y1="270" x2="620" y2="320" stroke="#F59E0B" stroke-width="4"/>
            <circle cx="620" cy="265" r="14" fill="#F59E0B"/>
            <text x="620" y="300" fill="#F59E0B" font-size="11" font-family="monospace" text-anchor="middle">α·∇L</text>

            <!-- Regulated Outflow Stream -->
            <path d="M 680 341 L 760 341" fill="none" stroke="#10B981" stroke-width="8" stroke-dasharray="8,4"/>
            <text x="720" y="325" fill="#10B981" font-size="12" font-family="monospace" text-anchor="middle">STABLE OUTFLOW</text>

            <defs>
                <linearGradient id="liquidGrad" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.8"/>
                    <stop offset="100%" stop-color="#6366F1" stop-opacity="0.95"/>
                </linearGradient>
            </defs>
        </svg>
    </div>
    """


# ==============================================================================
# 6. SYSTEM ARCHITECTURES: DUAL SYNCHRONIZED CODE & MEMORY INSPECTOR
# ==============================================================================
def render_dual_code_inspector(
    title: str = "Dual Code Execution & Dynamic Memory Topology Inspector",
    code_snippet: str = None,
    memory_slots: list[dict] = None,
    active_line: int = 4,
) -> str:
    """
    Renders a synchronized dual-pane inspection window:
    Left: Syntax highlighted source code with active execution pointer.
    Right: Live heap allocation and variable symbol table.
    """
    if code_snippet is None:
        code_snippet = (
            "class Value:\n"
            "    def __init__(self, data, _children=()):\n"
            "        self.data = float(data)\n"
            "        self.grad = 0.0\n"
            "        self._backward = lambda: None\n"
            "        self._prev = set(_children)\n\n"
            "    def __add__(self, other):\n"
            "        out = Value(self.data + other.data, (self, other))\n"
            "        def _backward():\n"
            "            self.grad += 1.0 * out.grad\n"
            "            other.grad += 1.0 * out.grad\n"
            "        out._backward = _backward\n"
            "        return out"
        )

    if memory_slots is None:
        memory_slots = [
            {
                "addr": "0x7f9a10",
                "var": "x",
                "val": "2.0000",
                "grad": "∂L/∂x = 6.00",
                "status": "ACCUMULATED",
            },
            {
                "addr": "0x7f9a28",
                "var": "w",
                "val": "-3.0000",
                "grad": "∂L/∂w = 4.00",
                "status": "ACCUMULATED",
            },
            {
                "addr": "0x7f9a40",
                "var": "b",
                "val": "0.5000",
                "grad": "∂L/∂b = 1.00",
                "status": "STEADY",
            },
            {
                "addr": "0x7f9a58",
                "var": "out",
                "val": "-5.5000",
                "grad": "∂L/∂out = 1.00",
                "status": "TERMINAL",
            },
        ]

    code_lines_html = []
    for idx, line in enumerate(code_snippet.splitlines(), start=1):
        is_active = idx == active_line
        bg = "background: rgba(99,102,241,0.22);" if is_active else ""
        border = (
            "border-left: 3px solid #38BDF8;"
            if is_active
            else "border-left: 3px solid transparent;"
        )
        code_lines_html.append(
            f'<div style="display: flex; gap: 14px; padding: 2px 8px; {bg} {border}">'
            f'<span style="color: #475569; width: 24px; text-align: right; user-select: none;">{idx}</span>'
            f'<span style="color: {"#FFFFFF" if is_active else "#CBD5E1"};">{html.escape(line)}</span>'
            f"</div>"
        )

    slot_rows_html = []
    for slot in memory_slots:
        status_val = slot.get("status", "ACTIVE")
        badge_col = "#10B981" if status_val == "ACCUMULATED" else "#38BDF8"
        var_name = slot.get("var", slot.get("name", "v"))
        addr_val = slot.get("addr", "0xHEAP")
        val_str = slot.get("val", "0.0")
        grad_str = slot.get("grad", "")
        grad_span = f'<span style="color: #38BDF8;">{grad_str}</span>' if grad_str else ""
        slot_rows_html.append(
            f'<div style="background: rgba(30,41,59,0.6); border: 1px solid rgba(255,255,255,0.08); border-radius: 6px; padding: 10px 14px; margin-bottom: 8px;">'
            f'<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">'
            f'<span style="font-family: monospace; font-weight: 700; color: #F8FAFC; font-size: 13px;">{var_name} <span style="color: #64748B; font-weight: 400;">({addr_val})</span></span>'
            f'<span style="font-size: 11px; padding: 2px 8px; border-radius: 4px; background: {badge_col}22; color: {badge_col}; font-weight: 700;">{status_val}</span>'
            f"</div>"
            f'<div style="display: flex; justify-content: space-between; font-family: monospace; font-size: 12px; color: #94A3B8;">'
            f'<span>data: <strong style="color: #FFFFFF;">{val_str}</strong></span>'
            f'{grad_span}'
            f"</div>"
            f"</div>"
        )

    return f"""
    <div style="background: #0d121f; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; padding: 22px; color: #FFFFFF; font-family: -apple-system, sans-serif;">
        <div style="font-size: 16px; font-weight: 700; color: #F8FAFC; margin-bottom: 14px;">{html.escape(title)}</div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 18px;">
            <!-- Left Pane: Code -->
            <div style="background: #080C14; border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 14px; font-family: 'JetBrains Mono', monospace; font-size: 12px; line-height: 1.6; overflow-x: auto;">
                <div style="color: #64748B; font-size: 11px; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 6px; margin-bottom: 8px;">SOURCE RUNTIME EXECUTION</div>
                {''.join(code_lines_html)}
            </div>

            <!-- Right Pane: Memory State -->
            <div style="background: #080C14; border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 14px;">
                <div style="color: #64748B; font-size: 11px; font-family: 'JetBrains Mono', monospace; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 6px; margin-bottom: 10px;">DYNAMIC HEAP ALLOCATIONS & TOPOLOGY</div>
                {''.join(slot_rows_html)}
            </div>
        </div>
    </div>
    """


# ==============================================================================
# 7. MULTI-LAYOUT ASSEMBLY CONTAINERS (6 DIVERSE ARCHITECTURES)
# ==============================================================================
def render_top_formula_bottom_dynamic_layout(
    scene_kicker: str,
    scene_title: str,
    formula_latex: str,
    formula_explanation: str,
    dynamic_component_html: str,
) -> str:
    """
    Layout 2: Top mathematical theorem card (35% height) + Bottom dynamic visual manifold (65% height).
    """
    return f"""
    <div class="scene-layout-container" style="
        width: 1920px; height: 1080px; background: #080C14; color: #FFFFFF;
        display: flex; flex-direction: column; padding: 60px 100px; box-sizing: border-box;
        font-family: -apple-system, BlinkMacSystemFont, 'Inter', sans-serif;
    ">
        <!-- Scene Header -->
        <div style="margin-bottom: 24px;">
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 13px; font-weight: 700; color: #38BDF8; letter-spacing: 1px; text-transform: uppercase;">
                {html.escape(scene_kicker)}
            </div>
            <div style="font-size: 34px; font-weight: 800; color: #F8FAFC; margin-top: 4px;">
                {html.escape(scene_title)}
            </div>
        </div>

        <!-- Top Formula Card -->
        <div style="background: rgba(30,41,59,0.5); border: 1.5px solid rgba(99,102,241,0.3); border-radius: 12px; padding: 20px 28px; margin-bottom: 24px; display: flex; justify-content: space-between; align-items: center;">
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 24px; font-weight: 700; color: #38BDF8; letter-spacing: 0.5px;">
                {html.escape(formula_latex)}
            </div>
            <div style="font-size: 15px; color: #CBD5E1; max-width: 820px; line-height: 1.5; border-left: 2px solid #6366F1; padding-left: 18px;">
                {html.escape(formula_explanation)}
            </div>
        </div>

        <!-- Bottom Dynamic Component Canvas -->
        <div style="flex: 1; display: flex; flex-direction: column;">
            {dynamic_component_html}
        </div>
    </div>
    """


def render_quad_comparison_layout(
    scene_kicker: str, scene_title: str, quad_cards: list[dict]
) -> str:
    """
    Layout 3: 2x2 Quad Ablation/Experiment Matrix.
    quad_cards = [{ title, badge, desc, stat_val, stat_label, color }]
    """
    card_htmls = []
    for c in quad_cards:
        col = c.get("color", "#38BDF8")
        card_htmls.append(
            f"""
        <div style="background: #0d121f; border: 1px solid rgba(255,255,255,0.08); border-top: 4px solid {col}; border-radius: 10px; padding: 24px; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <span style="font-size: 18px; font-weight: 700; color: #FFFFFF;">{html.escape(c["title"])}</span>
                    <span style="font-size: 11px; padding: 3px 8px; border-radius: 4px; background: {col}22; color: {col}; font-weight: 700;">{html.escape(c["badge"])}</span>
                </div>
                <p style="font-size: 13.5px; color: #94A3B8; line-height: 1.5; margin: 0 0 16px 0;">{html.escape(c["desc"])}</p>
            </div>
            <div style="border-top: 1px solid rgba(255,255,255,0.06); padding-top: 12px; display: flex; justify-content: space-between; align-items: baseline;">
                <span style="font-size: 12px; color: #64748B;">{html.escape(c["stat_label"])}</span>
                <span style="font-family: 'JetBrains Mono', monospace; font-size: 26px; font-weight: 800; color: {col};">{html.escape(c["stat_val"])}</span>
            </div>
        </div>
        """
        )

    return f"""
    <div class="scene-layout-container" style="
        width: 1920px; height: 1080px; background: #080C14; color: #FFFFFF;
        display: flex; flex-direction: column; padding: 60px 100px; box-sizing: border-box;
        font-family: -apple-system, BlinkMacSystemFont, 'Inter', sans-serif;
    ">
        <div style="margin-bottom: 28px;">
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 13px; font-weight: 700; color: #38BDF8; letter-spacing: 1px; text-transform: uppercase;">
                {html.escape(scene_kicker)}
            </div>
            <div style="font-size: 34px; font-weight: 800; color: #F8FAFC; margin-top: 4px;">
                {html.escape(scene_title)}
            </div>
        </div>

        <div style="flex: 1; display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 24px;">
            {''.join(card_htmls)}
        </div>
    </div>
    """

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


# ==============================================================================
# SECTION 7: MULTI-DISCIPLINARY SCIENTIFIC & ALGORITHMIC VISUALIZATIONS
# (Researched & Verified via Grok 4.7 Heavy Survey across Qiskit, Control, PyG, WebLogo, DAG)
# ==============================================================================

def render_quantum_bloch_circuit(
    vector: tuple[float, float, float] = (0.35, 0.61, 0.71),
    theta_deg: float = 45.0,
    phi_deg: float = 60.0,
    circuit_gates: list[dict] = None,
    title: str = "QUANTUM STATE BLOCH SPHERE & CIRCUIT TELEMETRY",
    subtitle: str = "Pure Qubit State Manifold |ψ⟩ = cos(θ/2)|0⟩ + e^(iφ)sin(θ/2)|1⟩ with Unitary Transform",
    width: int = 860,
    height: int = 520,
) -> str:
    """
    Renders a synchronized dual-pane Quantum State visualizer:
    Left: Isometric 3D Bloch Sphere with spherical projection ellipses, basis poles |0⟩, |1⟩, |+⟩, |-⟩,
          and glowing state vector |ψ⟩ with θ, φ angular arcs.
    Right: Multi-qubit circuit wire diagram with styled unitary gates (H, X, Rz, CNOT, Measure).
    Styled under Qiskit 'iqp-dark' official color palette.
    """
    if circuit_gates is None:
        circuit_gates = [
            {"qubit": 0, "col": 0, "gate": "H", "type": "hadamard"},
            {"qubit": 0, "col": 1, "gate": "Rz(π/4)", "type": "phase"},
            {"qubit": 1, "col": 1, "gate": "X", "type": "pauli"},
            {"qubit": 0, "col": 2, "gate": "●", "target": 1, "type": "cnot"},
            {"qubit": 0, "col": 3, "gate": "M", "type": "measure"},
            {"qubit": 1, "col": 3, "gate": "M", "type": "measure"}
        ]

    bx, by, bz = vector
    cx, cy, r = 180, 240, 130
    vx = cx + r * (bx * 0.866 - by * 0.5)
    vy = cy - r * bz + (by * 0.25) * r

    num_qubits = 2
    col_width = 70
    start_x = 420
    circuit_svg = []
    
    for q in range(num_qubits):
        qy = 180 + q * 80
        circuit_svg.append(f'<line x1="{start_x}" y1="{qy}" x2="{start_x + 380}" y2="{qy}" stroke="#64748B" stroke-width="1.5"/>')
        circuit_svg.append(f'<text x="{start_x - 30}" y="{qy + 4}" fill="#38BDF8" font-family="monospace" font-size="12" font-weight="700">|q{q}⟩</text>')
        circuit_svg.append(f'<line x1="{start_x}" y1="{qy + 2}" x2="{start_x + 380}" y2="{qy + 2}" stroke="#334155" stroke-width="1" stroke-dasharray="2,2"/>')

    for g in circuit_gates:
        q = g.get("qubit", 0)
        col = g.get("col", 0)
        gx = start_x + 40 + col * col_width
        gy = 180 + q * 80
        gtype = g.get("type", "generic")
        gate_name = g.get("gate", "U")

        if gtype == "hadamard":
            circuit_svg.append(f'<rect x="{gx-18}" y="{gy-18}" width="36" height="36" rx="4" fill="#FA4D56" stroke="#FFA39E" stroke-width="1"/>')
            circuit_svg.append(f'<text x="{gx}" y="{gy+5}" fill="#FFFFFF" font-family="monospace" font-size="12" font-weight="800" text-anchor="middle">H</text>')
        elif gtype == "pauli":
            circuit_svg.append(f'<rect x="{gx-18}" y="{gy-18}" width="36" height="36" rx="4" fill="#4589FF" stroke="#A6C8FF" stroke-width="1"/>')
            circuit_svg.append(f'<text x="{gx}" y="{gy+5}" fill="#FFFFFF" font-family="monospace" font-size="12" font-weight="800" text-anchor="middle">X</text>')
        elif gtype == "phase":
            circuit_svg.append(f'<rect x="{gx-24}" y="{gy-18}" width="48" height="36" rx="4" fill="#FF7EB6" stroke="#FFD6E8" stroke-width="1"/>')
            circuit_svg.append(f'<text x="{gx}" y="{gy+5}" fill="#161616" font-family="monospace" font-size="10" font-weight="800" text-anchor="middle">{html.escape(gate_name)}</text>')
        elif gtype == "cnot":
            tgt_q = g.get("target", 1)
            tgt_y = 180 + tgt_q * 80
            circuit_svg.append(f'<line x1="{gx}" y1="{gy}" x2="{gx}" y2="{tgt_y}" stroke="#38BDF8" stroke-width="2"/>')
            circuit_svg.append(f'<circle cx="{gx}" cy="{gy}" r="5" fill="#38BDF8"/>')
            circuit_svg.append(f'<circle cx="{gx}" cy="{tgt_y}" r="12" fill="none" stroke="#38BDF8" stroke-width="2"/>')
            circuit_svg.append(f'<line x1="{gx-8}" y1="{tgt_y}" x2="{gx+8}" y2="{tgt_y}" stroke="#38BDF8" stroke-width="2"/>')
            circuit_svg.append(f'<line x1="{gx}" y1="{tgt_y-8}" x2="{gx}" y2="{tgt_y+8}" stroke="#38BDF8" stroke-width="2"/>')
        elif gtype == "measure":
            circuit_svg.append(f'<rect x="{gx-16}" y="{gy-16}" width="32" height="32" rx="4" fill="#1E293B" stroke="#64748B" stroke-width="1.5"/>')
            circuit_svg.append(f'<path d="M{gx-10},{gy+8} A12,12 0 0,1 {gx+10},{gy+8} M{gx},{gy+8} L{gx+7},{gy-6}" fill="none" stroke="#F8FAFC" stroke-width="1.5"/>')

    return f"""
    <div style="background: #090D16; border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 24px; color: #FFFFFF; font-family: -apple-system, sans-serif; width: {width}px; height: {height}px; box-sizing: border-box; position: relative;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
            <div>
                <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #FA4D56; font-weight: 700; letter-spacing: 1px;">QISKIT UNIFIED QUANTUM SPECIFICATION // v1.2</div>
                <div style="font-size: 16px; font-weight: 800; color: #F8FAFC; margin-top: 2px;">{html.escape(title)}</div>
                <div style="font-size: 11px; color: #94A3B8; margin-top: 2px;">{html.escape(subtitle)}</div>
            </div>
            <div style="display: flex; gap: 8px;">
                <span style="background: rgba(250,77,86,0.15); border: 1px solid #FA4D56; color: #FA4D56; font-size: 10px; font-family: monospace; padding: 2px 8px; border-radius: 4px; font-weight: 700;">|ψ⟩ = [{bx:.2f}, {by:.2f}, {bz:.2f}]</span>
                <span style="background: rgba(69,137,255,0.15); border: 1px solid #4589FF; color: #4589FF; font-size: 10px; font-family: monospace; padding: 2px 8px; border-radius: 4px; font-weight: 700;">θ={theta_deg}° φ={phi_deg}°</span>
            </div>
        </div>

        <svg viewBox="0 0 820 420" style="width: 100%; height: 420px; overflow: visible;">
            <!-- LEFT: 3D BLOCH SPHERE -->
            <g id="bloch-sphere">
                <circle cx="{cx}" cy="{cy}" r="{r}" fill="#0D1527" stroke="#334155" stroke-width="1.5"/>
                <ellipse cx="{cx}" cy="{cy}" rx="{r}" ry="{r*0.35}" fill="none" stroke="#475569" stroke-width="1" stroke-dasharray="4,4"/>
                <ellipse cx="{cx}" cy="{cy}" rx="{r*0.35}" ry="{r}" fill="none" stroke="#475569" stroke-width="1" stroke-dasharray="4,4"/>
                
                <line x1="{cx}" y1="{cy+r+15}" x2="{cx}" y2="{cy-r-15}" stroke="#94A3B8" stroke-width="1.5"/>
                <line x1="{cx-r-15}" y1="{cy}" x2="{cx+r+15}" y2="{cy}" stroke="#64748B" stroke-width="1"/>
                <line x1="{cx-r*0.6}" y1="{cy+r*0.4}" x2="{cx+r*0.6}" y2="{cy-r*0.4}" stroke="#64748B" stroke-width="1"/>
                
                <text x="{cx}" y="{cy-r-22}" fill="#F8FAFC" font-family="monospace" font-size="12" font-weight="700" text-anchor="middle">|0⟩ (+z)</text>
                <text x="{cx}" y="{cy+r+28}" fill="#F8FAFC" font-family="monospace" font-size="12" font-weight="700" text-anchor="middle">|1⟩ (-z)</text>
                <text x="{cx+r+22}" y="{cy+4}" fill="#94A3B8" font-family="monospace" font-size="11">+y</text>
                <text x="{cx-r*0.6-18}" y="{cy+r*0.4+12}" fill="#94A3B8" font-family="monospace" font-size="11">+x</text>

                <line x1="{cx}" y1="{cy}" x2="{vx}" y2="{vy}" stroke="#38BDF8" stroke-width="3"/>
                <circle cx="{vx}" cy="{vy}" r="5" fill="#38BDF8"/>
                <text x="{vx+10}" y="{vy-6}" fill="#38BDF8" font-family="monospace" font-size="13" font-weight="800">|ψ⟩</text>
                <line x1="{vx}" y1="{vy}" x2="{vx}" y2="{cy + (vy-cy)*0.3}" stroke="#38BDF8" stroke-width="1" stroke-dasharray="2,2"/>
                <circle cx="{vx}" cy="{cy + (vy-cy)*0.3}" r="3" fill="#64748B"/>
            </g>

            <!-- RIGHT: QUANTUM CIRCUIT -->
            <g id="quantum-circuit">
                <rect x="380" y="80" width="430" height="310" rx="8" fill="rgba(15,23,42,0.4)" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>
                <text x="400" y="110" fill="#94A3B8" font-family="monospace" font-size="11" font-weight="700">CIRCUIT EXECUTION MATRIX // DEPTH: 4</text>
                {''.join(circuit_svg)}
                
                <g transform="translate(400, 320)">
                    <rect width="390" height="50" rx="6" fill="#0B132B" stroke="#1E293B" stroke-width="1"/>
                    <text x="14" y="22" fill="#64748B" font-family="monospace" font-size="10">FIDELITY: 99.84%</text>
                    <text x="14" y="38" fill="#64748B" font-family="monospace" font-size="10">ENTANGLEMENT: BELL-PAIR (|Φ+⟩)</text>
                    <text x="230" y="22" fill="#10B981" font-family="monospace" font-size="10">SHOTS: 8192</text>
                    <text x="230" y="38" fill="#38BDF8" font-family="monospace" font-size="10">BACKEND: AER_SIMULATOR</text>
                </g>
            </g>
        </svg>
    </div>
    """


def render_bode_nyquist_frequency_plot(
    title: str = "BODE FREQUENCY RESPONSE & NYQUIST STABILITY CRITERIA",
    subtitle: str = "Logarithmic Gain/Phase Margins with Complex Nyquist Contour Encircling (-1, 0)",
    gain_margin_db: float = 14.2,
    phase_margin_deg: float = 48.6,
    width: int = 860,
    height: int = 520,
) -> str:
    """
    Renders a unified Classical Control Frequency Response layout:
    Left: Dual-decker Bode plot (Top: Magnitude in dB; Bottom: Phase in degrees) with 0dB gain crossover and -180° phase crossover.
    Right: Complex s-plane Nyquist plot with unit circle, critical point (-1, 0), and gain/phase margin indicators.
    Follows Python-Control and IEEE Control Systems Society conventions.
    """
    bode_pts_mag = [(60, 80), (120, 85), (200, 110), (280, 160), (360, 220)]
    bode_pts_phase = [(60, 260), (120, 275), (200, 320), (280, 390), (360, 420)]
    
    bode_mag_str = " ".join(f"{x},{y}" for x, y in bode_pts_mag)
    bode_phase_str = " ".join(f"{x},{y}" for x, y in bode_pts_phase)

    ncx, ncy, nr = 620, 240, 100

    return f"""
    <div style="background: #080C14; border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 24px; color: #FFFFFF; font-family: -apple-system, sans-serif; width: {width}px; height: {height}px; box-sizing: border-box;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
            <div>
                <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #38BDF8; font-weight: 700; letter-spacing: 1px;">FREQUENCY DOMAIN TELEMETRY // PYTHON-CONTROL SPEC</div>
                <div style="font-size: 16px; font-weight: 800; color: #F8FAFC; margin-top: 2px;">{html.escape(title)}</div>
                <div style="font-size: 11px; color: #94A3B8; margin-top: 2px;">{html.escape(subtitle)}</div>
            </div>
            <div style="display: flex; gap: 8px;">
                <span style="background: rgba(16,185,129,0.15); border: 1px solid #10B981; color: #10B981; font-size: 10px; font-family: monospace; padding: 2px 8px; border-radius: 4px; font-weight: 700;">GM: +{gain_margin_db} dB</span>
                <span style="background: rgba(56,189,248,0.15); border: 1px solid #38BDF8; color: #38BDF8; font-size: 10px; font-family: monospace; padding: 2px 8px; border-radius: 4px; font-weight: 700;">PM: {phase_margin_deg}°</span>
            </div>
        </div>

        <svg viewBox="0 0 820 420" style="width: 100%; height: 420px; overflow: visible;">
            <!-- LEFT: BODE MAGNITUDE & PHASE -->
            <g id="bode-panel">
                <rect x="40" y="40" width="360" height="180" fill="#0B132B" stroke="#1E293B" stroke-width="1"/>
                <rect x="40" y="235" width="360" height="175" fill="#0B132B" stroke="#1E293B" stroke-width="1"/>
                
                <line x1="40" y1="130" x2="400" y2="130" stroke="#475569" stroke-width="1" stroke-dasharray="3,3"/>
                <text x="35" y="134" fill="#94A3B8" font-family="monospace" font-size="10" text-anchor="end">0 dB</text>
                <text x="35" y="60" fill="#64748B" font-family="monospace" font-size="10" text-anchor="end">+40</text>
                <text x="35" y="200" fill="#64748B" font-family="monospace" font-size="10" text-anchor="end">-40</text>
                <text x="50" y="58" fill="#38BDF8" font-family="monospace" font-size="11" font-weight="700">MAGNITUDE |G(jω)|</text>

                <polyline points="{bode_mag_str}" fill="none" stroke="#38BDF8" stroke-width="2.5"/>
                <circle cx="240" cy="130" r="4" fill="#38BDF8"/>
                <line x1="240" y1="130" x2="240" y2="350" stroke="#38BDF8" stroke-width="1" stroke-dasharray="2,2"/>
                <text x="246" y="125" fill="#38BDF8" font-family="monospace" font-size="10">ω_gc = 12.4 rad/s</text>

                <line x1="40" y1="325" x2="400" y2="325" stroke="#475569" stroke-width="1" stroke-dasharray="3,3"/>
                <text x="35" y="329" fill="#FA4D56" font-family="monospace" font-size="10" text-anchor="end">-180°</text>
                <text x="35" y="255" fill="#64748B" font-family="monospace" font-size="10" text-anchor="end">0°</text>
                <text x="35" y="395" fill="#64748B" font-family="monospace" font-size="10" text-anchor="end">-270°</text>
                <text x="50" y="253" fill="#818CF8" font-family="monospace" font-size="11" font-weight="700">PHASE ∠G(jω)</text>

                <polyline points="{bode_phase_str}" fill="none" stroke="#818CF8" stroke-width="2.5"/>
                <circle cx="280" cy="390" r="4" fill="#818CF8"/>
                <line x1="240" y1="325" x2="240" y2="350" stroke="#10B981" stroke-width="3"/>
                <text x="246" y="342" fill="#10B981" font-family="monospace" font-size="10" font-weight="700">PM={phase_margin_deg}°</text>
            </g>

            <!-- RIGHT: NYQUIST CONTOUR -->
            <g id="nyquist-panel">
                <rect x="430" y="40" width="370" height="370" rx="8" fill="#0B132B" stroke="#1E293B" stroke-width="1"/>
                <text x="450" y="66" fill="#F8FAFC" font-family="monospace" font-size="12" font-weight="700">NYQUIST COMPLEX s-PLANE</text>
                
                <line x1="{ncx-140}" y1="{ncy}" x2="{ncx+140}" y2="{ncy}" stroke="#475569" stroke-width="1"/>
                <line x1="{ncx}" y1="{ncy-140}" x2="{ncx}" y2="{ncy+140}" stroke="#475569" stroke-width="1"/>
                <text x="{ncx+145}" y="{ncy+4}" fill="#64748B" font-family="monospace" font-size="10">Re</text>
                <text x="{ncx+4}" y="{ncy-145}" fill="#64748B" font-family="monospace" font-size="10">Im</text>

                <circle cx="{ncx}" cy="{ncy}" r="{nr}" fill="none" stroke="#334155" stroke-width="1" stroke-dasharray="4,4"/>
                <text x="{ncx+nr-12}" y="{ncy+16}" fill="#475569" font-family="monospace" font-size="10">|s|=1</text>

                <circle cx="{ncx-nr}" cy="{ncy}" r="5" fill="#FA4D56"/>
                <text x="{ncx-nr-14}" y="{ncy-10}" fill="#FA4D56" font-family="monospace" font-size="11" font-weight="800">(-1, 0)</text>

                <path d="M{ncx+70},{ncy+110} C{ncx+120},{ncy+40} {ncx-20},{ncy-60} {ncx-65},{ncy-15}" fill="none" stroke="#38BDF8" stroke-width="2.5"/>
                <path d="M{ncx+70},{ncy-110} C{ncx+120},{ncy-40} {ncx-20},{ncy+60} {ncx-65},{ncy+15}" fill="none" stroke="#38BDF8" stroke-width="1.5" stroke-dasharray="3,3" opacity="0.6"/>

                <line x1="{ncx-nr}" y1="{ncy}" x2="{ncx-65}" y2="{ncy}" stroke="#10B981" stroke-width="2"/>
                <text x="{ncx-nr+10}" y="{ncy+16}" fill="#10B981" font-family="monospace" font-size="9" font-weight="700">1/GM</text>

                <text x="450" y="390" fill="#10B981" font-family="monospace" font-size="11" font-weight="700">✓ ASYMPTOTICALLY STABLE (N=0)</text>
            </g>
        </svg>
    </div>
    """


def render_graph_network_topology(
    nodes: list[dict] = None,
    edges: list[dict] = None,
    title: str = "GRAPH NEURAL NETWORK MESSAGE-PASSING TOPOLOGY",
    subtitle: str = "Heterogeneous Node Feature Aggregation & Directed Spatial Message Passing",
    width: int = 860,
    height: int = 520,
) -> str:
    """
    Renders a Graph Neural Network / Knowledge Graph topology:
    - Hub nodes with radiant halos
    - Directed curved edges with message aggregation flow arrows
    - Node cluster groupings (color-coded) and telemetry attributes
    Follows NetworkX, PyTorch Geometric, and Graphviz visual conventions.
    """
    if nodes is None:
        nodes = [
            {"id": "h0", "label": "Hub-0", "x": 220, "y": 180, "size": 26, "color": "#38BDF8", "group": "Cluster A"},
            {"id": "n1", "label": "Embed-1", "x": 130, "y": 90, "size": 16, "color": "#818CF8", "group": "Cluster A"},
            {"id": "n2", "label": "Embed-2", "x": 110, "y": 270, "size": 18, "color": "#818CF8", "group": "Cluster A"},
            {"id": "h1", "label": "Hub-1", "x": 580, "y": 160, "size": 28, "color": "#10B981", "group": "Cluster B"},
            {"id": "n3", "label": "Embed-3", "x": 680, "y": 90, "size": 16, "color": "#34D399", "group": "Cluster B"},
            {"id": "n4", "label": "Embed-4", "x": 710, "y": 260, "size": 18, "color": "#34D399", "group": "Cluster B"},
            {"id": "c0", "label": "Bridge", "x": 390, "y": 280, "size": 22, "color": "#F59E0B", "group": "Transit"}
        ]

    if edges is None:
        edges = [
            {"src": "n1", "tgt": "h0", "weight": 0.85},
            {"src": "n2", "tgt": "h0", "weight": 0.72},
            {"src": "h0", "tgt": "c0", "weight": 0.94},
            {"src": "c0", "tgt": "h1", "weight": 0.91},
            {"src": "h1", "tgt": "n3", "weight": 0.78},
            {"src": "h1", "tgt": "n4", "weight": 0.82},
            {"src": "h0", "tgt": "h1", "weight": 0.65}
        ]

    node_dict = {n["id"]: n for n in nodes}
    edge_svg = []
    for e in edges:
        s = node_dict[e["src"]]
        t = node_dict[e["tgt"]]
        alpha = max(0.25, min(1.0, e.get("weight", 0.5)))
        edge_svg.append(
            f'<path d="M{s["x"]},{s["y"]} Q{(s["x"]+t["x"])/2},{(s["y"]+t["y"])/2 - 15} {t["x"]},{t["y"]}" '
            f'fill="none" stroke="#64748B" stroke-width="2" stroke-opacity="{alpha}"/>'
        )

    node_svg = []
    for n in nodes:
        col = n["color"]
        r = n["size"]
        node_svg.append(f'<circle cx="{n["x"]}" cy="{n["y"]}" r="{r*1.5}" fill="{col}" opacity="0.1"/>')
        node_svg.append(f'<circle cx="{n["x"]}" cy="{n["y"]}" r="{r}" fill="#0F172A" stroke="{col}" stroke-width="2.5"/>')
        node_svg.append(f'<text x="{n["x"]}" y="{n["y"]+4}" fill="#F8FAFC" font-family="monospace" font-size="11" font-weight="700" text-anchor="middle">{n["label"]}</text>')

    return f"""
    <div style="background: #080C14; border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 24px; color: #FFFFFF; font-family: -apple-system, sans-serif; width: {width}px; height: {height}px; box-sizing: border-box;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
            <div>
                <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #10B981; font-weight: 700; letter-spacing: 1px;">GRAPH REPRESENTATION LEARNING // PYG & NETWORKX</div>
                <div style="font-size: 16px; font-weight: 800; color: #F8FAFC; margin-top: 2px;">{html.escape(title)}</div>
                <div style="font-size: 11px; color: #94A3B8; margin-top: 2px;">{html.escape(subtitle)}</div>
            </div>
            <div style="display: flex; gap: 8px;">
                <span style="background: rgba(56,189,248,0.15); border: 1px solid #38BDF8; color: #38BDF8; font-size: 10px; font-family: monospace; padding: 2px 8px; border-radius: 4px; font-weight: 700;">NODES: {len(nodes)}</span>
                <span style="background: rgba(16,185,129,0.15); border: 1px solid #10B981; color: #10B981; font-size: 10px; font-family: monospace; padding: 2px 8px; border-radius: 4px; font-weight: 700;">EDGES: {len(edges)}</span>
            </div>
        </div>

        <svg viewBox="0 0 820 400" style="width: 100%; height: 400px; overflow: visible;">
            <rect width="820" height="400" rx="8" fill="#0B132B" stroke="#1E293B" stroke-width="1"/>
            {''.join(edge_svg)}
            {''.join(node_svg)}
            
            <g transform="translate(30, 360)">
                <circle cx="10" cy="10" r="6" fill="#38BDF8"/>
                <text x="24" y="14" fill="#94A3B8" font-family="monospace" font-size="10">Cluster A (Sensory)</text>
                <circle cx="170" cy="10" r="6" fill="#10B981"/>
                <text x="184" y="14" fill="#94A3B8" font-family="monospace" font-size="10">Cluster B (Motor)</text>
                <circle cx="330" cy="10" r="6" fill="#F59E0B"/>
                <text x="344" y="14" fill="#94A3B8" font-family="monospace" font-size="10">Bridge (Latent Alignment)</text>
            </g>
        </svg>
    </div>
    """


def render_genomic_sequence_ribbon(
    logo_columns: list[dict] = None,
    features: list[dict] = None,
    title: str = "GENOMIC SEQUENCE MOTIF & FEATURE TRACK TOPOLOGY",
    subtitle: str = "Information-Theoretic Sequence Logo (Bits) & Annotated Genomic Open Reading Frames",
    width: int = 860,
    height: int = 520,
) -> str:
    """
    Renders a unified Bioinformatics Sequence & Genome Feature view:
    Top: WebLogo style information-entropy letter stack (A: #3CB44A, C: #3D5AFE, G: #FF9F1C, T: #E10600)
         measured in 0 - 2.0 bits.
    Bottom: DNA Features Viewer linear genomic track showing CDS, promoters, and terminators with directional arrows.
    Follows Biopython, WebLogo, and genome browser standards.
    """
    if logo_columns is None:
        logo_columns = [
            {"pos": 1, "bits": 1.85, "stack": [("T", 1.45), ("A", 0.25), ("C", 0.15)]},
            {"pos": 2, "bits": 1.95, "stack": [("A", 1.80), ("G", 0.15)]},
            {"pos": 3, "bits": 1.20, "stack": [("T", 0.80), ("A", 0.30), ("C", 0.10)]},
            {"pos": 4, "bits": 1.70, "stack": [("A", 1.50), ("T", 0.20)]},
            {"pos": 5, "bits": 1.92, "stack": [("A", 1.75), ("T", 0.17)]},
            {"pos": 6, "bits": 1.88, "stack": [("T", 1.65), ("A", 0.23)]},
            {"pos": 7, "bits": 0.65, "stack": [("C", 0.30), ("G", 0.20), ("A", 0.15)]},
            {"pos": 8, "bits": 1.40, "stack": [("G", 1.10), ("C", 0.30)]}
        ]

    if features is None:
        features = [
            {"start": 60, "end": 200, "strand": 1, "type": "Promoter (TATA)", "color": "#38BDF8"},
            {"start": 220, "end": 580, "strand": 1, "type": "CDS (Kinase Exon 1)", "color": "#10B981"},
            {"start": 600, "end": 740, "strand": -1, "type": "Terminator (PolyA)", "color": "#F59E0B"}
        ]

    color_map = {"A": "#3CB44A", "C": "#3D5AFE", "G": "#FF9F1C", "T": "#E10600"}
    logo_svg = []
    
    for idx, col in enumerate(logo_columns):
        cx = 100 + idx * 80
        total_bits = col["bits"]
        y_accum = 210
        for char, char_bits in col["stack"]:
            h = (char_bits / 2.0) * 160
            y_accum -= h
            c = color_map.get(char, "#FFFFFF")
            logo_svg.append(f'<text x="{cx}" y="{y_accum + h*0.88}" fill="{c}" font-family="Impact, sans-serif" font-size="{max(12, int(h*1.1))}" font-weight="900" text-anchor="middle">{char}</text>')
        logo_svg.append(f'<text x="{cx}" y="{232}" fill="#64748B" font-family="monospace" font-size="11" text-anchor="middle">{col["pos"]}</text>')

    feature_svg = []
    for f in features:
        x1 = f["start"]
        x2 = f["end"]
        col = f["color"]
        strand = f["strand"]
        arrow_w = 16
        if strand == 1:
            poly = f"{x1},310 {x2-arrow_w},310 {x2},325 {x2-arrow_w},340 {x1},340"
        else:
            poly = f"{x1+arrow_w},310 {x2},310 {x2},340 {x1+arrow_w},340 {x1},325"
        feature_svg.append(f'<polygon points="{poly}" fill="{col}33" stroke="{col}" stroke-width="2"/>')
        feature_svg.append(f'<text x="{(x1+x2)/2}" y="329" fill="#F8FAFC" font-family="monospace" font-size="11" font-weight="700" text-anchor="middle">{html.escape(f["type"])}</text>')

    return f"""
    <div style="background: #080C14; border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 24px; color: #FFFFFF; font-family: -apple-system, sans-serif; width: {width}px; height: {height}px; box-sizing: border-box;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
            <div>
                <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #3CB44A; font-weight: 700; letter-spacing: 1px;">COMPUTATIONAL GENOMICS // WEBLOGO & BIOPYTHON</div>
                <div style="font-size: 16px; font-weight: 800; color: #F8FAFC; margin-top: 2px;">{html.escape(title)}</div>
                <div style="font-size: 11px; color: #94A3B8; margin-top: 2px;">{html.escape(subtitle)}</div>
            </div>
            <div style="display: flex; gap: 8px;">
                <span style="background: rgba(60,180,74,0.15); border: 1px solid #3CB44A; color: #3CB44A; font-size: 10px; font-family: monospace; padding: 2px 8px; border-radius: 4px; font-weight: 700;">ENTROPY: 1.84 BITS</span>
                <span style="background: rgba(61,90,254,0.15); border: 1px solid #3D5AFE; color: #3D5AFE; font-size: 10px; font-family: monospace; padding: 2px 8px; border-radius: 4px; font-weight: 700;">MOTIF: TATA-BOX</span>
            </div>
        </div>

        <svg viewBox="0 0 820 400" style="width: 100%; height: 400px; overflow: visible;">
            <rect x="40" y="40" width="740" height="200" fill="#0B132B" stroke="#1E293B" stroke-width="1"/>
            <line x1="80" y1="210" x2="760" y2="210" stroke="#475569" stroke-width="1.5"/>
            <line x1="80" y1="50" x2="80" y2="210" stroke="#475569" stroke-width="1.5"/>
            
            <text x="70" y="55" fill="#94A3B8" font-family="monospace" font-size="10" text-anchor="end">2.0</text>
            <text x="70" y="130" fill="#94A3B8" font-family="monospace" font-size="10" text-anchor="end">1.0</text>
            <text x="70" y="210" fill="#94A3B8" font-family="monospace" font-size="10" text-anchor="end">0.0</text>
            <text x="50" y="130" fill="#64748B" font-family="monospace" font-size="10" text-anchor="middle" transform="rotate(-90 50 130)">BITS</text>
            
            {''.join(logo_svg)}

            <rect x="40" y="265" width="740" height="110" rx="6" fill="#0B132B" stroke="#1E293B" stroke-width="1"/>
            <text x="60" y="290" fill="#64748B" font-family="monospace" font-size="10" font-weight="700">GENOMIC ANNOTATION TRACK (5' ➔ 3')</text>
            <line x1="60" y1="325" x2="760" y2="325" stroke="#334155" stroke-width="1"/>
            {''.join(feature_svg)}
        </svg>
    </div>
    """


def render_dag_workflow_statechart(
    tasks: list[dict] = None,
    dependencies: list[dict] = None,
    title: str = "DIRECTED ACYCLIC GRAPH (DAG) TASK ORCHESTRATION PIPELINE",
    subtitle: str = "Multi-Stage Distributed Pipeline with Execution States & Asynchronous Dependency Channels",
    width: int = 860,
    height: int = 520,
) -> str:
    """
    Renders a Distributed DAG Pipeline / State Machine view:
    - Layered topological ranks from left to right (rankdir LR)
    - Orthogonal dependency connectors
    - Tasks colored by lifecycle state (success, running, queued, failed) with runtime duration badges
    Follows Airflow, Prefect, and XState visual execution standards.
    """
    if tasks is None:
        tasks = [
            {"id": "t1", "rank": 0, "label": "Ingest Invariance", "state": "success", "dur": "140ms"},
            {"id": "t2", "rank": 1, "label": "Convex MPC Solve", "state": "running", "dur": "12ms"},
            {"id": "t3", "rank": 1, "label": "Kalman Filtering", "state": "success", "dur": "4ms"},
            {"id": "t4", "rank": 2, "label": "Torque Command", "state": "queued", "dur": "--"},
            {"id": "t5", "rank": 2, "label": "Safety Reflex Interlock", "state": "success", "dur": "1ms"}
        ]

    if dependencies is None:
        dependencies = [
            {"src": "t1", "tgt": "t2"},
            {"src": "t1", "tgt": "t3"},
            {"src": "t2", "tgt": "t4"},
            {"src": "t3", "tgt": "t4"},
            {"src": "t3", "tgt": "t5"}
        ]

    task_coords = {
        "t1": (100, 200),
        "t2": (360, 130),
        "t3": (360, 270),
        "t4": (620, 130),
        "t5": (620, 270)
    }

    state_colors = {
        "success": ("#10B981", "rgba(16,185,129,0.15)"),
        "running": ("#4589FF", "rgba(69,137,255,0.2)"),
        "queued": ("#64748B", "rgba(100,116,139,0.1)"),
        "failed": ("#FA4D56", "rgba(250,77,86,0.2)")
    }

    dep_svg = []
    for d in dependencies:
        x1, y1 = task_coords[d["src"]]
        x2, y2 = task_coords[d["tgt"]]
        sx = x1 + 160
        sy = y1 + 30
        tx = x2
        ty = y2 + 30
        mx = (sx + tx) / 2
        dep_svg.append(f'<path d="M{sx},{sy} H{mx} V{ty} H{tx}" fill="none" stroke="#475569" stroke-width="2"/>')
        dep_svg.append(f'<polygon points="{tx},{ty} {tx-6},{ty-4} {tx-6},{ty+4}" fill="#94A3B8"/>')

    node_svg = []
    for t in tasks:
        tid = t["id"]
        x, y = task_coords[tid]
        st = t.get("state", "queued")
        bcol, bgcol = state_colors.get(st, ("#64748B", "rgba(100,116,139,0.1)"))
        lbl = t["label"]
        dur = t.get("dur", "")

        node_svg.append(f'<rect x="{x}" y="{y}" width="160" height="60" rx="6" fill="#0B132B" stroke="{bcol}" stroke-width="1.5"/>')
        node_svg.append(f'<rect x="{x}" y="{y}" width="4" height="60" rx="2" fill="{bcol}"/>')
        node_svg.append(f'<text x="{x+14}" y="{y+24}" fill="#F8FAFC" font-family="monospace" font-size="11" font-weight="700">{html.escape(lbl)}</text>')
        node_svg.append(f'<text x="{x+14}" y="{y+46}" fill="{bcol}" font-family="monospace" font-size="10" font-weight="700">[{st.upper()}]</text>')
        node_svg.append(f'<text x="{x+148}" y="{y+46}" fill="#64748B" font-family="monospace" font-size="10" text-anchor="end">{dur}</text>')

    return f"""
    <div style="background: #080C14; border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 24px; color: #FFFFFF; font-family: -apple-system, sans-serif; width: {width}px; height: {height}px; box-sizing: border-box;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
            <div>
                <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #4589FF; font-weight: 700; letter-spacing: 1px;">DISTRIBUTED PIPELINE DAG // AIRFLOW & PREFECT</div>
                <div style="font-size: 16px; font-weight: 800; color: #F8FAFC; margin-top: 2px;">{html.escape(title)}</div>
                <div style="font-size: 11px; color: #94A3B8; margin-top: 2px;">{html.escape(subtitle)}</div>
            </div>
            <div style="display: flex; gap: 8px;">
                <span style="background: rgba(69,137,255,0.15); border: 1px solid #4589FF; color: #4589FF; font-size: 10px; font-family: monospace; padding: 2px 8px; border-radius: 4px; font-weight: 700;">STAGE: 2/3 EXECUTING</span>
                <span style="background: rgba(16,185,129,0.15); border: 1px solid #10B981; color: #10B981; font-size: 10px; font-family: monospace; padding: 2px 8px; border-radius: 4px; font-weight: 700;">CONCURRENCY: 4 WORKERS</span>
            </div>
        </div>

        <svg viewBox="0 0 820 400" style="width: 100%; height: 400px; overflow: visible;">
            <rect width="820" height="400" rx="8" fill="#0B132B" stroke="#1E293B" stroke-width="1"/>
            
            <line x1="260" y1="30" x2="260" y2="370" stroke="#1E293B" stroke-width="1" stroke-dasharray="4,4"/>
            <line x1="520" y1="30" x2="520" y2="370" stroke="#1E293B" stroke-width="1" stroke-dasharray="4,4"/>
            <text x="180" y="385" fill="#475569" font-family="monospace" font-size="10" text-anchor="middle">RANK 0: INGESTION</text>
            <text x="440" y="385" fill="#475569" font-family="monospace" font-size="10" text-anchor="middle">RANK 1: PARALLEL COMPUTE</text>
            <text x="700" y="385" fill="#475569" font-family="monospace" font-size="10" text-anchor="middle">RANK 2: SERVO ACTUATION</text>

            {''.join(dep_svg)}
            {''.join(node_svg)}
        </svg>
    </div>
    """
