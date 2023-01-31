---
layout: default
title: VScript Integration
parent: Panorama
features:
  - USE_VSCRIPT
---

# VScript Integration

When Panorama is enabled, a new `SendToPanorama` function is added to the
VScript API. This functions takes two parameters, the name of an event and an
additional value to be sent to JavaScript (currently only strings are
supported), and dispatches a global Panorama event with the given name and
argument.

# Usage Example

First the event needs to be defined in `eventdefinition.js`:

```js
$.DefineEvent("MyCustomEvent", 1, "content", "Custom VScript event");
```

Then in any Panorama JS file a global event handler can be attached to it:

```js
$.RegisterForUnhandledEvent("MyCustomEvent", function (content) {
  // Do something with the content
});
```

Finally the event can be dispatched from a VScript file:

```
function OnBtnPressed() {
    SendToPanorama("MyCustomEvent", "Event Content")
}
```
