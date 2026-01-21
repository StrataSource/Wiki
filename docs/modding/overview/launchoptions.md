---
title: Launch Options
---

# Launch Options

This document only lists Strata Source-specific launch options, for a full list
of launch options, please see
[the Valve Developer Wiki page](https://developer.valvesoftware.com/wiki/Command_Line_Options).

| Option                   | Description                                                                                                |
| ------------------------ | ---------------------------------------------------------------------------------------------------------- |
| -mountmod <path>         | Specifies the mod to launch the game with. Must be an absolute path                                        |
| -nogamemount             | Do not mount any games/mods specified in the gameinfo mounts block or mounts.kv                            |
| -nousermount             | Do not mount any games/mods specified in the mounts.kv                                                     |
| -nocustommount           | Do not mount any folders specified in gameinfo which contain wildcards (\* or ?), usually "custom" folders |
| -legacyui                | Launches the game with the old VGUI GameUI                                                                 |
| -dev                     | Developer mode                                                                                             |
| -multirun/-allowmultiple | Disables the creation of the source engine mutex, and allows the game to start even if one already exists  |
| -dedicated               | Launches the game as a dedicated server                                                                    |
| -nojserrors              | Disables the Panorama JS error dialog box                                                                  |
| -unrestrictedwebrequests | Disables the Panorama web request whitelist. NOT recommended, unless for a standalone mod                  |
| -debug_dynamic_mounts    | Enables verbose debug printing for debugging dynamic mounts                                                |
| -safemode                | Runs the game in safe mode, disabling additional configured mounts                                         |
| -jolt                    | Runs the game with vphysics_jolt (EXPERIMENTAL!)                                                           |
| -dedicated               | Launch the dedicated server                                                                                |
| -tools                   | Launch the game in engine tools mode                                                                       |

# Linux-only options

The following options are only available on Linux currently.

| Option         | Description                                                                                          |
| -------------- | ---------------------------------------------------------------------------------------------------- |
| -nomousegrab   | Forbids the game from grabbing the mouse                                                             |
| -exclusivefs   | Run game with non-desktop friendly fullscreen. This will resize your display resolution (Deprecated) |
| -noexclusivefs | Run game with desktop friendly fullscreen, which is the default regardless (Deprecated)              |

# Hammer Options

| Option      | Description                                                 |
| ----------- | ----------------------------------------------------------- |
| -winecompat | Enables the Qt file dialog in Hammer (on Linux)             |
