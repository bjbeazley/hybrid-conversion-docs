# hybrid-conversion-docs
Documentation repo for a hybrid vehicle conversion project

## Deployment
This repo contains source for a static site generator which is being published to GitHub Pages. Pages always contains the latest content from the `main` branch and is automatically updated when changes merge.

## Development
To preview the site created by MkDocs, without installing theme packages locally do the following

```
# 1. Create a venv
python -m venv .venv

# 2. Activate it
# macOS / Linux:
source .venv/bin/activate
# Windows (PowerShell):
# .venv\Scripts\Activate.ps1

# 3. Install MkDocs + any themes/plugins *into the venv only*
pip install mkdocs-bootswatch

# 4. Run the dev server
mkdocs serve
```

