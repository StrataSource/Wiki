---
layout: default
title: "Control: Label"
parent: Panorama
---

# Control: Label

The Label control is a simple text display.

## Example

```xml
<!-- Simple text -->
<Label text="Sample Text"/>

<!-- Localized strings -->
<Label text="#PORTAL2_NewGame"/>
```

## Properties

| Name | Type   | Description                                      |
| ---- | ------ | ------------------------------------------------ |
| text | string | The text to display                              |
| html | bool   | Whether or not the text should be parsed as html |

## Methods

### SetLocalizationString

Assign a localization string to the label

```javascript
myLabel.SetLocalizationString("PORTAL2_NewGame");
```

### SetProceduralTextThatIPromiseIsLocalizedAndEscaped

Yes that's an actual function name. Assigns raw text to a label. Use with
caution.

```javascript
myLabel.SetProceduralTextThatIPromiseIsLocalizedAndEscaped(
  "Some text that should not be processed"
);
```
