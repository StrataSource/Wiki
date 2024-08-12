---
layout: default
title: PBR
---
# PBR
This page contains information about the parameters of the PBR shader. 

***Tip:** Use "Ctrl+F" to find a specific parameter you are looking for*
## Parameters
### Basics
#### `$basetexture` \<texture\>

&ensp;Default: `shadertest/BaseTexture`

&ensp;Description: Base texture with lighting built in.

#### `$basetexture2` \<texture\>

&ensp;Default: `shadertest/lightmappedtexture`

&ensp;Description: Blended texture for use with displacements

----
### Appearance
#### `$basetexturetransform` \<matrix\>

&ensp;Default: `center .5 .5 scale 1 1 rotate 0 translate 0 0`

&ensp;Description: Base Texture Texcoord Transform. Transforms the texture before use. Does not affect lightmaps.

#### `$color` \<color\>

&ensp;Default: `[1 1 1]`

&ensp;Description: Adjusts the color of $basetexture

#### `$color2` \<color\>

&ensp;Default: `[1 1 1]`

&ensp;Description: Adjusts the color of $basetexture2

#### `$frame` \<int\>

&ensp;Default: `0`

&ensp;Description: Sets what static frame to use if $basetexture is animated

#### `$frame2` \<int\>

&ensp;Default: `0`

&ensp;Description: Sets what static frame to use if $basetexture2 is animated

#### `$srgbtint` \<color\>

&ensp;Default: `[1 1 1]`

&ensp;Description: Tint value to be applied when running on new-style srgb parts

#### `$hsv` \<color\>

&ensp;Default: `[1 1 1]`

&ensp;Description: HSV color to transform $basetexture texture with

#### `$hsv_blend` \<bool\>

&ensp;Default: `0`

&ensp;Description: Blend untransformed color and HSV transformed color

----
### Flashlight
#### `$flashlighttexture` \<texture\>

&ensp;Default: `effects/flashlight001`

&ensp;Description: Flashlight spotlight shape texture

#### `$flashlighttextureframe` \<int\>

&ensp;Default: `0`

&ensp;Description: Sets what static frame to use if $flashlighttexture is animated

----
### Physically Based Rendering
#### `$model` \<bool\>

&ensp;Default: ``

&ensp;Description: Specifies if the material is intended for use on models or brushes. If set to 1, acts like VLG (phong for lights, no lightmaps). If set to 0, acts like LMG.

#### `$mraotexture` \<texture\>

&ensp;Default: ``

&ensp;Description: Texture with metalness in R, roughness in G, ambient occlusion in B for $basetexture

#### `$mraoframe` \<int\>

&ensp;Default: ``

&ensp;Description: Sets what static frame to use if $mraotexture is animated.

#### `$mraotexture2` \<texture\>

&ensp;Default: ``

&ensp;Description: Texture with metalness in R, roughness in G, ambient occlusion in B for $basetexture2

#### `$mraoframe2` \<int\>

&ensp;Default: ``

&ensp;Description: Sets what static frame to use if $mraotexture2 is animated.

#### `$mraoscale` \<color\>

&ensp;Default: `[1 1 1]`

&ensp;Description: Factors for metalness, roughness, and ambient occlusion for $mraotexture

#### `$mraoscale2` \<color\>

&ensp;Default: `[1 1 1]`

&ensp;Description: Factors for metalness, roughness, and ambient occlusion for $mraotexture2

#### `$parallax` \<bool\>

&ensp;Default: `0`

&ensp;Description: Enables [Parallax Occlusion Mapping](/modding/PBR/parallaxmapping).

#### `$parallaxdepth` \<float\>

&ensp;Default: `0.0030`

&ensp;Description: Depth of the Parallax Map. Essentially the intensity of the heightmap. 

#### `$parallaxcenter` \<float\>

&ensp;Default: `0.5`

&ensp;Description: Center depth of the Parallax Map. Essentially how far away from the face the center of the heightmapped material appears to be.

#### `$blendtintbymraoalpha` \<bool\>

&ensp;Default: `0`

&ensp;Description: Blend tint by the alpha channel in MRAO texture. Similar to $blendtintbybasealpha for [VLG](https://developer.valvesoftware.com/wiki/VertexLitGeneric)

----
### Alpha
#### `$alpha` \<float\>

&ensp;Default: `1.0`

&ensp;Description: Scales the transparency of the whole image

#### `$alphatestreference` \<float\>

&ensp;Default: `0`

&ensp;Description: Specifies the threshold alpha channel value at which the surface should be transparent instead of opaque. A value of ".3" will create a thicker shape while a value of ".7" will create a thinner shape.

----
### Emissive
#### `$emissiontexture` \<texture\>

&ensp;Default: ``

&ensp;Description: Emission texture

#### `$emissionframe` \<int\>

&ensp;Default: ``

&ensp;Description: Static frame to use if $emissiontexture is animated.

#### `$emissiontexture2` \<texture\>

&ensp;Default: ``

&ensp;Description: Emission texture for $basetexture2

#### `$emissionframe2` \<int\>

&ensp;Default: ``

&ensp;Description: Static frame to use if $emissiontexture2 is animated.

#### `$emissionscale` \<color\>

&ensp;Default: `[1 1 1]`

&ensp;Description: Color to multiply $emissiontexture with

#### `$emissionscale2` \<color\>

&ensp;Default: `[1 1 1]`

&ensp;Description: Color to multiply $emissiontexture2 with

----
### Reflection
#### `$envmap` \<texture\>

&ensp;Default: ``

&ensp;Description: Set the cubemap for this material.

#### `$envmapframe` \<int\>

&ensp;Default: ``

&ensp;Description: Static frame to use if $envmap is animated.

----
### Bumpmap
#### `$normaltexture` \<texture\>

&ensp;Default: ``

&ensp;Description: Normalmap texture (deprecated, use $bumpmap)

#### `$bumpmap` \<texture\>

&ensp;Default: ``

&ensp;Description: Bumpmap texture for $basetexture

#### `$bumpframe` \<int\>

&ensp;Default: ``

&ensp;Description: Static frame to use if $bumpmap is animated.

#### `$bumpmap2` \<texture\>

&ensp;Default: ``

&ensp;Description: Bumpmap texture for $bsaetexture2

#### `$bumpframe2` \<int\>

&ensp;Default: ``

&ensp;Description: Static frame to use if $bumpmap2 is animated.

----
### Paint
#### `$paintsplatnormalmap` \<texture\>

&ensp;Default: `paint/splatnormal_default`

&ensp;Description: The paint splat normal map to use when paint is enabled on the surface

#### `$paintsplatbubblelayout` \<texture\>

&ensp;Default: `paint/bubblelayout`

&ensp;Description: The layout texture which defines the distribution of bubbles in the paint

#### `$paintsplatbubble` \<texture\>

&ensp;Default: `paint/bubble`

&ensp;Description: The normal mapped texture of a single bubble

#### `$paintenvmap` \<texture\>

&ensp;Default: `paint/paint_envmap_hdr`

&ensp;Description: Envmap that is consistent across all surfaces
