---
title: vfont
---

# vfont

vfont is a compiler/decompiler for Valve's encrypted font files. Unlike previous branches, `vfont` is combined into a single executable that does both compilation and decompilation. This tool is available for Windows and Linux.

## Help Text

```
----------------------------------------------------------------------------------
vfont - Copyright Valve Software (Aug 28 2022)
Usage: vfont inputFontFilename [outputFontFilename]

Example Usage:
Convert from a TTF to a vfont: vfont font.ttf
Convert from a vfont to a TTF: vfont font.vfont
Custom output name:            vfont filename.ttf otherfilename.vfont
----------------------------------------------------------------------------------
```

## Examples

Example 1: Decompiling a vfont file. Output will be `myfont.ttf`
```
vfont myfont.vfont
```