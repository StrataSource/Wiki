---
title: TypeScript Setup
---

# TypeScript Setup

This article assumes that readers will have a basic understanding of how TypeScript and its configuration file function. To learn more about these topics, see the [TypeScript official documentation.](https://www.typescriptlang.org/docs/)

## Linting

Code linting for Panorama scripting is typically done with ESLint and the ESLint Visual Studio Code extension, which allows code linting errors to be reported in real time instead of having to re-run the linter. This requires no special setup, however its accuracy can be greatly improved by installing the types module.

## Types Module

In order to ease development and enable better code linting, the Strata team maintains a library of TypeScript types which define every public interface available in Panorama as well as provide utility types for writing cleaner code.

This package can be installed in multiple ways:

### Package Dependency

If you are using a JavaScript package manager, the Panorama TypeScript types can be installed as a developer dependency:

```
npm install --save-dev github:StrataSource/pano-typed
```

After installing the package, it can be used in your `tsconfig.json` with the `compilerOptions.typeRoots` and `types` parameters.

```json :: tsconfig.json
{
	"compilerOptions": {
		"typeRoots": ["./node_modules/pano-typed"],
		"types": ["p2ce"]
	}
}
```

### Submodule

Installing the types as a Git submodule is a similar process. The submodule can be initialized to the `scripts/types` folder via the following command:

```
git submodule add "https://github.com/StrataSource/pano-typed.git" scripts/types
```

Just as the previous method, the location and subfolder of the types can be specified in the `tsconfig.json`.

```json :: tsconfig.json
{
	"compilerOptions": {
		"typeRoots": ["./scripts/types"],
		"types": ["p2ce"]
	}
}
```

## External Transpilation

When using Typescript, it is conventional to transpile it to JavaScript before passing it onto the target platform. While this is an option, Strata also supports directly importing and referencing TypeScript files. These files are internally transpiled and cached. This happens within the engine and is only recompiled whenever the code changes. To enable this functionality, simply use the `.ts` extension in place of the `.js` extension on your files. Note that `.ts` extensions are also expected in module imports.

> [!TIP]
> If you find that your code is not updating correctly in-game, try closing the game and deleting the `panorama_cache.dat` file. This fully removes any cached transpiled TypeScript/SCSS code.

During development, as well as for projects which encourage users to customize the interface, it is recommended to ship TypeScript instead of passing it through a bundler. It is for this reason that both Momentum Mod and Portal 2: Community Edition ship their TypeScript code. For other mods and games, using pre-transpiled scripts may net a slight performance benefit.

It is recommended to use the TypeScript transpiler without any additional bundling, as a bundler will have to be configured to treat each file referenced by a panel as an individual entrypoint, saving minimal amounts of storage (possibly increasing it when using shared modules!) and increasing deployment complexity unnecessarily.
