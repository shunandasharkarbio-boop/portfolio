# Mobile Responsiveness Implementation Plan

## Goal Description

Make the entire Shunanda portfolio website fully mobile responsive while preserving the premium design, animations, and visual fidelity. This includes adjusting layout, typography, images, and interactive elements for viewport widths from 320px up to desktop.

## User Review Required

> [!IMPORTANT]
> The plan introduces several new media queries and reorganizes some HTML structures (e.g., converting grid rows to flex on small screens). Confirm that you are comfortable with the proposed breakpoints and that no additional design assets are required.

## Open Questions

> [!WARNING]
> - Do you want a mobile navigation drawer (slide‑in menu) or a simple collapsible menu? The plan assumes a slide‑in drawer.
> - Are there any sections (e.g., the 3‑D DNA helix) that must retain exact dimensions on mobile, or can they be scaled down?

## Proposed Changes

---
### HTML Adjustments
- **Header**: Add a mobile‑toggle button (already present) and a hidden navigation drawer (`.mobile-nav`).
- **Skills Section**: Ensure the hero row (`.skd-hero-row`) switches to a single column on <768px.
- **About Section**: Change `.about-grid` to a single column on small screens. Adjust profile photo size.
- **Projects & Journey**: Add responsive grid tweaks similar to Skills.
- **Footer**: Stack footer columns vertically on narrow screens.

---
### CSS Updates (`style.css`)
- Add a base breakpoint at **768px** for tablets and **480px** for phones.
- Use `flex-direction: column;` for grid containers when below breakpoints.
- Scale fonts using `clamp()` for fluid typography.
- Resize images and canvas (`#dnaCanvas`) to fit container width.
- Reduce padding/margins for mobile to preserve space.
- Implement a slide‑in mobile navigation drawer with transition.
- Ensure the rotating DNA overlay scales proportionally via `aspect‑ratio` and `%` positioning.
- Adjust stat cards, skill cards, and interest pills to wrap appropriately.

---
### Verification Plan
- **Automated**: Run `npx http-server` and open `http://localhost:3000` with Chrome DevTools device toolbar for multiple viewports.
- **Manual**: Visually inspect each section on iPhone SE (320px), Pixel 4 (411px), iPad (768px) and desktop.
- Verify that hover effects degrade gracefully on touch devices.
- Confirm the DNA animation still rotates and aligns correctly.

---
### Timeline
- **Day 1**: Add HTML structure for mobile nav drawer and update media queries.
- **Day 2**: Test and tweak layout breakpoints, adjust typography, images.
- **Day 3**: Polish animations for mobile, final QA, update README.
