---
title: dmxconvert
---

# dmxconvert

dmxconvert is a command line utility that converts between different datamodel types and encodings. It is available for Windows and Linux.

## Help Text

```
Usage: dmxconvert -i <in file> [-ie <in encoding hint>] [-o <out file>] [-oe <out encoding>] [-of <out format>]
     -i, --input               - Input file name
     -o, --output              - Output filename
     -ie, --input-encoding     - Input encoding hint
     -of, --output-format      - Output format
     -oe, --output-encoding    - Output encoding
If no output file is specified, dmx to dmx conversion will overwrite the input
Supported DMX file encodings:
   keyvalues
   keyvalues2
   keyvalues2_flat
   binary
   actbusy
   commentary
   vmt
   vmf
   mks
   tex_source1
Supported DMX file formats:
   dmx
   movieobjects
   sfm
   sfm_settings
   sfm_session
   sfm_trackgroup
   pcf
   gui
   schema
   preset
   facial_animation
   model
   ved
   mks
   mp_preprocess
   mp_root
   mp_model
   mp_anim
   mp_physics
   mp_hitbox
   mp_materialgroup
   mp_keyvalues
   mp_eyes
   mp_bonemask
   tex
   world
   worldnode
```

## Usage Examples

Example 1: Converting a DMX encoded file to keyvalues2.
```
./bin/linux64/dmxconvert -i medic_lod_03_high.dmx -o medic_lod_03_high.kv2 -oe keyvalues2
```