---
title: Code blocks
---

```yml
hello: worlddddddddddddddddddddddddddddddddddddddddddddd aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
```

```json
[
  {
    "title": "apples",
    "count": [12000, 20000],
    "description": {"text": "...", "sensitive": false}
  },
  {
    "title": "oranges",
    "count": [17500, null],
    "description": {"text": "...", "sensitive": false}
  }
]
```


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
