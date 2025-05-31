---
title: VScript Integration
features:
  - USE_VSCRIPT
---

# VScript Integration

When Panorama is enabled, a new `SendToPanorama` function is added to the
VScript API. This functions takes two parameters, the name of an event and an
additional value to be sent to JavaScript (currently only strings are
supported), and dispatches a global Panorama event with the given name and
argument.

## Usage Example

First, the event needs to be defined in `scripts/util/event-definition.ts`:

```js
$.DefineEvent("MyCustomEvent", 1, "content", "Custom VScript event");
```

Then a global event handler can be attached to it in any Panorama JS file:

```js
$.RegisterForUnhandledEvent("MyCustomEvent", function (content) {
  // Do something with the content
});
```

Finally the event can be dispatched from a VScript file:

```squirrel
function OnBtnPressed() {
    SendToPanorama("MyCustomEvent", "Event Content")
}
```

## TypeScript Compatibility

When using Typescript with the Strata types library, it is expected that all events should be declared alongside their parameter types. Events can be added by re-declaring the `PanelEventNameMap`/`GlobalEventNameMap` interfaces with only your custom events. This will merge the interface rather than override it.

```ts
interface GlobalEventNameMap {
	'MyCustomEvent': (myNumericArg: number) => void;

	// This example can also be shortened down with function syntax:
	// MyCustomEvent(myNumericArg: number): void;
}
```

These checks can also be disabled by declaring the `ALLOW_MISSING_EVENTS` type as `true`.
