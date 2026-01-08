---
title: Getting Started With The Wiki Software
weight: 0
---

# Getting Started With The Wiki Software

This Wiki topic assumes that you understand how to work with TypeScript, SCSS, HTML, Svelte, as well as Git submodules. The Wiki software is a submodule separate from the documentation.

If you followed the instructions from [Getting Started](../basics/getting-started.md), then the Wiki software should already be setup correctly. However, if you wish to contribute to the Wiki software, you will need to make a fork of the repository so an Pull Request can be created. If you remove the current `site` folder in the `Wiki` repository and replace it with your own fork under the same name, then the Wiki will use your version of the software.

## Editors & Extensions

The recommended editor for editing both the Wiki documentation or working with the Wiki software is [Visual Studio Code](https://code.visualstudio.com/).

Below are a few extensions you can install to help with working the repository:

[`markdownlint`](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint) By David Anson: A extension for Markdown linting and style checking.

[`Svelte for VS Code`](https://marketplace.visualstudio.com/items?itemName=svelte.svelte-vscode) By Svelte: The official language support extension.

[`ESLint`](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) By Microsoft: A linter for both JavaScript and TypeScript code.

[`Code Spell Checker`](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker) By Street Side Software: A basic spellchecker for both code and other files.

## File Structure

The Wiki software file structure is much more complex than the Wiki documentation. The folder that will be worked with the most is the `src` folder which contains everything that drives the Wiki. Nothing else should be touched unless you know what you are doing.

`lib`: Where some site assets belong, where various components like buttons, Markdown notices, and more are structure, as well as where the dump parsers live.

`routes`: Contains the TypeScript and Svelte files used to structure and make the Wiki function for each page and piece of the Wiki. Ex. page footers, categories, CSS formatting, HTML structure, etc.

## What's Next

Once you are setup and you understand what each folder in Wiki software is for, feel free to check out the other articles in the `Advanced` section of the `Contribution` topic.