# Strata Wiki Docs

[![Strata Source](https://branding.stratasource.org/i/strata/logo/ondark/color.svg)](https://stratasource.org)

Welcome to the Strata Wiki!

This repository contains the documentation for various pages on the Wiki, sperate from the repository that contains the [Wiki software](https://github.com/StrataSource/strata-wiki). The Wiki software is a submodule of this repository and is required to run a local instance of the Wiki through this repository.

## Quick Start

To quickly start developing on the Wiki, run the following:

```shell
./run.bat # Windows
 # or
./run.sh # Linux
```

The `run` script on first run will clone and initiate the Wiki software submodule. The script will then make sure all dependencies are installed to build the Wiki. Afterward, the site will be built and then run locally.

> [!NOTE]
> Building will perform a build of the full site as well as indexing it for the search. This will take a few minutes. The search data is cached and will update on every build.

All future executions of `run` will just build and run the server.

Site build output files are placed in `site/build`, which can be served using the HTTP Server of choice.
