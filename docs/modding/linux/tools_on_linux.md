---
title: "Running Windows Tools on Linux"
--- 
# Running Windows Tools on Linux

This article will cover the process of running Hammer on Linux-based operating systems and address many common questions or issues that may arise.

## Installing Dependencies

Running Windows applications on Linux is done through [Wine](https://www.winehq.org/). Valve has a modified version of Wine called Proton, but we do not recommend using it with Hammer for
ease of use reasons, and due to some issues with dynamic mounting.

### Step 1: Installing Wine and Winetricks

>[!CAUTION]
> Since Wine 11, both the 32 and 64 bit packages of wine have been combined into one, so you only need to install the `wine` package for the tools to run properly. Installing the separate outdated 32 and 64 bit packages is not recommended and will likely cause issues.

>[!CAUTION]
> Some versions of Wine 10 are known to cause severe flickering in the 2D and 3D viewports. **We recommend using Wine 11+**, if possible.
>
> Wine 11 causes a minor regression with the face edit dialog causing it to open when Hammer is launched.

To install via APT (Debian, Ubuntu, etc.):
```sh
sudo apt-get install wine winetricks
```

To install via DNF (Fedora, Rocky Linux, Alma Linux, etc.):
```sh
sudo dnf install wine winetricks
```

To install via pacman (Arch, Manjaro, etc.):
```sh
sudo pacman -S wine winetricks
```

### Step 2: Installing DXVK with Winetricks

For the best possible Hammer experience on Linux, we recommend using DXVK instead of the native WineD3D compatibility layer. DXVK fixes a number of issues caused by WineD3D.

This can be done trivially using winetricks:
```sh
winetricks dlls dxvk
```

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

Installing DXVK should fix this. The default DirectX 11 compatibility layer in wine called wined3d tends to cause this.

You can also try to disable anti-aliasing in the Hammer settings, though this should be unnecessary with DXVK.

### "Portal 2 is not installed" (Portal 2: Community Edition)

This may happen if there's an issue with Steam's generated libraryfolders.vdf.
1. Make sure that Portal 2 is actually installed in Steam
2. Restart Steam to ensure the libraryfolders.vdf is updated on disk.

Launching Hammer with `-debug_dynamic_mounts` will trace through the dynamic mounts loading code and can give hints as to why the mounting has failed.

If you're still having issues, verify that `~/.steam/steam/steamapps/libraryfolders.vdf` exists and contains an entry for appid 620.

### Hammer looks tiny on my 4k screen!

You can adjust the default DPI of the applications using `winecfg`.

Run `winecfg` in a terminal, navigate to "Graphics" and adjust the DPI as desired under the "Screen resolution" section.
