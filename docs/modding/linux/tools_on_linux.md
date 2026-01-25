---
title: "Running Windows Tools on Linux"
--- 
# Running Windows Tools on Linux

This article will cover the process of running Hammer on Linux-based operating systems and address many common questions or issues that may arise.

## Prerequisites

This process uses [Wine](https://www.winehq.org/), a program which acts as a translation layer that converts Windows calls into Linux calls, without the need for emulation. Wine can be installed using your distro's appropriate package manager, typically under the package name `wine`, or from Wine's website. 

>[!CAUTION]
>Since Wine 11, both the 32 and 64 bit packages of wine have been combined into one, so you only need to install the `wine` package for the tools to run properly. Installing the separate outdated 32 and 64 bit packages is not recommended and will likely cause issues.

If using a Virtual Machine or emulator such as WinBoat, the tools should work as-is, apart from any configuration file changes.

## Running Windows Tools

Tools such as Hammer, HLMV and Faceposer can be run trivially using wine. Typically, you will want to run these tools from the root of the game directory (the directory containing `p2ce/`, `platform/`, etc.).

For Hammer:
```sh
wine bin/win64/hammer.exe -winecompat
```

>[!NOTE]
> `-winecompat` is completely optional for Hammer. It simply enables the Qt file browser dialog instead of using the native one provided by wine.
> This flag does nothing in HLMV and Faceposer, as those tools have no Qt integration.

Faceposer and HLMV both require the `-game` parameter to tell it which game to use. If running from the root of the game directory:
```sh
wine bin/win64/hlmv.exe -game p2ce
```

`-game` can be an arbitrary path, even an absolute directory. It just needs to point to the directory containing `gameinfo.txt`.

If you are running Hammer after previously using the program on Windows, you will have to edit your configurations to the correct filepaths. Make sure to point to the Windows executables, even for tools that have Linux-native versions, as Wine is not able to run Linux applications.

## Common Issues and Fixes

This section should cover most of the issues most users have when setting up Windows tools. If this guide does not solve your issue, please ask for help in your game's Discord server. Make sure to list what steps you have taken to attempt to solve the issue, and follow [Dont Ask to Ask](https://dontasktoask.com/)!

### "Setup file 'gameinfo.txt' doesn't exist in subdirectory" when launching

Typically, this occurs when a path in your configuration file is incorrect, especially for Hammer if it has previously been run on Windows. 

For Hammer, if you see the Select Config dialog when you start the program, edit the config to use the correct path.

For HLMV/Faceposer or if you only have one config for Hammer, first try making sure that the path specified in your `-game` option exists and that a `gameinfo.txt` file exists. If it does exist but `gameinfo.txt` still cannot be found, try using an absolute path. This should fix most cases of broken paths. If this does not fix your issue, navigate to `<game>/hammer/cfg` and either delete or rename `gameconfig.txt`. This will recreate your game configuration file next time you start Hammer, and will likely fix all issues with broken paths. Alternatively, you can manually edit the file to alter the paths to their correct location.
>[!NOTE]
>Wine prefixes all paths with a fake drive letter, `Z:` for the root with each loaded partition having its own drive letter, to maintain compatibility with Windows filesystems. Make sure to add this to the beginning of all your paths for them to work correctly.

### My game looks washed out when ran from Hammer!

In some distros or Desktop Environments, when launching the game through the compilation can appear washed out or overbrightened when ran through Wine. This appears to be an issue with how some Desktop Environments, like Hyprland, interact with Wine applications, so the best way to remedy this issue is by running the game through Steam and manually running the map through the console.

### "Portal 2 is not installed" (Portal 2: Community Edition)

This error can occur for a variety of reasons, but usually it is because Portal 2 cannot be found by Steam. Make sure that Portal 2 is in fact installed and visible in your Steam library, then try verifying the game files of both Portal 2 and Portal 2: CE. Next, try restarting Steam to reload your library. If this does not fix your issue, try moving your Portal 2 install to the same drive as your Portal 2: Community Edition install. If all else fails, contact a programmer with your issue.