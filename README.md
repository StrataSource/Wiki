# Strata Source Wiki Docs

[![Strata Source](https://branding.stratasource.org/i/strata/logo/ondark/color.svg)](https://stratasource.org)

Welcome to the Strata Source Wiki!

This repository contains the documentation for various pages on the Wiki, separate from the repository that contains the [Wiki software](https://github.com/StrataSource/strata-wiki). The Wiki software is a submodule of this repository and is required to run a local Wiki instance.

If you are looking for the officially run Strata Source Wiki, please go here: https://wiki.stratasource.org/

## Getting Started

Before you begin, if you are wishing to contribute documentation changes to this repository, you will need to [fork this repository](https://github.com/StrataSource/Wiki/fork). This allows you to open a Pull Request targeting the `main` branch for review. The same goes for working with the Wiki software except making a Pull Request in that repository instead.

Node.js is required to run the Strata Source Wiki. If you do not have it installed, please go to the Node.js download page here: https://nodejs.org/en/download/

To start the Wiki, run the following:

```shell
./run.bat # Windows
 # or
./run.sh # Linux
```

On the first run, the `run` script will clone and initialize the Wiki software submodule. The script will then make sure all dependencies are installed to build the Wiki. Afterward, the site will be built and then run locally.

> [!NOTE]
> Every time `run` is executed, the script will perform a full-site build and index it for search. This will take a few minutes. The search data is cached and will be updated on every build.
>
> All future executions of `run` will just build and run the server. If you wish to run the Wiki instead of waiting for it to build, run `npm run dev`.

Site build output files are placed in `site/build`, which can be served using the HTTP server of choice.
