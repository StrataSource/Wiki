---
title: "Running Hammer on Linux"
--- 
# Running Hammer on Linux
This article will cover the process of running Hammer on Linux-based operating systems and address many common questions or issues that may arise.

## Prerequisites
This process uses a program named [Wine](https://www.winehq.org/), which is a translation layer that converts calls meant for Windows into native Linux calls, without the need for emulation. Wine can be installed using your distro's appropriate package manager or from the [WineHQ](https://www.winehq.org/) website. 

## Running Hammer
First, run a Terminal window and navigate to `<game>/bin/win64` using `cd`. Now, copy this command into the terminal: 
```
wine hammer.exe -winecompat -game "./../../YOUR_MOD_HERE"
```
Once you run this option, Hammer should launch and provide you with the normal configuration prompt.

If you are running Hammer after previously using the program on Windows, you will have to edit your configurations to the correct filepaths. Make sure to point to the Windows executables, even for tools that have Linux-native versions, as Wine is not able to run Linux applications.

### Creating a Shell script
For ease of use, you may find it useful to create a Shell (`.sh`) script that automatically runs Hammer under wine. Here is an example of a script for Portal 2: Community Edition named `hammer.sh` located in `/bin/linux64/`.:
```
echo "Launching Hammer under Wine"
cd "./../win64"
wine "./hammer.exe" -winecompat -game "./../../p2ce"
```
If placing this script somewhere other than `/bin/linux64`, then make sure to change `cd "..."` and `-game` to the appropriate path. When in doubt, use an absolute path.

When you create the file for the first time, you may need to give it permission to execute. This can be done by running this command:
```
sudo chmod +x "./hammer.sh"
```

## Common Issues / Fixes
This section should cover most of the issues most users have when setting up Hammer. If this guide does not solve your issue, as for help in your game's Discord server. Make sure to list what steps you have taken to attempt to solve the issue, and follow [Dont Ask to Ask](https://dontasktoask.com/)!

### "Setup file 'gameinfo.txt' doesn't exist in subdirectory" when launching
Typically, this occurs when a path in your configuration file is incorrect, especially if Hammer had previously been run on Windows. Make sure to edit your configuration file to update the paths.

If you do not see the Configurations window on startup because you only use one config, navigate to `<game>/hammer/cfg` and either delete or rename `gameconfig.txt`. This will recreate your game configuration file, that way Hammer will fully launch. Alternatively, you can manually edit the file to alter the paths to their correct location.
>![NOTE]
>Wine prefixes all paths with a fake drive letter, `Z:` by default, to maintiain compatibility with Windows filesystems. Make sure to add this to the beginning of all your paths for them to work correctly.

### My game looks washed out when ran from Hammer!
In some distros or Desktop Environments, when launching the game through the compilation can appear washed out or overbrightened when ran through Wine. This appears to be an issue with how some Desktop Environments, like Hyprland, interact with Wine applications, so the best way to remedy this issue is by running the game through Steam and manually running the map through the console.

### "Portal 2 is not installed" (Portal 2: Community Edition)
This error can occur for a variety of reasons, but usually it is because Portal 2 cannot be found by Steam. Make sure that Portal 2 is in fact installed and visible in your Steam library, then try Verifying the game files of both Portal 2 and Portal 2: CE. Next, try restarting Steam to reload your library. If this does not fix your issue, try moving your Portal 2 install to the same drive as your Portal 2: Community Edition install. If all else fails, contact a programmer with your issue.