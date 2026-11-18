# Contributing to Scientific Visual Studio

Thank you for your interest in contributing to **Scientific Visual Studio**! We welcome contributions to expand our domain-agnostic visual component library.

## Architectural Principles

When contributing new components or layouts, please adhere to these core design rules:

1. **Domain-Agnostic Core**: Visual components must NOT contain hardcoded application logic or course domain content. All labels, values, formulas, code snippets, and metrics should be passed via parameters.
2. **Deterministic & Self-Contained**: Components render self-contained HTML/SVG with embedded styling and CSS animations. They must render reliably both in browser contexts (Remotion, Slide decks) and headlessly (Playwright, Puppeteer).
3. **Cyber-Academic Aesthetic**: Deep slate/navy canvases (`#080C14`, `#0B0F19`), translucent frosted glass cards, monospace telemetry micro-labels, and high-contrast scientific accent palettes (`#38BDF8`, `#6366F1`, `#10B981`, `#F59E0B`).

## Development Workflow

1. Fork and clone the repository.
2. Install dependencies:
   ```bash
   pip install -e .
   ```
3. Add your new visual component function in `scientific_visual_studio/visual_studio.py` (or `visual_studio_extensions.py`).
4. Add a gallery test case in `generate_gallery_assets.py` and run:
   ```bash
   python generate_gallery_assets.py
   ```
5. Ensure the new preview image renders cleanly in `assets/gallery/`.
6. Document the component in `GALLERY.md` and submit a Pull Request!
