---
title: vtex2
---

# vtex2

vtex2 is a Valve Texture Format conversion and creation tool. It has a CLI and a GUI component for viewing, packing and otherwise converting the files.

The source code is available [here on GitHub](https://github.com/StrataSource/vtex2).

## Usage

Command help documentation and usage examples can be shown on the command line using `vtex2 --help`.

For action-specific help, use `vtex2 <action> --help`.

### Creating VTFs

Creating a VTF can be done with the `vtex2 convert` action.

For example, the following command will create a VTF called `some-file.vtf` with the format `BGRA8888`:
```
vtex2 convert -f bgra8888 some-file.jpg
```

If you pass a directory to `vtex2 convert`, it will convert all files in that directory. The `-r` or `--recursive` parameter
will cause the program to descend and process subdirectories too.

Full list of options:
```
USAGE: vtex2 convert [OPTIONS] file...

  Convert a generic image file to VTF

Options:
  --bumpscale                      Bumpscale
  --clamps                         Clamp on S axis
  --clampt                         Clamp on T axis
  --clampu                         Clamp on U axis
  --no-mips                        Disable mipmaps for this texture
  --pointsample                    Set point sampling method
  --srgb                           Process this image in sRGB color space
  --start-frame                    Animation frame to start on
  --thumbnail                      Generate thumbnail for the image
  --trilinear                      Set trilinear sampling method
  --version                        Set the VTF version to use
  -c,--compress [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                                   DEFLATE compression level to use. 0=none, 9=max. This will force VTF version to 7.6
  -f,--format [rgba8888, abgr8888, rgb888, bgr888, rgb565, i8, ia88, p8, a8, rgb888_bluescreen, bgr888_bluescreen, argb8888, bgra8888, dxt1, dxt3, dxt5, bgrx8888, bgr565, bgrx5551, bgra4444, dxt1_onebitalpha, bgra5551, uv88, uvwq8888, rgba16161616f, rgba16161616, uvlx8888, r32f, rgb323232f, rgba32323232f, ati2n, ati1n, bc7]
                                   Image format of the VTF
  -gl,--opengl                     Treat the incoming normal map as a OpenGL normal map
  -h,--height                      Height of the output VTF
  -m,--mips                        Number of mips to generate
  -n,--normal                      Create a normal map
  -o,--output                      Name of the output VTF
  -r,--recursive                   Recursively process directories
  -w,--width                       Width of the output VTF
  file                             Image file to convert or directory to process
```

### Extracting image data from VTF

Extracting image data from a VTF can be done using `vtex2 extract`.

For example, the following command will extract the VTF to `some-file.jpg`:
```
vtex2 extract -f jpg some-file.vtf
```

If you pass a directory to `vtex2 extract`, it will convert all files in that directory. The `-r` or `--recursive` parameter
will cause the program to descend and process subdirectories too.

Full list of options:
```
USAGE: vtex2 extract [OPTIONS] file...

  Converts a VTF into png, tga, jpeg, bmp or hdr image file

Options:
  -f,--format [png, jpeg, jpg, tga, bmp, hdr]
                                   Output format to use
  -m,--mip                         Mipmap to extract from image
  -na,--no-alpha                   Exclude alpha channel from converted image
  -o,--output                      File to place the output in
  -r,--recursive                   Recursively process directories
  file                             VTF file to convert or directory to process
```

### Displaying VTF Info

The `vtex2 info` command can be used to display some info about VTF files.

Full list of options:
```
USAGE: vtex2 info [OPTIONS] file...

  Displays info about a VTF file

Options:
  -a,--all                         Display all detailed info about a VTF
  -r,--resources                   List all resource entries in the VTF
  file                             VTF file to process
```

### Channel pack a VTF

The `vtex2 pack` command can be used pack images into channels of a VTF.

Full list of options:
```
USAGE: vtex2 pack [OPTIONS] -o...

  Packs images into a MRAO or normal+height map

Options:
  -aoc,--ao-const                  If no AO map is specified, fill AO value with this constant value
  -aomap,--ao-map                  AO map to pack [MRAO only]
  -gl,--opengl                     Treat the incoming normal map as a OpenGL normal map
  -h,--height                      Height (dimension) of output image. If set to -1, autodetect from input maps
  -hc,--height-const               If no height map is specified, fill height value with this constant value
  -hmap,--height-map               Height map to pack
  -m,--mips                        Number of mipmaps for output image
  -mc,--metalness-const            If no metalness map is specified, fill metalness value with this constant value
  -mmap,--metalness-map            Metalness map to pack [MRAO only]
  -mrao,--mrao                     Create MRAO map
  -n,--normal                      Create packed normal+height map
  -nmap,--normal-map               Normal map to pack
  -o,--outfile                     Output file name
  -rc,--roughness-const            If no roughness map is specified, fill roughness value with this constant value
  -rmap,--roughness-map            Roughness map to pack [MRAO only]
  -tmask,--tint-mask               Tint mask texture to use [MRAO only]
  -w,--width                       Width of output image. If set to -1, autodetect from input maps
```


