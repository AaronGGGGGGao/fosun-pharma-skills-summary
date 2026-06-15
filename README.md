# Fosun Pharma Skills Summary

This repository contains a static HTML showcase for multiple AI for Science skills.

## Main site

- Entry page: `summary/index.html`
- Skill pages: `summary/skills/`
- Shared assets: `summary/assets/`
- Download bundles: `summary/downloads/`

## Local preview

From the `summary/` directory:

```bash
python3 -m http.server 8123
```

Then open:

```text
http://127.0.0.1:8123
```

## Notes

- The site is plain static HTML/CSS/JS.
- Source skill outputs are stored under `skills_output/`.
- Downloadable artifacts used by the site are generated from local output files.
