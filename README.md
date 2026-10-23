# The gr3y family â€” new websites

## Central website source

This public repository is now the central source for the GitHub websites. Application
backends, endpoint agents, credentials and customer data belong in separate private
projects. The original root previews below are preserved separately from the current
production snapshots in `sites/`.

| Site folder | Address | GitHub Pages publishing repository |
|---|---|---|
| `sites/gr3y-io` | gr3y.io | gr3y-io-site |
| `sites/gr3ycapital` | gr3ycapital.com | gr3ycapital-site |
| `sites/gr3ylabs` | gr3ylabs.com | gr3ylabs-site |
| `sites/julianben` | julianben.com | julianben.com |
| `sites/labs-gr3y` | labs.gr3y.io | labs-gr3ylabs |
| `sites/gr3ycapital-legacy` | Existing GitHub Pages project, no custom domain configured | gr3ycapital |
| `sites/scanprotectai` | scan.gr3y.io | scanprotectai-web |

`sites.json` records each target, custom domain and imported source commit/file hashes.
Six existing public site repositories were copied without Git history or changes to
their live content or DNS. ScanProtectAI contains only its public static assets and
links to its separately protected support API. The existing `scanprotectai-site`
repository remains private and is not used as a public deployment target.

GitHub Pages supports one custom domain per repository. These small publishing
repositories therefore remain in place for their domains, while edits are managed
here. Consolidation does not require moving the websites to Synology or changing
their addresses. Avoid editing deployment repositories directly; import any emergency
fix back into this repository before the next publication.

## Update a website

1. Edit the appropriate `sites/<name>/` folder and preview it with a static server.
2. Keep its CNAME, links, licenses and assets intact. Review the files for private data.
3. Commit and push this repository's `main` branch.
4. Run `python scripts/publish_site.py <name>` to review changed/removed files.
5. Run `python scripts/publish_site.py <name> --publish` to publish that site only.
6. Check the target repository's Pages deployment and its live address.

The publisher uses your existing `gh` sign-in, checks that the target is public and
static, and makes a single non-forced commit. It refuses uncommitted/unpushed central
source, symlinks, unsupported files and common credential formats. No cross-repository
token or credentials are stored here. Automatic cross-repository publishing is not
configured. Revert the central source and publish again to roll back a content change.

The root GitHub Pages collection continues to show the original design previews.
It is not the production publishing source for all custom domains at once.

## Original design previews

Three responsive static websites, built from scratch for GitHub Pages.

- `capital/`: gr3ycapital â€” finance and financial software
- `labs/`: gr3ylabs â€” software and experiments
- `support/`: gr3y.io â€” IT support
- `index.html`: collection preview

## Preview

Run `python -m http.server 4173` from this directory and open http://localhost:4173.
No package installation or build step is needed. `python build.py` regenerates the pages.

## Hosting

GitHub Actions deploys the static pages on every push to main. In repository Settings â†’ Pages, choose GitHub Actions as the source.

These are new designs. Existing repositories and custom domain DNS remain untouched. No contact email, phone number, pricing, testimonials, or service guarantees were invented. Before moving the support site onto its live domain, supply the real contact route to add an inquiry CTA. Product artwork is illustrative; no budget app functionality is implied by the preview.

## Separate domains

Each website can be deployed separately: copy the relevant folderâ€™s `index.html` plus `assets/` into a dedicated repository root, change `../assets/` to `assets/`, and replace relative family links with your confirmed production URLs. Add the appropriate CNAME file and configure DNS only when ready to replace the existing sites. The gr3ylabs production domain must be confirmed first.

Typography uses Google Fonts with system fallbacks; all artwork is local CSS, with no stock images, tracking, or paid dependencies. Includes keyboard focus states, mobile menus, reduced-motion support, semantic landmarks, and native FAQ disclosure controls.
