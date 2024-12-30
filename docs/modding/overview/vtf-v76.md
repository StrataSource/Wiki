---
title: VTF v7.6 Format
---

# VTF Version 7.6

VTF v7.6 is Strata Source's modified VTF format that adds a few new image formats, as well as optional CPU compression.
This document goes over all additions to the format.

No changes have been made to the header's fields. The header is identical to VTF v7.5.

## New Texture Formats

A few new texture formats are present in Strata Source. These will technically work in any VTF version loaded by a Strata Source
game, but it is recommended to only use them in v7.6 VTFs so there isn't any confusion about why the textures will not work in
older Source engine games.

| Name   | Value | Description                                                                                                                                                              |
| ------ | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `R8`   | `69`  | Identical to `I8`, except where `I8` is treated as greyscale `R8` is purely a red channel. No practical benefit to using this format outside internal engine operations. |
| `BC7`  | `70`  | This format is recommended as a replacement for `DXT5`. The alpha channel is optional.                                                                                   |
| `BC6H` | `71`  | Used to store cubemaps, and recommended for HDR textures. This is the signed half-float variant.                                                                         |

## New Resources

There is one new resource in VTF v7.6. The "Auxiliary Compression Info" resource (`AXC` identifier) controls CPU compression
of texture data. The first version of this resource is supported by all Strata Source games, and has the following structure,
excluding the length integer present in every non-legacy resource:

```cpp
struct AXC_v1 {
    uint32_t compression_strength;
    uint32_t compressed_sizes[mip_count * frame_count * face_count];
};
```

The only supported compression method for this version is [Deflate](https://en.wikipedia.org/wiki/Deflate). The compression
strength can be `-1` (default compression strength), `0` (no compression was applied), or `1-9` (specific compression strength).
If the compression strength is `0` the VTF is assumed to be uncompressed and the resource is ignored.

The compressed sizes array is structured similarly to how VTF texture data is structured. In pseudocode:

```
for each mip level:
    for each frame:
        for each face:
            uint32_t compressed_size
```

The array stores the compressed size of each piece of texture data. They are compressed separately to avoid having to decompress
the entire VTF every time a different part of it is accessed. 3D textures (textures with more than one slice) are compressed as one
unit rather than compressing each individual slice. The uncompressed size can be calculated from the texture dimensions and format.
To calculate the offset of a texture into the image resource at a given mip, frame, and face, the size of every compressed texture
before it must be added together.

The second and most recent version of the `AXC` resource introduces a field to control the compression method, and adds support for
[Zstandard](https://facebook.github.io/zstd/) compression. The structure of the resource is now:

```cpp
// These values match minizip defines, but keep in
// mind they are the only ones supported right now
uint16_t METHOD_DEFLATE = 8;
uint16_t METHOD_ZSTD = 93;

struct AXC_v2 {
    uint16_t compression_strength;
    uint16_t compression_method;
    uint32_t compressed_sizes[mip_count * frame_count * face_count];
};
```

The version of the `AXC` resource can be determined using the compression method field. If the field is less than or equal to `0`,
the resource is the original, and the compression method is known to be Deflate. If the field is either `8` or `93` (the only supported
values currently) then the resource is the second iteration, and the value can be relied on to determine the compression method.
If the compression method lies outside this domain the VTF is malformed.

> [!REVOLUTION]
> The second version of this resource is unsupported in Portal: Revolution when compressing with Zstandard. Portal: Revolution is expecting
> the original version of the resource, and cannot decode Zstandard compression. Due to the resource's forwards and backwards compatibility
> however, as long as Deflate compression is specified when creating a compressed VTF Portal: Revolution will support that VTF, even though
> it may be using the updated resource definition.
