---
title: Javascript Modules
weight: 0
---

# Javascript Modules

Strata Source Panorama supports a subset of the ECMAScript modules specification. This can be used to create cleaner and more modular code by reusing script exports without introducing clutter into the panel scope.

Just as non-module code is treated, script modules are reimported with a fresh instance for each panel. If a single module is used between multiple panels, each panel will get its own instance. If multiple scripts in a single panel reuse the same import, they will share the same instance.

> [!NOTE]
> Dynamic imports, import.meta, and top-level awaits are unsupported.

> [!NOTE]
> It should be noted that all of the below works with Typescript, and substituting the `.js` extensions with `.ts` will cause the code to be transpiled and cached by the engine prior to execution.

## Example

To expose a function or variable, the `export` syntax can be used.

```js :: scripts/utils/math.js
export function square(x) {
	return x ** 2;
}
```

To use these exported properties, an import can be declared with the `import` syntax. Absolute paths will be resolved relative to the `scripts/` directory, and relative import paths will be resolved relative to the current file.

```js :: scripts/utils/saysquare.js
import { square } from './math.js';

export function saySquare(x) {
	$.Msg(`The square of ${x} is ${square(x)}!`);
}
```

Similarly to how modules are declared on the web, scripts should be imported with `type="module"` in the xml to inform the engine that it should be parsed as a module.

```xml
<include type="module" src="file://{scripts}/utils/saysquare.js" />
```

Unfortunately, this example currently does nothing. Despite declaring and exporting our function, we don't have a way to attach the function to an event handler yet.

There are multiple ways of connecting the panel and script(s) - so we'll look at the simplest.

## Basic Panel interactivity

When declaring scripts as modules, variables are no longer implicitly exposed to the panel scope. Any variables that panels should interact with must be exposed by setting it as a property on the context object.

The context object is used as the script context when evaluating code that is embedded in panel tags in the xml, and is accessible through the `$.GetContextObject()` method.

```js :: scripts/components/mypanel.js
import { saySquare } from 'utils/saysquare.js';

const context = $.GetContextObject();

context.sayHelloAndSquare = function() {
	$.Msg('Hello!');
	saySquare(5);
}
```

```xml :: layout/components/mypanel.xml
<root>
	<scripts>
		<include type="module" src="file://{scripts}/components/mypanel.js" />
	</scripts>
	<Panel>
		<TextButton text="Test Button" onactivate="sayHelloAndSquare()" />
	</Panel>
</root>
```

While exposing each variable by hand works for basic cases, it can become tedious and messy when dealing with more, larger scripts. For this reason, it is recommended to expose either a class instance or a static class to avoid the repetition of individually exporting every method.

```js :: scripts/components/mypanel.js
import { saySquare } from 'utils/saysquare.js';

class MyPanelHandler {
	constructor() {
		$.RegisterEventHandler('PanelLoaded', $.GetContextPanel(), () => this.onPanelLoaded());
	}

	onPanelLoaded() {
		$.Msg('Panel loaded!');
	}

	saySquare(x) {
		return saySquare(x);
	}

	sayHello() {
		$.Msg('Hello from MyPanelHandler!');
	}
}

// This name is arbitrary, but using
// consistent names can help keep your code clean!
$.GetContextObject()['MyPanelHandler'] = new MyPanelHandler();
```

```xml :: layout/components/mypanel.xml
<!-- ... -->
	<TextButton text="Square of 5" onactivate="MyPanelHandler.saySquare(5)" />
	<TextButton text="Hello" onactivate="MyPanelHandler.sayHello()" />
<!-- ... -->
```

## Advanced Panel Interactivity

For those who are Typescript-savvy, class decorators can also be used to automate this process, slimming down the required code for each panel even more. See Momentum Mod's `module-helpers.ts` for an implementation of this method.

```ts :: scripts/components/mypanel.ts
import { saySquare } from 'utils/saysquare.ts';

@PanelHandler()
class MyPanelHandler {
	onPanelLoad() {
		$.Msg('Panel Loaded!');
	}

	saySquare(x: number) {
		return saySquare(x);
	}

	sayHello() {
		$.Msg('Hello from MyPanel!');
	}
}
```

## Further Reading

- [Javascript Modules on MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
- [Momentum's module-helper.ts](https://github.com/momentum-mod/panorama/blob/274c5782eaca5bcd3d57ff6fd1c0e7ac4639cf58/scripts/util/module-helpers.ts#L98-L135)
