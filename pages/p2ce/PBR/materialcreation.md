---
title: Creating PBR materials
---
(Note: WIP)
# Creating PBR materials
## Overview
The PBR workflow is much more complicated than the standard Source workflow. While most Source textures can be created with a simple image editing program like GIMP, PBR textures need many more textures, some of which cannot be made with a simple paintbrush or pattern tool (well, they can, but it's not recommended). These textures need specialized programs to create them, of which there are a couple of options. This page will not cover the creation of these textures, as many tutorials already exist on this topic. This page will however go over the creation of MRAO textures and the creation of the material file.
## Obtaining PBR textures
As stated before, PBR textures need to be created in specialized programs. If you do not possess a license to paid programs like Adobe or a computer powerful enough to run programs like Blender, some free and relatively easy-to-run programs exist like [Materialize](https://boundingboxsoftware.com/materialize/). Here is a list of textures needed to create a fully functional PBR material:
* [Metalness](https://help.poliigon.com/en/articles/1712652-texture-maps-explained#h_758312b1b2) map (Defines what parts of your material are metal)
* [Roughness](https://help.poliigon.com/en/articles/1712652-texture-maps-explained#h_e0063ea358) map (Defines the Roughness/Non-Reflectivity of parts of your material)
 
    ***IMPORTANT**: If the program you used to create these textures labels these as "Glossiness" or "Smoothness" maps, make sure you invert the colors before proceeding!*

* [Ambient Occlusion](https://help.poliigon.com/en/articles/1712652-texture-maps-explained#h_00c9ca0901) map (Specifies which areas of the texture are "behind", or always shaded. You can compare this to what an [SSBump](https://developer.valvesoftware.com/wiki/$ssbump) map accomplishes)
* [Bump](https://developer.valvesoftware.com/wiki/Bump_map) map *with optional Height map in alpha channel* (Standard bump map that is usually used with standard Source workflow, but it can optionally include a Height map in the alpha channel of the texture for [Parallax Mapping](/p2ce/PBR/parallaxmapping))
## Creating the MRAO texture
### What is "MRAO"?
A **M**etalness, **R**oughness, **A**mbient **O**cclusion map is a texture that contains the first 3 texture maps listed above in the RGB channels of the texture, respectively (Metalness on the Red channel, Roughness in the Green, AO in the Blue). This texture is used to compress the usually 3 needed maps down into one to free up drive space. While this might not seem like much space, this quickly adds up the more PBR materials your game/mod contains. While most programs do not contain a simple button that does this for you, there are very easy ways to create this texture with basic programs like [GIMP](https://www.gimp.org/), or with specialized programs like [PBR-2-Source](https://koerismo.digital/projects#pbr-2-source). 
### Method 1: GIMP
GIMP can combine different layers into the RGBA channels of one texture, which makes creating MRAO maps using GIMP trivial. First, create a new image with the dimensions of your texture maps. Next, go to file and click "Import as layers...", select your Metalness, Roughness, and AO maps and click Import. Next, go to "Image -> Mode" and make sure "Grayscale" is selected. Even if your images are grayscale, GIMP may still treat them as color images, which prevents this method from working. 
(TODO: Finish)
