---
title: Enums
weight: 30
---

# Enums

This page outlines the various Strata Hammer AngelScript enums.

## `GuiElement`

```as
enum GuiElement
{
  Label = 0,
  TextBox = 1 << 0,
  Divider = 1 << 1
}
```

## `InitTexFlags`

```as
enum InitTexFlags
{
  INIT_TEXTURE_FORCE = 1,
  INIT_TEXTURE_AXES = 2,
  INIT_TEXTURE_ROTATION = 4,
  INIT_TEXTURE_SHIFT = 8,
  INIT_TEXTURE_SCALE = 16,
  INIT_TEXTURE_ALL = 30
}
```

## `PrimitiveType`

```as
enum PrimitiveType
{
  MATERIAL_LINES = 1,
  MATERIAL_TRIANGLES = 2,
  MATERIAL_LINE_LOOP = 5,
  MATERIAL_POLYGON = 6,
  MATERIAL_QUADS = 7
}
```

## `RenderMode`

```as
enum RenderMode
{
  RENDER_MODE_WIREFRAME = 4,
  RENDER_MODE_FLAT = 5,
  RENDER_MODE_TRANSLUCENT_FLAT = 9,
  RENDER_MODE_TEXTURED = 10,
  RENDER_MODE_TEXTURED_SHADED = 14
}
```

## `TextureAlignment`

```as
enum TextureAlignment
{
  TEXTURE_ALIGN_NONE = 0,
  TEXTURE_ALIGN_WORLD = 1 << 0,
  TEXTURE_ALIGN_FACE = 1 << 1
}
```
