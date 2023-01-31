---
layout: default
title: GameInfo.txt Format
parent: Modding
---

# New GameInfo.txt Format

In order to support the new filesystem changes in Chaos, modifications have been
made to Source's existing GameInfo.txt format.

# Mounts Block

The mounts block is designed to supplement the user-editable mounts.kv file in
cfg. This block should be used to setup the required paths for your mod.

This block should be placed in the `"GameInfo"` block like everything else.

An example of the mounts block:

```
mount
{
	// The AppID of your mod
	620
	{
		"required" "1" // If 1, the game will not launch if this couldn't be mounted.
		"head" "0" // If 1, this will add the search path to the head of the list

		// 'update' is the name of the folder to look in
		"update"
		{
			"vpk" "pak01" // The vpk directive tells the engine to look for update/pak01_XXX.vpk
		}

		"portal2_dlc2"
		{
			"vpk" "pak01" // Add portal2_dlc2/pak01_XXX.vpk
			"dir" "maps" // Add the portal2_dlc2/maps directory to the search path
			"dir" "models" // Add the portal2_dlc2/models directory to the search path
		}

		"portal2_dlc1"
		{
			"vpk" "pak01"
		}

		"portal2"
		{
			"vpk" "pak01"
		}
	}
}
```

# Custom Folder

Chaos supports many Source 2013/TF2-style constructs in the gameinfo, such as the custom folder.

To support the custom folder, simply add `game "<your mod>/custom/*"` to your `SearchPaths` block.
Anything under the `<your mod>/custom/` folder will be mounted as if it were a game.

# Other Considerations

* When making a P2CE mod, you should omit the `gamebin` entry from the
`SearchPaths` block. This will cause the game to attempt to load binaries from
your mod's bin directory instead of P2CE's.

* When adding p2ce to your gameinfo, add it as `game+mod`. Otherwise, the game will not be
able to find `steam.inf` unless your mod ships it.

# Example GameInfo.txt

The following is an example gameinfo.txt from our template mod repo found [here](https://github.com/ChaosInitiative/p2ce-mod-template)

```
"GameInfo"
{
	game 		"Portal 2: My Cool Template Mod"
	GameData	"p2ce.fgd"

	// Mounts content from Portal 2 and P2CE.
	// To add additional mounts, see cfg/mounts.kv

	mount
	{
		// Portal 2 is required for this mod
		620
		{
			"required" "1"

			// Priority is determined by the order
			// in which folders are defined.
			// For example, assets in "portal2_dlc1" will
			// be overridden by assets in "update"

			"update
			{
				"vpk" "pak01"
			}
			"portal2_dlc2"
			{
				"vpk" "pak01"
			}
			"portal2_dlc1"
			{
				"vpk" "pak01"
			}
			"portal2"
			{
				"vpk" "pak01"
			}
		}
	}

	FileSystem
	{
		SteamAppId				440000	// Identifies this as a P2CE mod.

		SearchPaths
		{
			Game+mod+default_write_path	|gameinfo_path|.

			// p2ce should be marked as a mod too so it can pull important files that are missing from your mod
			Game+mod			p2ce
			GameBin				p2ce/bin
			Game				hammer
			Game				update
			Platform+game		platform
		}
	}
}
```