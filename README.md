# hybrid-conversion-docs
Documentation repo for a hybrid vehicle conversion project

## Deployment
This repo contains source for the Material static site generator which is being published to GitHub Pages. 
Pages always contains the latest content from the `main` branch and is automatically updated when changes merge.

## Development
To preview the site created by Material, without installing locally use the following command

```
docker run --rm -it --net=host -v ${PWD}:/docs squidfunk/mkdocs-material serve
```

