---
layout: default
title: Using Panorama
parent: Panorama
nav_order: 1
---

# Using Panorama

As of Momentum Mod 0.8.8 and Portal 2: Community Edition 0.5.6, both games ship
with Panorama installed.

To use Panorama, you must launch the game *without* the `-legacyui` option. P2CE has launch options specifically
for Panorama, so Steam should ask you when you're trying to launch the game. Momentum Mod launches with Panorama
by default.

## Tinkering with Panorama

All current Chaos engine games do not pack Panorama assets, letting users freely modify them. However, this is subject
to change. If `<game>/panorama/code.pbin` is present, you must extract the contents of `<game>/panorama/code.pbin`
into `<game>/panorama/`. The `code.pbin` file is just a signed zip file, so you should be able to open it with a
utility such as WinRAR, Ark, or 7-Zip. For Panorama to load the extracted files off the disk instead of from `code.pbin`,
the game needs to be run with `-dev`. 

Keep in mind that `code.pbin` is signed to prevent modification, and if present it must exist for the game to start with Panorama.

## Reloading Your Changes

When running the game with `-dev`, layouts, styles, and scripts can be reloaded by pressing `F7` or `F8` with a panel focused.
Pressing `F7` reloads everything that has changed since the last reload, and `F8` forcibly reloads every Panorama UI file.

Panels that use the global v8 context need special care taken when writing scripts. Defining named types such as classes or
functions should be completely avoided, since in global contexts, scripts aren't reloaded, but rather re-executed in the same
environment. The main menu's script is a good example of a "global context safe" script.

## Panorama Debugger

The panorama debugger can be enabled by entering `panorama_debugger_toggle` in the console, or by pressing `F6` with a
panel focused. The debugger is supported on Windows and Linux.

## Developing Panorama

When developing Panorama, it is recommended to use [Visual Studio Code](https://code.visualstudio.com/) with the [Panorama CSS Support](https://marketplace.visualstudio.com/items?itemName=braemie.panorama-css) extension active. This extension is developed by brae, a member of the Momentum team, and the source can be found [here](https://github.com/braem/vscode-panorama-css). The extension adds several quality of life features, including but not limited to autocomplete and highlighting.

## Useful References

The Valve Developer Community wiki has several useful articles to assist with creating a UI in Panorama. Note that these
articles target CSGO and do not cover any new Chaos engine features.
- [CSGO CSS Properties](https://developer.valvesoftware.com/wiki/CSGO_Panorama_CSS_Properties) - Chaos engine currently uses
  all the CSS properties of CS:GO.
- [CSGO Panorama Events](https://developer.valvesoftware.com/wiki/CSGO_Panorama_Events) - A majority of these events are either
  nonfunctional or not present in the Chaos engine, however general events that do not pertain to CSGO should be present and
  functional.
- [CSGO Panorama API](https://developer.valvesoftware.com/wiki/CSGO_Panorama_API) - Contains many API functions that can be ran
  in Panorama JavaScript files. Some are specific to CSGO, and either not present or not functional in the Chaos engine.

You can also run these console commands to access up-to-date documentation:
- `dump_panorama_css_properties` - Prints a list of the available CSS properties to the console, along with documentation for
  each property if documentation is written.
- `dump_panorama_events` - Prints a list of Panorama events to the console, along with documentation for each event if documentation
  is written.
- `dump_panorama_js_scopes` - Prints a list of the currently available JavaScript API functions to the console, along with
  documentation for each function if documentation is written.
