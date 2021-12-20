---
layout: default
title: GameInfo.txt Format
parent: Modding
---

# New GameInfo.txt

In order to support the new filesystem changes in Chaos, modifications have been
made to Source's existing GameInfo.txt format.

## Mounts Block

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

## Other Considerations

When making a P2CE mod, you should omit the `gamebin` entry from the
`SearchPaths` block. This will cause the game to attempt to load binaries from
your mod's bin directory instead of P2CE's.
