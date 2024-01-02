---
layout: default
title: PBR
---
*(NOTE: WIP. Parameters will be reorganized to make more sense in the future.)*

# PBR

## Parameters

### `$flags` \<int\>

Default: `0`

flags

### `$flags2` \<int\>

Default: `0`

flags2

### `$color` \<color\>

Default: `[1 1 1]`

color

### `$alpha` \<float\>

Default: `1.0`

alpha

### `$basetexture` \<texture\>

Default: `shadertest/BaseTexture`

Base Texture with lighting built in

### `$frame` \<int\>

Default: `0`

Animation Frame

### `$basetexturetransform` \<matrix\>

Default: `center .5 .5 scale 1 1 rotate 0 translate 0 0`

Base Texture Texcoord Transform

### `$flashlighttexture` \<texture\>

Default: `effects/flashlight001`

flashlight spotlight shape texture

### `$flashlighttextureframe` \<int\>

Default: `0`

Animation Frame for $flashlight

### `$color2` \<color\>

Default: `[1 1 1]`

color2

### `$srgbtint` \<color\>

Default: `[1 1 1]`

tint value to be applied when running on new-style srgb parts

### `$basetexture2` \<texture\>

Default: `shadertest/lightmappedtexture`

Blended texture

### `$frame2` \<int\>

Default: `0`

frame number for $basetexture2

### `$alphatestreference` \<float\>

Default: `0`



### `$envmap` \<texture\>

Default: ``

Set the cubemap for this material.

### `$envmapframe` \<int\>

Default: ``

Frame number for $envmap.

### `$mraotexture` \<texture\>

Default: ``

Texture with metalness in R, roughness in G, ambient occlusion in B.

### `$mraoframe` \<int\>

Default: ``

Frame number for $mraotexture.

### `$mraotexture2` \<texture\>

Default: ``

Texture with metalness in R, roughness in G, ambient occlusion in B.

### `$mraoframe2` \<int\>

Default: ``

Frame number for $mraotexture2.

### `$emissiontexture` \<texture\>

Default: ``

Emission texture

### `$emissionframe` \<int\>

Default: ``

Frame number for $emissiontexture.

### `$emissiontexture2` \<texture\>

Default: ``

Emission texture

### `$emissionframe2` \<int\>

Default: ``

Frame number for $emissiontexture2.

### `$normaltexture` \<texture\>

Default: ``

Normal texture (deprecated, use $bumpmap)

### `$bumpmap` \<texture\>

Default: ``

Normal texture

### `$bumpframe` \<int\>

Default: ``

Frame number for $bumpmap.

### `$bumpmap2` \<texture\>

Default: ``

Normal texture

### `$bumpframe2` \<int\>

Default: ``

Frame number for $bumpmap2.

### `$parallax` \<bool\>

Default: `0`

Use Parallax Occlusion Mapping.

### `$parallaxdepth` \<float\>

Default: `0.0030`

Depth of the Parallax Map

### `$parallaxcenter` \<float\>

Default: `0.5`

Center depth of the Parallax Map

### `$mraoscale` \<color\>

Default: `[1 1 1]`

Factors for metalness, roughness, and ambient occlusion

### `$mraoscale2` \<color\>

Default: `[1 1 1]`

Factors for metalness, roughness, and ambient occlusion

### `$emissionscale` \<color\>

Default: `[1 1 1]`

Color to multiply emission texture with

### `$emissionscale2` \<color\>

Default: `[1 1 1]`

Color to multiply emission texture with

### `$hsv` \<color\>

Default: `[1 1 1]`

HSV color to transform $basetexture texture with

### `$hsv_blend` \<bool\>

Default: `0`

Blend untransformed color and HSV transformed color

### `$brdf_integration` \<texture\>

Default: ``



### `$envmapparallax` \<matrix\>

Default: `[1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1]`



### `$envmaporigin` \<vec3\>

Default: `[0 0 0]`

The world space position of the env_cubemap being corrected

### `$blendtintbymraoalpha` \<bool\>

Default: `0`

Blend tint by the alpha channel in MRAO texture. Similar to $blendtintbybasealpha for VLG

### `$paintsplatnormalmap` \<texture\>

Default: `paint/splatnormal_default`

The paint splat normal map to use when paint is enabled on the surface

### `$paintsplatbubblelayout` \<texture\>

Default: `paint/bubblelayout`

The layout texture which defines the distribution of bubbles in the paint

### `$paintsplatbubble` \<texture\>

Default: `paint/bubble`

The normal mapped texture of a single bubble

### `$paintenvmap` \<texture\>

Default: `paint/paint_envmap_hdr`

Envmap that is consistent across all surfaces

## Example

```
PBR
{
	$color               "[1 1 1]"
	$alpha               "1.0"
	$basetexture         "shadertest/BaseTexture"
	$frame               "0"
	$basetexturetransform "center .5 .5 scale 1 1 rotate 0 translate 0 0"
	$flashlighttexture   "effects/flashlight001"
	$flashlighttextureframe "0"
	$color2              "[1 1 1]"
	$srgbtint            "[1 1 1]"
	$basetexture2        "shadertest/lightmappedtexture"
	$frame2              "0"
	$alphatestreference  "0"
	$envmap              ""
	$envmapframe         ""
	$mraotexture         ""
	$mraoframe           ""
	$mraotexture2        ""
	$mraoframe2          ""
	$emissiontexture     ""
	$emissionframe       ""
	$emissiontexture2    ""
	$emissionframe2      ""
	$normaltexture       ""
	$bumpmap             ""
	$bumpframe           ""
	$bumpmap2            ""
	$bumpframe2          ""
	$parallax            "0"
	$parallaxdepth       "0.0030"
	$parallaxcenter      "0.5"
	$mraoscale           "[1 1 1]"
	$mraoscale2          "[1 1 1]"
	$emissionscale       "[1 1 1]"
	$emissionscale2      "[1 1 1]"
	$hsv                 "[1 1 1]"
	$hsv_blend           "0"
	$brdf_integration    ""
	$envmapparallax      "[1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1]"
	$envmaporigin        "[0 0 0]"
	$blendtintbymraoalpha "0"
	$paintsplatnormalmap "paint/splatnormal_default"
	$paintsplatbubblelayout "paint/bubblelayout"
	$paintsplatbubble    "paint/bubble"
	$paintenvmap         "paint/paint_envmap_hdr"
}
```

