# The gr3y family — new websites

Three responsive static websites, built from scratch for GitHub Pages.

- `capital/`: gr3ycapital — finance and financial software
- `labs/`: gr3ylabs — software and experiments
- `support/`: gr3y.io — IT support
- `index.html`: collection preview

## Preview

Run `python -m http.server 4173` from this directory and open http://localhost:4173.
No package installation or build step is needed. `python build.py` regenerates the pages.

## Hosting

GitHub Actions deploys the static pages on every push to main. In repository Settings → Pages, choose GitHub Actions as the source.

These are new designs. Existing repositories and custom domain DNS remain untouched. No contact email, phone number, pricing, testimonials, or service guarantees were invented. Before moving the support site onto its live domain, supply the real contact route to add an inquiry CTA. Product artwork is illustrative; no budget app functionality is implied by the preview.

## Separate domains

Each website can be deployed separately: copy the relevant folder’s `index.html` plus `assets/` into a dedicated repository root, change `../assets/` to `assets/`, and replace relative family links with your confirmed production URLs. Add the appropriate CNAME file and configure DNS only when ready to replace the existing sites. The gr3ylabs production domain must be confirmed first.

Typography uses Google Fonts with system fallbacks; all artwork is local CSS, with no stock images, tracking, or paid dependencies. Includes keyboard focus states, mobile menus, reduced-motion support, semantic landmarks, and native FAQ disclosure controls.
