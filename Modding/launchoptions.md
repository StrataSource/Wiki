# Launch Options

This document only lists Chaos Source-specific launch options, 
for a full list of launch options, please see [the Valve Developer Wiki page](https://developer.valvesoftware.com/wiki/Command_Line_Options).

|Option|Description|
|---|---|
|-mountmod <path>|Specifies the mod to launch the game with|
|-legacyui|Launches the game with the old VGUI GameUI|
|-dev|Developer mode|


## POSIX-specific options (Not available on Windows)

The following options are only available on Linux currently. 

|Option|Description| 
|---|---|
|-gl_debug|(ToGL only) Spew additional OpenGL info for debugging|
|-nomousegrab|Forbids the game from grabbing the mouse|
|-gl_dump_strings|(ToGL only) Spew additional OpenGL info for debugging (Deprecated)|
|-exclusivefs|Run game with non-desktop friendly fullscreen. This will resize your display resolution (Deprecated)|
|-noexclusivefs|Run game with desktop friendly fullscreen, which is the default regardless (Deprecated)| 

## Hammer Options

|Option|Description|
|---|---|
|-winecompat|Runs hammer with some workarounds for wine bugs/differences|
