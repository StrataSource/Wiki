---
title: P2:CE Mod Template
---

# P2:CE Mod Template
For Portal 2: Community Edition, you can download a free template for sourcemods that includes a basic structure for your mod.

### Using the SDK Launcher
The easiest way to make a mod for P2:CE is to use the SDK Launcher.
Simply open the launcher, choose Utilites, and then New Mod. Through the dialog, you can choose the install location, the name, and also whether or not to create a shortcut on your desktop.

### Manually
Another way to make a content-based mod, simply download the template [here](https://github.com/StrataSource/p2ce-mod-template) and extract its contents to `<your Steam installation>/steamapps/sourcemods`.

Note that even if your Steam library is in a different location, you **must** place your mod in your Steam installation or else it will not show up. You also must restart Steam for your mod to show up once everything's copied over.

## Launching
If your mod's files are placed within your `sourcemods` folder, you can simply launch your mod from Steam itself.

Alternatively, your mod can be launched from the command line.
To launch on Windows: 
```sh
"..\..\common\Portal 2 Community Edition\bin\win64\p2ce.exe" -legacyui -game "%cd%"
```
###### Note: on some older versions of P2:CE, you may need to replace `p2ce.exe` with `chaos.exe`.

To launch on Linux:
```sh
"../../common/Portal 2 Community Edition/p2ce.sh" -legacyui -game "$PWD"
```

## Contents
The template includes a few files and folders that you can use for easy customization of P2:CE. This section will go over the most important ones, or ones that are different from a typical sourcemod.

### `cfg`
`cfg` contains important configuration files for your mod, like `mounts.kv`.

### `maps`
This folder is where all your maps should be placed. P2:CE will look inside of this directory for map files.

### `panorama`
The `panorama` folder contains assets and XML files for customization of Panorama, P2:CE's UI framework.

### `resource`
This folder contains resource files, configurations, and notably, your mod's icon (`game.ico` and `game-icon.bmp`).

`resource` also contains closed caption and localization files.

### `scripts`

The `scripts` folder contains some useful configurations for UI elements as well as VScripts.

