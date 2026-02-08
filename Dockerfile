# Dockerfile
FROM squidfunk/mkdocs-material:latest

# Install the PlantUML markdown plugin into the image
RUN pip install --no-cache-dir plantuml-markdown
