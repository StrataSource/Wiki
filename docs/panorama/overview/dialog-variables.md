---
title: Dialog Variables
---

# Dialog Variables

Dialog variables provide a quick and easy way to substitute text within a snippet or panel from your JavaScript code.

Certain dialog variable types provide additional modifiers that may be used to fine-tune output.

# JavaScript API

The following methods may be used to set a dialog variable on a `Panel`:
* `Panel.SetDialogVariable(variable: string, value: string)`
* `Panel.SetDialogVariableInt(variable: string, value: number)`
* `Panel.SetDialogVariableFloat(variable: string, value: number)`
* `Panel.SetDialogVariableTime(variable: string, value: number)`

# Formatting

Dialog variables are supplied in layout files in the format `{x:y:myname}`, where `x:` is the format, `y:` is the optional modifier, and `myname` is the name of your dialog variable.

There are two parts to the format string: the format and the modifier. The _format_ comes first and is **required**. The _modifier_ comes second and is optional, if supported.
When a format is provided without a modifer, it's in the format `{x:myname}`.

## String: `s`, `S`

Displays a formatted string.

### Modifiers

| Name | Description |
|---|---|
| `u` | Upper-case the string |
| `l` | Lower-case the string |
| `h` | HTML allowed in string |

### Examples

Use a dialog variable `mytest` in a `Label`:
```xml
<Label text="{s:mytest}"/>
```

Use a dialog variable `mytest` in a `Label`, and make it upper-case:
```xml
<Label text="{s:u:myupperstring}"/>
```

## Time: `t`, `T`

Displays a formatted time.

Use with `Panel.SetDialogVariableTime`.

### Modifiers

| Name | Description |
|---|---|
| `s` | Short date |
| `l` | Long date |
| `t` | Short time |
| `T` | Long time, with seconds |
| `r` | Relative time |
| `d` | Duration (i.e. 3 hours 40 minutes)  |
| `m` | Minutes |
| `e` | Server real time |

### Examples

Time duration:
```
{t:d:myvar}
```

Long date:
```
{t:l:mylongdate}
```

## Currency: `m`, `M`

Displays a formatted currency.

Use with `Panel.SetDialogVariableFloat`.

### Modifiers

None.

### Examples

None.

## Integers: `i`, `I`, `d`, `D`

Displays a formatted integer.

Use with `Panel.SetDialogVariableInt`.

### Modifiers

| Name | Description |
|---|---|
| `r` | Raw number |

### Examples

Simple integer format:
```
{d:myvar}
```

Raw integer format:
```
{i:r:myvar}
```

## Floating Point Numbers: `f`, `F`

Displays a formatted floating point number.

Use with `Panel.SetDialogVariableFloat`.

### Modifiers

None.

### Examples

Floating-point format:
```
{F:myfloat}
```

Also floating-point format:
```
{f:myfloat}
```

## Unsigned 64-bit Integers: `u`, `U`

Displays a formatted uint64.

Use with `Panel.SetDialogVariableInt`.

### Modifiers

None.

### Examples

UInt64 format:
```
{u:myuint64}
```

# Sample Code

The following example code demonstrates the usage of many different types of dialog variables.

```xml
<snippets>
    <snippet name="ExampleSnippet">
        <Panel class="full flow-down">
            <Label text="This is a float: {f:myfloat}"/>
            <Label text="This is a string: {s:mystring}"/>
            <Label text="This is an UPPER STRING: {s:u:myupperstring}"/>
            <Label text="This is a long date: {t:l:mytime}" />
            <Label text="This is an integer: {d:myint}" />
        </Panel>
    </snippet>
</snippets>
```

```js
// Create a panel and load the snippet
const panel = $.CreatePanel('Panel', null, 'test');
panel.LoadLayoutSnippet('ExampleSnippet');

// Set a bunch of dialog variables
panel.SetDialogVariableFloat('myfloat', 32.32);
panel.SetDialogVariable('mystring', 'Hello World!');
panel.SetDialogVariable('myupperstring', 'This text should be all caps');
panel.SetDialogVariableTime('mytime', 1); // January 1st, 1970
panel.SetDialogVariableInt('myint', -1);
```