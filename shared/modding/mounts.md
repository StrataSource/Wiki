---
layout: default
title: Configuring Mounts
parent: Modding
---

# Configuring Mounts

Mounting configuration is now done via `<game>/cfg/mounts.kv` instead of through
the GameInfo.txt. This allows greater flexibility when configuring mounts, and
is generally safer than directly editing your GameInfo.txt file.

# Format

The root of the mounts.kv should be a key called `Mounts`, which contains a list
of `AppID` blocks, which specify dynamic search paths loaded via Steam.

Example of the format is below:

```
"Mounts"
{
	"620" // AppID ("620" is Portal 2)
	{
		"required" 	"0"
		"head"		"0"

		"portal2" // mod_folder, folder inside of the given AppID (Portal 2)'s folder. In this case, <portal 2 install>\portal2\
		{
			"mountmoddir" "0"
			"vpk"	"pak01_dir" // mounts VPK: <Portal 2 install>\portal2\pak01_dir.vpk
			"dir"	"custom" // mounts folder: <Portal 2 install>\portal2\custom\
		}

		"update" // mod_folder, <portal 2 install>\update\
		{
			"vpk" "pak01_dir"
		}

		"portal2_dlc2" // mod_folder, <portal 2 install>\portal2_dlc2\
		{
			"vpk" "pak01_dir"
		}

		"portal2_dlc1" // mod_folder, <portal 2 install>\portal2_dlc1\
		{
			"vpk" "pak01_dir"
		}
	}
}
```

## `Mounts` block

This is just an array of `AppID` blocks. Other data inside of it will be
ignored.

## `AppID` block

The AppID block specifies a Steam application to dynamically mount. The value of
the name of the block is the particular AppID to mount. 620 is Portal 2, 220
HL2, and so on.

## `required` property

This is an integer, 0 or 1, that specifies if this mount is required or not. If
required and the mount fails to load, the game will report and error and exit.

## `head` property

This is an integer, 0 or 1, that determines if the desired AppID mount should be
added to the head of the mount list.

In other words, should this AppID's mount be searched above all other folders?

## `mod_folder` property

String representing the folder inside of the AppID's install folder to mount. In
the case of older games, this is typically just one: "cstrike", or "hl2".

For games like Portal 2, as seen in the example, this can be multiple.
"portal2", "portal2_dlc1", "update" etc.

## `vpk` property

This string value is a VPK file to mount inside of the given `mod_folder`.

It is ideal to mount each of the `<filename>_dir.vpk` (VPK directory) files
here, rather than every single VPK file in the folder.

## `dir` property

This string value is a subfolder inside of `mod_folder` that is mounted.

For older games such as TF2 and CS:S, you may want to mount the `download` or
`custom` folders here alongside the VPKs.

## `mountmoddir` property

This is an integer, 0 or 1, that determines if the `mod_folder` gets added as
search path.

The default is 1 if omitted, which causes all maps/textures/sounds/etc. shipped
as loose files with the mod to be mounted and appear in-game. It will only be
considered for searches after the VPKs and subfolders specified in this block.

Setting it to 0 instead will still mount all contained `vpk` and `dir` blocks
but **not** the `mod_folder`.
