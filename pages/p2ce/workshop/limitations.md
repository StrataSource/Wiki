---
title: Addon Limitations
---
# Addon Limitations
Addons can be very powerful, however there are some limitations to take into account when creating addons. 
## 1. Addons cannot include autoexec.cfg
`autoexec.cfg` can only be run from the base mod directory, and as such any autoexecs present in addons are not run on startup, which can prove to be an issue for a few mappacks that edit portal colors or keybindings. However, some workarounds can be implemented.
### Option 1: Automatically executing a vScript file upon loading each map
You can create a vScript to be called upon loading up each map in the series. Remember to execute this with a little delay, as there is a small time where the map is loaded but the player does not exist yet.
### Option 2: Honor system
You can also create a `.cfg` file that players must manually execute when the game starts up that does all this automatically. This can be slightly annoying for some users, however, and should not be done unless all else fails.
## 2. Addons cannot include mounts.kv
Because of a similar reason to before, `mounts.kv` is only read from the base mod path and not the addon. Unfortunately, the only way to fix this is by telling the users to manually mount the required game in their `mounts.kv` file. 
## 3. Any content in the user's `p2ce\custom` folder will override your addon content
There is no known fix for this, other than to tell users to remove any content present in their custom folder before using your addon for the intended effect.
## 4. Addons cannot override UI
UI is only read from the base mod path, so there is no way to override UI files. 

## Fix for Everything
If all else fails and you *absolutely* need all these features, the best way to fix all these issues is by telling the users to Symoblic Link their files to `SteamApps\sourcemods\addon_name_here` to get the proper effect. This is how [Black Mesa: Blue Shift](https://steamcommunity.com/sharedfiles/filedetails/2424633574) does this, as Black Mesa's workshop works similarly to Portal 2: Community Edition's. 
***TODO: DOCUMENT THIS PROCESS***
