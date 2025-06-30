---
title: VTF Hotspot Resource
---

# VTF Hotspot Resource

Strata Hammer supports [Hotspot texturing](https://www.defaultinteractive.co.uk/post/hotspot-texturing), a technique which allows a single texture to contain many smaller rectangular regions which can then be automatically assigned to the faces of brushes. This allows for the rapid and detailed texturing of complex geometry.

The following specification introduces a standardized way of writing and reading hotspot textures, so that hotspot editing tools may be created that work seamlessly between Strata and other Source-based games.

## Hotspot Resource Specification

This specification describes the HotSpot resource for embedding in VTFs greater than version 7.2. All structs in this resource should be assumed to be byte-aligned without padding.

This resource does not include world texel-scaling information, and assumes that implementations will attempt to match rects with the default texture scale as defined in the user configuration.

Due to the need for compatibility across many games, this resource cannot rely on the VTF version for possible format changes, and instead contains its own version in the body.

## Header

This resource uses the UTF-8 tag "`+\0\0`" (`2B 00 00` in hexadecimal) for identification.

No additional flags are defined in the resource header flags field.

## Body

The resource body begins with the following header:

```cpp
struct HotspotHeader_t {
	unsigned char  version;    // The resource version. Currently 0x1
	unsigned char  flags;      // Implementation-specific flags for editors.
	unsigned short rect_count; // The number of rect regions.
};
```

Following immediately after are a contiguous array of rect regions. These regions use the following structure:

```cpp
struct HotspotRect_t {
	HotspotRectFlags_t flags; // See below section.
	unsigned short min_x;     // Coordinates are stored in pixels.
	unsigned short min_y;
	unsigned short max_x;
	unsigned short max_y;
};
```

Orientation randomization is defined within the flags of each rect. Although these are defined per-rect, it is recommended that editors implement batch editing for ease of use.

Regions with the `alt_group` flag should be excluded from random selection by default, and be exclusively randomly selected when an implementation-specific modifier key is active. For consistency, the left-hand Alt key is recommended for this purpose.

```cpp
enum class HotspotRectFlags_t : unsigned char {
	enable_rotation   = 0x1, // Can this region be randomly rotated?
	enable_reflection = 0x2, // Can this region be randomly horizontally flipped?
	alt_group         = 0x4, // If true, this region belongs to the alternate group.
};
```
