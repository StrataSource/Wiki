---
layout: default
title: Modwrapper
parent: Modding
---

# Modwrapper

Making a mod for P2CE works a bit differently to normal sourcemods. Every P2CE
mod includes a .exe file that loads up the installed Steam copy of P2CE and
mounts your mod on top of it.

## SDK Launcher

The [SDK Launcher](https://github.com/ChaosInitiative/SDKLauncher) can be used
to set up this entire mod scaffold automatically.

## Creating the mod wrapper

The mod wrapper creation python script located at
`steamapps/common/Portal 2 Community Edition/sdk_tools/newmod.py` can be used to
quickly set up a boilerplate mod wrapper. (Requires python version 3!)

Example:

```
python3 newmod.py --name "my_mod" --target "C:\Projects\My mod"
```

This will create a mod wrapper in '`C:/Projects/My mod` with your mod's content
path "my_mod". If you have a Steam App ID for your mod, enter the parameter
`--appid`

```
python3 newmod.py --name "revolution" --target "C:\Projects\Portal Revolution" --appid 601360
```

A `gameinfo.txt` template called `example_gameinfo.txt` will be generated in the
content dir. You can remove and replace this with your own `gameinfo.txt`.

You will find a `launch.bat` script in the root directory of the mod. This
launches `modwrapper.exe` with the proper command line parameters. Steam mods
should directly reference the `modwrapper.exe` with those parameters in the
Steamworks launch configuration

Other than that, modding works exactly like with any other source engine game.
