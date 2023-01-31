---
layout: default
title: Event System
parent: Panorama
nav_order: 100
---

# Event System
Panorama uses an event system to communicate between the engine and panels but also between panels. They can be defined and subscribed to via Javascript.

## Defining Events
```
**TODO** What is the difference between these two functions
```
You can define your own global events within the ``scripts/util/event-definition.js`` file by calling the ``$.DefineEvent`` and ``$.DefinePanelEvent`` functions.

### Example
```js
$.DefineEvent("LoadTutorialMap", 0);  // Event "LoadTutorialMap" with no arguments
$.DefineEvent("LoadStoryMap", 1);     // Event "LoadStoryMap" with one argument
```

## Subscribing to Events
Any panel can subscribe to an event by calling ``$.RegisterForUnhandledEvent`` or ``$.RegisterEventHandler`` within JavaScript. These functions will be called, when the event is fired. Some events may include additional parameters, which will be forwarded to your function.

#### $.RegisterForUnhandledEvent(``EVENT_NAME``, ``CALLBACK``)
This function can be used to subscribe to events.

#### $.RegisterEventHandler(``EVENT_NAME``, ``CONTEXT``, ``CALLBACK``)
This function can be used to subscribe to events within a specific context. This context can be another panel or its own panel by calling ``$.GetContextPanel()``.

### Example
```js
class MainMenu {
  static {
    $.RegisterForUnhandledEvent("ChaosShowPauseMenu", this.onShowPauseMenu.bind(this));
    
    // Custom Event with a parameter
    $.DefineEvent("LoadMap", 1);
    $.RegisterForUnhandledEvent("LoadMap", this.playMap.bind(this));
  }
  
  static onShowPauseMenu() {
    // ...
  }
  static playMap(map) {
    // [map] contains the parameters value
  }
}
```

## Dispatching Events
Events can be dispached via JavaScript by calling ``$.DispatchEvent``.

### Example
```js
$.DispatchEvent("LoadTutorialMap"); // Event "LoadTutorialMap" with no arguments
$.DispatchEvent("LoadStoryMap", "sp_a1_intro1"); // Event "LoadStoryMap" with one argument
```

## Global Events
Global events are events that are defined on an engine level. These events are usually prefixed by ``Chaos`` and are fired at various engine related events.

### Event Reference

| Event Name                       | Parameters | Description                                                       |
|----------------------------------|------------|-------------------------------------------------------------------|
| `ChaosShowMainMenu`              | *None*     | Shows the main menu.                                              |
| `ChaosHideMainMenu`              | *None*     | Hides the main menu.                                              |
| `ChaosShowPauseMenu`             | *None*     | Shows the pause menu.                                             |
| `ChaosHidePauseMenu`             | *None*     | Hides the pause menu.                                             |
|                                  |            |                                                                   |
| `ChaosMainMenuPauseGame`         | *None*     | Pauses the game.                                                  |
| `ChaosMainMenuResumeGame`        | *None*     | Resumes the game if paused.                                       |
|                                  |            |                                                                   |
| `ChaosShowIntroMovie`            | *None*     | Display the intro movie.                                          |
| `ChaosHideIntroMovie`            | *None*     | Hides the intro movie (Can also be used to skip the intro movie). |
|                                  |            |                                                                   |
| `ChaosVideoSettingsInit`         | *None*     | Initialized video settings                                        |
| `ChaosVideoSettingsResetDefault` | *None*     | Resets the video settings to default                              |
| `ChaosApplyVideoSettings`        | *None*     | Applies the video settings                                        |

## Further documentation
[Panorama/Events on Valve Developer Community](https://developer.valvesoftware.com/wiki/Dota_2_Workshop_Tools/Panorama/Events)