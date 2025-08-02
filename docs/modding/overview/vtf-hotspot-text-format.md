---
title: Hotspot Text Format
---

# Hotspot Text Format

Alongside the embedded format, Strata Source supports the Hammer++ rect format, which is derived from Source 2's rect format. This format makes it possible to quickly manually create and edit hotspot information, as well as reuse them between multiple materials.

```kv :: example_rectmap.rect
Rectangles
{
	rectangle
	{
		min		"0 0"
		max		"512 32"
	}
	rectangle
	{
		min		"512 0"
		max		"768 32"
	}
}
```

```kv :: example_material.vmt
LightmappedGeneric
{
	$basetexture "example_material"
	%rectanglemap "example_rectmap"
}
```

Each rect region is contained in a `rectangle` inside the `Rectangles` set, and has the `min` and `max` properties at minimum. These values represent pixel positions in the image starting from the top left. Flag keyvalues can optionally be appended to the rectangle, which modify the behavior used when placing them.

Regions with the `alt` flag are excluded from the selection set by default, unless the `Alt` key is pressed, in which case they are exclusively selected. This allows a second set of regions to be defined within the same texture, which can be used for patterned trims or decorations.

```kv
rectangle
{
	min		"0 0"
	max		"256 256"
	rotate	1			// Should this region be randomly rotated?
	reflect	1			// Should this region be randomly horizontally flipped?
	alt		1			// If true, this region belongs to the alternate group.
}
```
