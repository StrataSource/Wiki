---
title: Tools & Utilities Main Page
---

> [!NOTE]
> This page is non-exhaustive. If you have a suggestion for a stable/useful tool that would fit in here, create a PR for it!

# Open Source Tools & Utilities

This page serves as a list of open source tools & utilities to work with Strata Source (and Strata Games) with credits to respective authors and potential links to separate pages.
In addition, this is akin to a "guide", specifying when you would want to use the given tool.




---
# TEXTURES 
---

## MareTF

[MareTF](https://github.com/craftablescience/MareTF) - An open source utility to create, edit and display VTF files.

**Use Cases:**
* VTF texture creation, conversion and manipulation.
* Drop-in replacement for vtex2.
* Replacement for Valve's original vtex tool.
* Native Linux alternative to VTFEdit/VTFCmd.

**Authors:**
* craftablescience & koerismo

## VTFEdit Reloaded
[VTFEdit Reloaded](https://developer.valvesoftware.com/wiki/VTFEdit_Reloaded) - a fork of the original VTFEdit, with some QoL and fixes (Dark Mode VMT editor, fixed cubemap previews, etc.)

**Use Cases:**
* Anytime you want to use VTFEdit.

**Authors:**
* Neil "Jed" Jedrzejewski
* Ryan "Nemesis" Gregg
* Fork by Skyrym and Joshua Ashton

## vtex2 (Deprecated)
[vtex2](/modding/util/vtex2) - an open-source successor to Valve's vtex tool made by the Strata team, it comes packed with a Qt-based GUI named vtfview.

Deprecated in favor of MareTF.

**Use Cases:**
* Quick VTF conversion alternative to VTFEdit
* As a replacement for the original vtex.
* Native Linux alternative to VTFEdit/VTFCmd

**Authors:**
* Strata Source Team & Contributors


---
# FILES
---

[VPKEdit](https://github.com/craftablescience/VPKEdit) - CLI/GUI tool to handle multiple pack formats (creation, reading, writing) such as VPK, WAD, BMZ, BEE_PACK.

## VPKEdit

**Use Cases:**
- You want a good tool to handle package formats such as VPK
- Native Linux Support

**Authors:**
* craftablescience and contributors

ㅤ    
ㅤ  
ㅤ  

---
# PROGRAMMING
---

## sourcepp

[sourcepp](https://github.com/craftablescience/sourcepp) - modern open-source collection of libraries written in C++20 to parse Valve formats, with Python wrappers included.

**Use Cases:**
* You need a sane parser for most Valve file formats associated with the Source Engine.
* Something more "modern", thanks to its C++20 implementation.
* A swiss-army knife powerhouse of parsers.

**Authors:**
* Strata Source Team & Contributors

ㅤ    
ㅤ  
ㅤ  

## VTFLib

> [!CAUTION]
> VTFLib has some "quirks" from the old days of Source and from its age. One such thing is that VTFLib cannot parse textures which's dimensions aren't power of 2, and has middling error handling.

[VTFLib](https://github.com/NeilJed/VTFLib) - open-source C/C++ library meant for parsing and working with the Valve Texture Format (VTF).
The original VTFCmd and VTFEdit are part of the same repository.

**Use Cases:**
* If you want to have a reliable, yet archaic VTF library.
* When sourcepp's vtfpp does not support a feature that VTFLib does.

**Authors:**  
* Neil "Jed" Jedrzejewski
* Ryan "Nemesis" Gregg 
ㅤ    
ㅤ  
ㅤ  

## datamodel-rs

[datamodel-rs](https://crates.io/crates/datamodel) - work-in-progress Rust library meant for serialization and deserialization of Valve's DMX format, supporting binary v1-5, KV2 and KV2_flat.

**Use Cases:**
* DMX/KV2 are rather commonly used around Source 1/2 (such as the .vmap file format which is DMX binary v4, the DMX model, particle files), sourcepp only supports the Binary version of DMX, but not the ASCII encoded version of DMX (KeyValues2), as a result, if you for some reason need to support the ASCII encoded one aswell, this is the choice.
* Want to write a tool/CLI/app for DMX/KV2 files in Rust rather than C/C++

**Authors:**
* jakobg1215

ㅤ    
ㅤ  
ㅤ  

## Source Engine VSCode Plugin

[Source Engine Support](https://marketplace.visualstudio.com/items?itemName=stefan-h-at.source-engine-support) - plugin for Visual Studio Code that adds support for the Source Engine file types (vmt, KV, fgd, qc, cfg, vpc, vgc, smd, fxc, fxc.h, lights.rad), additionally it can allow you to compile the .qc or subtitles files directly inside the extension.

**Use Cases:**
* If you find yourself working a lot with the human-readable text-based Source formats, it is a very good option.

**Authors:**
* Stefan Heinz
ㅤ    
ㅤ  
ㅤ  


## SpeedyKeyV

[SpeedyKeyV](https://github.com/ozxybox/SpeedyKeyV) - fast C++ parsing library for the KeyValues format. Nothing less, nothing more.

**Use Cases:**
* You want to parse keyvalues at a reasonably fast pace.

**Authors:**
* Ozxybox

ㅤ    
ㅤ  
ㅤ  

---
# UI
---
## Panorama Resources
[braem's Panorama Languages Support](https://github.com/panorama-languages-support) - a collection of different utilities (such as VSCode support for Panorama's CSS3) for working with Panorama UI


**Use Cases:**
* Whenever you are working with Panorama UI

**Authors:**
* braem