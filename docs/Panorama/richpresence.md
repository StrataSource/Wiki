---
layout: default
title: "API: Rich Presence"
parent: Panorama
---

# Rich Presence API

The rich presence API allows you to interact with Steam and Discord statuses. This is used by
P2CE to set a "Idling in XXX Menu" presence on Discord and Steam.

## API

| Function | Description |
| --- | --- |
| RichPresenceAPI.SetDiscordState(js\_object) | Sets the Discord rich presence status | 
| RichPresenceAPI.SetSteamState(js\_object) | Sets the Steam rich presence status (Not currently implemented) |
| RichPresenceAPI.Clear() | Clears all rich presence state and statuses |

## Example Usage

```js
// Update the discord rich presence info
var state = {
	'state': 'Idling',
	'name': 'P2CE',
	'details': 'Main Menu',
	'assets': {
		'large_image': 'logo_square',
		'small_text': 'Portal 2: Community Edition'
	}
}
RichPresenceAPI.UpdateDiscordState(state);
```

