---
title: vbsp
---

# vbsp

vbsp is a command line utility that builds VMF files into BSP files. It is available for Windows and Linux.

## Help Text
```
Valve Software - vbsp.exe (Nov 15 2024)

usage  : vbsp [options...] mapfile
example: vbsp -onlyents c:\hl2\hl2\maps\test

Common options (use -v to see all options):

  -v (or -verbose): Turn on verbose output (also shows more command line options).

  -instancepath : Specify a directory to search for instances in first. Falls back to default behavior if not found
  -onlyents   : This option causes vbsp only import the entities from the .vmf file. -onlyents won't reimport brush models.
  -onlyprops  : Only update the static props and detail props.
  -glview     : Writes .gl files in the current directory that can be viewed with glview.exe. If you use -tmpout, it will write the files into the \tmp folder.
  -nodetail   : Get rid of all detail geometry. The geometry left over is what affects visibility.
  -nowater    : Get rid of water brushes.
  -staticpropcombine    : Cluster specially supported static prop models.
  -keepsources    : Don't clean up cluster models after bspzip.
  -staticpropcombine_considervis : Cluster static prop models only within vis clusters.
  -staticpropcombine_autocombine : Automatically combine simple static props without an explicit combine rule.
  -staticpropcombine_suggestrules: Suggest rules to add to spcombinerules.txt
  -low        : Run as an idle-priority process.

  -vproject <directory> : Override the VPROJECT environment variable.
  -game <directory>     : Same as -vproject.

Other options  :
  -threads     : Control the number of threads vbsp uses (defaults to the # of processors on your machine).
  -verboseentities: If -v is on, this disables verbose output for submodels.
  -noweld      : Don't join face vertices together.
  -nocsg       : Don't chop out intersecting brush areas.
  -noshare     : Emit unique face edges instead of sharing them.
  -notjunc     : Don't fixup t-junctions.
  -noopt       : By default, vbsp removes the 'outer shell' of the map, which are all the faces you can't see because you can never get outside the map. -noopt disables this behaviour.
  -noprune     : Don't prune neighboring solid nodes.
  -nomerge     : Don't merge together chopped faces on nodes.
  -nomergewater: Don't merge together chopped faces on water.
  -nosubdiv    : Don't subdivide faces for lightmapping.
  -micro <#>   : vbsp will warn when brushes are output with a volume less than this number (default: 1.0).
  -fulldetail  : Mark all detail geometry as normal geometry (so all detail geometry will affect visibility).
  -alldetail   : Convert all structural brushes to detail brushes, except func_brush entities whose names begin with structure_.
  -leaktest    : Stop processing the map if a leak is detected. Whether or not this flag is set, a leak file will be written out at <vmf filename>.lin and it can be imported into Hammer.
  -bumpall     : Force all surfaces to be bump mapped.
  -snapaxial   : Snap axial planes to integer coordinates.
  -block # #      : Control the grid size mins that vbsp chops the level on.
  -blocks # # # # : Enter the mins and maxs for the grid size vbsp uses.
  -blocksize #    : Control the size of each grid square that vbsp chops the level on.  Default is 1024.
  -dumpstaticprops: Dump static props to staticprop*.txt
  -dumpcollide    : Write files with collision info.
  -forceskyvis     : Enable vis calculations in 3d skybox leaves
  -luxelscale #   : Scale all lightmaps by this amount (default: 1.0).
  -minluxelscale #: No luxel scale will be lower than this amount (default: 1.0).
  -maxluxelscale #: No luxel scale will be higher than this amount (default: 999999.0).
  -lightifmissing : Force lightmaps to be generated for all surfaces even if they don't need lightmaps.
  -keepstalezip   : Keep the BSP's zip files intact but regenerate everything else.
  -virtualdispphysics : Use virtual (not precomputed) displacement collision models
  -visgranularity # # # : Force visibility splits # of units along X, Y, Z
  -xbox         : Enable mandatory xbox options
  -replacematerials : Substitute materials according to materialsub.txt in content\maps
  -FullMinidumps        : Write large minidumps on crash.
  -upgradeversion  : Upgrade an existing BSP to Strata Source BSP version 25.
```