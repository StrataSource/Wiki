---
title: vtex
---

# vtex

NOTE: This tool was replaced with [vtex2](/shared/reference/util/vtex2)!

vtex is a command line utility that builds VTF files. It is available for Windows and Linux.

## Help Text

```
  Usage: vtex [-outdir dir] [-nopause] [-mkdir] [-compress level] [-shader ShaderName] [-vmtparam Param Value] tex1.txt tex2.txt ...

  -quiet            : don't print anything out, don't pause for input
  -warningsaserrors : treat warnings as errors
  -nopause          : don't pause for input
  -nomkdir          : don't create destination folder if it doesn't exist
  -shader           : make a .vmt for this texture, using this shader (e.g. "vtex -shader UnlitGeneric blah.tga")
  -vmtparam         : adds parameter and value to the .vmt file
  -outdir <dir>     : write output to the specified dir regardless of source filename and vproject
  -deducepath       : deduce path of sources by target file names
  -extractsrc       : extract approximate src art out of a vtf
  -dontbuild        : don't build the input files into VTFs (usually used with extractsrc)
  -quickconvert     : use with "-dontusegamedir -quickconvert" to upgrade old .vmt files
  -dontusegamedir   : output files in same folder as inputs (for use with -extractsrc and -quickconvert)
  -crcvalidate      : validate .vmt against the sources
  -crcforce         : generate a new .vmt even if sources crc matches
  -nopsd            : skip .psd files (e.g. use this with "vtex *.*")
  -notga            : skip .tga files (e.g. use this with "vtex *.*")
  -oldcubepath      : old cubemap method, expects 6 input files, suffixed: 'up', 'dn', 'lf', 'rt', 'ft', 'bk'
  -panorama         : performs the following: 1. generate _medium.vtf (half res) and _small.vtf (quarter res) unless -nomultires is specified.
                                              2. compress to YCoCg if possible, can 'upgrade' a source .vtf to YCoCg
                                              3. does not generate mip-maps (override this by specifying TEXTUREFLAGS_ALLMIPS in a config file)
  -nomultires       : only applicable if -panorama used, will avoid generating multi-res vtf files
  -compress <level> : compress the input using DEFLATE (level 0 = no compression, level -1 = default)

        eg: -vmtparam $ignorez 1 -vmtparam $translucent 1

  Note that you can use wildcards and that you can also chain them
  e.g. materialsrc/monster1/*.tga materialsrc/monster2/*.tga
```
