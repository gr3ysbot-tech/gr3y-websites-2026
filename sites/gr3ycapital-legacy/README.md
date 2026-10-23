# Gr3y Capital + Gr3yLabs website

A buildless static website for **gr3ycapital.com**, with the experimental branch at **/gr3ylab/**. Designed for GitHub Pages; no backend, database, npm installation, analytics, forms or accounts. Open `index.html` locally for a quick look, or run the preview server below.

## Contents

- `index.html`: Gr3y Capital, LLC parent site. Ivory/charcoal/orange editorial design; trading/finance identity, perspective and corporate relationship.
- `gr3ylab/index.html`: Gr3yLabs in charcoal/lime/lilac; filterable project list, project-detail dialogs, IT script review links, Gr3yShot development status, QuantGenius/Twitchy references and YouTube link.
- `assets/`: CSS, vanilla JS, original SVG/favicon and code-native graphic treatments. Fonts are self-hosted DM Sans and Space Grotesk under their included SIL Open Font Licenses, sourced from the Google Fonts repository. No external font request is needed.
- `.github/workflows/pages.yml`: upload/deploy workflow. Upload this folder's **contents** as the root of a dedicated repository, including the hidden `.github` directory.
- `CNAME`, `robots.txt`, `sitemap.xml`, `404.html`: domain, indexing and not-found support.

## Preview and checks

```powershell
cd Z:/Projects/Gr3yShot/websites/gr3ycapital
python check.py
node --check assets/site.js
python -m http.server 4317 --bind 127.0.0.1
```

Open `http://127.0.0.1:4317/` and `http://127.0.0.1:4317/gr3ylab/`. Stop the preview with Ctrl+C. No app signing certificate is required to host static HTML on GitHub Pages.

## Publish on GitHub Pages

1. Create a dedicated repository, such as `gr3ycapital-site`. Public repositories support Pages on GitHub Free; private repository support depends on the GitHub plan.
2. Put this directory's contents at the repository root, including `.github/workflows/pages.yml`. Do not upload the Gr3yShot application, Azure metadata, credentials, private captures or the rest of the workspace.
3. Set **Settings → Pages → Build and deployment → Source → GitHub Actions**.
4. Push to `main`, or run **Deploy static site to GitHub Pages** from Actions. The deployment environment returns your preview URL.
5. Verify domain ownership in GitHub, then set **Settings → Pages → Custom domain** to `gr3ycapital.com` before updating DNS. The included CNAME is useful for branch-based hosting; Actions deployments still require the domain setting in GitHub.
6. Configure the apex domain at your DNS provider using GitHub's documented A/ALIAS/ANAME records; configure `www` if desired, and enable Enforce HTTPS after DNS/certificate readiness.

GitHub's current instructions:
- https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
- https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site

## Content and verification boundaries

Confirmed by the owner: company legal name Gr3y Capital, LLC; trading/finance focus; Gr3yLabs experimental IT/software/media branch; domain gr3ycapital.com; route /gr3ylab/; channel https://www.youtube.com/@gr3ylabs. Public Labs reference supplied by the owner was retrieved for project names, public `hello@gr3y.io` contact, privacy/opt-out links. No private email/address/identity details from the Azure screenshots appear in the site.

No returns, licenses, regulatory registration, assets under management, customers, testimonials, clip counts, live market data or software release claims were invented. Existing Labs project descriptions are summarized, not proof of operational performance. Gr3yShot is explicitly in development. The utility link opens code for review; no remote script is executed or copied into an executable command. Existing terms/privacy/opt-out documents remain at the Labs reference site and are not rewritten here.

The site is committed at https://github.com/gr3ysbot-tech/gr3ycapital and deployed at https://gr3ysbot-tech.github.io/gr3ycapital/ with the Labs page at https://gr3ysbot-tech.github.io/gr3ycapital/gr3ylab/. GitHub Pages uses the included Actions workflow. The custom domain gr3ycapital.com is not connected yet; DNS and the existing Labs website are unchanged. No public contact email for Capital itself was confirmed; only the existing public Labs contact is used. Browser tools were unavailable for visual QA. Static integrity, JS syntax and local HTTP route checks are the available evidence; responsive layout, keyboard behavior and dialogs require browser review before publication. Existing `labs.gr3y.io` remains unchanged.

To publish Labs itself at `labs.gr3y.io` later, prepare a separate root export and update canonical/relative links and GitHub custom-domain settings; do not simply copy `gr3ylab/index.html` alone, because it needs shared assets and a parent link.

