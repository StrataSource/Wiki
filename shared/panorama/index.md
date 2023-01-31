---
layout: default
title: Panorama
nav_order: 3
has_children: true
permalink: docs/Panorama
---


# Panorama

Panorama is Valve's own web-like UI framework used in various Source and Source 2 titles like CS:GO and
Half-Life: Alyx. Panorama uses XML for layouts, JavaScript for scripting and a custom version of CSS
for styling. The Chaos fork of Panorama additionally supports SASS/SCSS for stylesheets without an 
additional compile step.

Portal 2: Community Edition and Momentum mod both make extensive use of Panorama for their new UI,
and it's planned to be the replacement for VGUI.

## Usage

To use Panorama, simply launch the game **without** the `-legacyui` option. Additional developer-only
functionality, like reload keybinds, can be enabled by running with `-dev`.

# Developing with Panorama

UI files can be found in `<mod>/panorama`, depending on the game. If you're developing a p2ce mod,
copy the p2ce panorama files into your mod directory, then modify them.

Some files are stored in `platform/panorama` but these should not be modified by the end user.
If you do want to modify some element within `platform/panorama`, simply override the files by
adding them to `<game>/panorama`.


## Reloading Your Changes

When running the game with `-dev`, layouts, styles, and scripts can be reloaded by pressing `F7` or `F8` with a panel focused.
Pressing `F7` reloads everything that has changed since the last reload, and `F8` forcibly reloads every Panorama UI file.

Panels that use the global v8 context need special care taken when writing scripts. Defining named types such as classes or
functions should be completely avoided, since in global contexts, scripts aren't reloaded, but rather re-executed in the same
environment. The main menu's script is a good example of a "global context safe" script.

## Debugging

The panorama debugger can be toggled by entering `panorama_debugger_toggle` in the console, or by pressing `F6` with a
panel focused. The debugger is supported on Windows and Linux.

## Editors to Use

When developing Panorama, it is recommended to use [Visual Studio Code](https://code.visualstudio.com/) with the [Panorama CSS Support](https://marketplace.visualstudio.com/items?itemName=braemie.panorama-css) extension active. This extension is developed by brae, a member of the Momentum team, and the source can be found [here](https://github.com/braem/vscode-panorama-css). The extension adds several quality of life features, including but not limited to autocomplete and highlighting.

# Useful References

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
