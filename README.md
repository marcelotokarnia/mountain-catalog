# Trekkpedia

## How to hack locally

[TL;DR](./docs/LOCAL_SETUP_TLDR.md)

[Explained version](./docs/LOCAL_SETUP_EXPLAINED.md)

## How to set your docker production environment

[Production environment](./docs/PRODUCTION_ENVIRONMENT.md)

## About the project

A `Vue` and `Typescript` application which you can search and filter mountains next to you and have hints on how to conquer them.

This application assets are built with `Webpack`.

All requests are made through `Graphql` (`Vue Apollo` on the frontend and `Django Graphene` on the backend) to communicate with the `Python / Django` backend and the `Postgis` database.

The local state management is powered by `Apollo Link State`.

Styling uses `Bootstrap` and `Styllus`

The application is served through generated `Docker` images, `uwsgi` server and balanced by `nginx` (which also server static assets)

Unit tests are made possible by `Karma (with mocha & chai)` on the frontend and `Django Nose` on the backend.

~~E2E tests are powered by `cypress`~~ (not yet)

Lint is made with `flake8` (python), `tslint` (typescript), `eslint` (js), `wotan`(vue)

Author: [Marcelo Tokarnia](https://www.github.com/marcelotokarnia)

Deployed at: [mountains@AWS/EC2](https://mountains.tokks.tech/)