# Website collection

- This public repository contains public static websites and website maintenance tools only.
- Do not copy application backends, endpoint agents, credentials, infrastructure snapshots or customer diagnostics here.
- Edit each production site in its `sites/<name>/` folder. Preserve its custom domain and deployment target in `sites.json`.
- Existing root `capital/`, `labs/` and `support/` folders are design previews; do not replace active websites with them as part of unrelated work.
- Keep README.md and sites.json current for setup, deployment and ownership changes.
- Publish one reviewed site at a time with `scripts/publish_site.py`; its default is a read-only diff. Preserve unrelated sites and never force-update target branches.
- The deployment repositories retain independent GitHub Pages custom domains. Do not delete them or change DNS during source consolidation.
