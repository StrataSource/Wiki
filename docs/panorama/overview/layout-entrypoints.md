---
title: Layout Entrypoints
---

# Layout Entrypoints

The game loads many XML files by hard-coded paths. The following is a collection of hard-coded XML paths and relevant information.

## pages/intro-movie.xml

> Loaded on game startup to display the intro movie.

## pages/main-menu.xml

> The game menus, loaded after the intro movie. This functions as both the main menu(s) and pause menu.
>
> The game menus are expected to respond to the following global events:
> - `ShowMainMenu`
> - `HideMainMenu`
> - `ShowPauseMenu`
> - `HidePauseMenu`
>
> The current state of the game menus can also be queried by calling `GameInterfaceAPI.GetGameUIState()`, which returns a value of the [`GameUIState` enum](https://github.com/StrataSource/pano-typed/blob/main/shared/enums.d.ts#L17).
> 
> The menu can request the game to pause or unpause by emitting the global `MainMenuPauseGame`/`MainMenuResumeGame` events.

## pages/console.xml

> The game console.

> [!WARNING]
> Be careful when overriding this, as bad code can render the console unusable!

## pages/loading-screen.xml

> The loading screen, shown during map loads and initialized when a map is first loaded. After loading, the game adds the `.loading-screen--closing` CSS class to the `LoadingScreen` element.
> 
> The loading screen is expected to respond to the following global events:
> - `UnloadLoadingScreenAndReinit`
> 	- Called when the loading screen should re-initialize, such as when a map load is triggered.
> - `PopulateLoadingScreen`
> 	- Called directly after the above, indicating that the loading screen should update its contents. The map name is provided as a string argument.

## hud/hud.xml

> The HUD elements visible in-game. This contains elements such as the `showpos` position overlay, console messages overlay, and the weapons HUD.
