# hybrid-conversion-docs
Documentation repo for a hybrid vehicle conversion project

## Deployment
This repo contains source for the Material static site generator which is being published to GitHub Pages. 
Pages always contains the latest content from the `main` branch and is automatically updated when changes merge.

## Development
To preview the site created by Material, without installing locally use the following command
```
docker compose up
```

To preview the site, with automatic re-generation when any file under `docs` is changed use
```
docker compose watch
```
