---
layout: default
title: Launch Options
parent: Reference
---

# Launch Options

This document only lists Chaos Source-specific launch options, for a full list
of launch options, please see
[the Valve Developer Wiki page](https://developer.valvesoftware.com/wiki/Command_Line_Options).

| Option                   | Description                                                                                                |
| ------------------------ | ---------------------------------------------------------------------------------------------------------- |
| -mountmod <path>         | Specifies the mod to launch the game with. Must be an absolute path                                        |
| -nogamemount             | Do not mount any games/mods specified in the gameinfo mounts block or mounts.kv                            |
| -nocustommount           | Do not mount any folders specified in gameinfo which contain wildcards (\* or ?), usually "custom" folders |
| -legacyui                | Launches the game with the old VGUI GameUI                                                                 |
| -dev                     | Developer mode                                                                                             |
| -dx11                    | Launch game with DirectX 11 shaderapi (On Linux, this will launch dx11 with dxvk)                          |
| -multirun/-allowmultiple | Disables the creation of the source engine mutex, and allows the game to start even if one already exists  |

## POSIX-specific options (Not available on Windows)

The following options are only available on Linux currently.

| Option         | Description                                                                                          |
| -------------- | ---------------------------------------------------------------------------------------------------- |
| -nomousegrab   | Forbids the game from grabbing the mouse                                                             |
| -exclusivefs   | Run game with non-desktop friendly fullscreen. This will resize your display resolution (Deprecated) |
| -noexclusivefs | Run game with desktop friendly fullscreen, which is the default regardless (Deprecated)              |
| -d9vk          | Launches the game with dx9 through dxvk                                                              |

## Hammer Options

| Option      | Description                                                 |
| ----------- | ----------------------------------------------------------- |
| -winecompat | Runs hammer with some workarounds for wine bugs/differences |
