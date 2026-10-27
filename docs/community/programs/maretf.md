---
title: MareTF
weight: 0
features:
---

<table>
  <tr>
    <td><b>Author</b></td>
    <td>craftablescience</td>
  </tr>
  <tr>
    <td><b>Website</b></td>
    <td><a href="https://maretf.me">maretf.me</a></td>
  </tr>
  <tr>
    <td><b>Download</b></td>
    <td><a href="https://github.com/craftablescience/MareTF/releases">GitHub releases</a></td>
  </tr>
  <tr>
    <td><b>Source Code</b></td>
    <td><a href="https://github.com/craftablescience/MareTF">GitHub</a></td>
  </tr>
  <tr>
    <td><b>Description</b></td>
    <td>A utility to create, edit, and display every type of VTF file ever made.</td>
  </tr>
  <tr>
    <td><b>Actively Maintained?</b></td>
    <td>Yes</td>
  </tr>
</table>

# MareTF
MareTF is an all-in-one texture utility for the Source engine. 
It supports creating and viewing all VTF versions and formats, and there are GUI and command-line executables.

## Creating VTFs through the GUI
You can easily create new VTFs through two methods:
 - Selecting an image by clicking the 'Create' button
 - Selecting a folder of files to convert using the 'Create en Masse' button.
 
## Creating VTFs through the terminal
Here is an example command to create a new VTF:
```bash
> maretf create input.png \ # Create a new VTF from `input.png`
    --version 7.6         \ # ...with version 7.6
    --format  DXT1        \ # ...using the DXT1 format
    --filter  KAISER        # ...and resizing the texture using the Kaiser filter.
```
You can also get info about a VTF.
```bash
> maretf info /path/to/my.vtf

/path/to/my.vtf

 ――― FORMAT ―――
Platform: PC
Version:  7.4

...
```
