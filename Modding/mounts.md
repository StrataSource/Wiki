# Configuring Mounts

Mounting configuration is now done via `<game>/cfg/mounts.kv` instead of through the GameInfo.txt. 
This allows greater flexibility when configuring mounts, and is generally safer than directly editing your GameInfo.txt 

## Format

The root of the mounts.kv should be a key called `Mounts`, which contains a list of `SteamApp` blocks, which specify 
dynamic search paths loaded via Steam.

Example of the format is below:
```
"Mounts"
{
	// Mounts portal2 
	SteamApp
	{
		AppID		620
		Required 	1
		
		SearchPath 	update
		SearchPath 	portal2_dlc2 
		SearchPath 	portal2_dlc1
		SearchPath 	portal2
	}
}
```

### `Mounts` block

This is just an array of `SteamApp` blocks. Other data inside of it will be ignored. 

### `SteamApp` block

The SteamApp block specifies a Steam application to dynamically mount. 

#### `AppID` property

This is an integer representing the AppID of the app to mount

#### `Required` property

This is an integer (technically boolean) that specifies if this mount is required or not. If required and the mount fails to load, the game will report
and error and exit.

#### `SearchPath` property

String representing a path relative to the mounted app's folder that should be added to the search path. 

#### `ToolsOnly` property

This is an integer representing if this app should only be mounted when running the game with tools mode or when running hammer.

#### `GameOnly` property

This is an integer representing if the app should only be mounted when running the game normally.
