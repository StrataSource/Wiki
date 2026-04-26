---
title: Introduction
weight: 0
---

# Developer UI

Developer UI, AKA DevUI, is an ImGui rewrite of some of Valve's VGUI debugging tools. It provides various information about the engine, entities and materials inside the map and the game overall, as well as debuggers for Angelscript and material inspector.

![Developer UI](categories/images/prof_all.png)

## Usage

There are two ways to open the Developer UI - using the `devui_toggle_menu` console command, or by pressing `shift + f1`.

There are 8 tabs total: 
[Windows](categories/windows), 
[Graphics](categories/graphics), 
[Profiler](categories/profiler), 
[Map](categories/map), 
[Game](categories/game), 
[Scripting](categories/scripting), 
[Settings](categories/settings),
[Debug](categories/debug). 
Each tab is a dropdown menu containing buttons, each button opens up a window.

![Developer UI Menu](categories/images/devui.png)

## Implementation

In Strata Source, Developer UI is implemented using ImGUI - a bloat-free graphical user interface library for C++. More about ImGUI in [here](https://github.com/ocornut/imgui).

## Misc

The map used on the screenshots is [Gentle Hum by Beckeroo.](https://steamcommunity.com/sharedfiles/filedetails/?id=3485953221).
