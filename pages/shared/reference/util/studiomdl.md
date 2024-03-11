---
title: studiomdl
---

# studiomdl

studiomdl is the MDL compiler shipped with all branches of Source. In Strata, mdlcompile's functionality was merged into studiomdl. It is available for Windows and Linux.

The following input model formats are supported:
* SMD
* DMX
* FBX
* OBJ

## Help Text

```
Usage: studiomdl.exe [options] <file.qc>

Options:
  [-a <normal_blend_angle>]
  [-checklengths]
  [-d] - dump glview files
  [-definebones]
  [-f] - flip all triangles
  [-fullcollide] - don't truncate really big collisionmodels
  [-game <gamedir>]
  [-h] - dump hboxes
  [-i] - ignore warnings
  [-minlod <lod>] - truncate to highest detail <lod>
  [-n] - tag bad normals
  [-perf] report perf info upon compiling model
  [-printbones]
  [-printgraph]
  [-quiet] - operate silently
  [-r] - tag reversed
  [-t <texture>]
  [-fastbuild] - write a single vertex windings file
  [-nowarnings] - disable warnings
  [-dumpmaterials] - dump out material names
  [-mdlreport] model.mdl - report perf info
  [-mdlreportspreadsheet] - report perf info as a comma-delimited spreadsheet
  [-striplods] - use only lod0
  [-overridedefinebones] - equivalent to specifying $unlockdefinebones in qc file
  [-stripmodel] - process binary model files and strip extra lod data
  [-stripvhv] - strip hardware verts to match the stripped model
  [-vsi] - generate stripping information .vsi file - can be used on .mdl files too
  [-allowdebug]
  [-overridedefinebones]
  [-verbose]
  [-makefile]
  [-verify]
  [-fastbuild]
  [-maxwarnings]
  [-preview]
  [-dumpmaterials]
  [-basedir]
  [-tempcontent]
  [-outdir <dir>] - directory to place the resultant model into. ie, /some/path will create the model /some/path/mymdl.mdl
```

# List of StudioMDL commands (.qc scripts)

| Command | Parameters | Description |
|---|---|---|
| `$cd` | `string directory` | Directory to change to |
| `$modelname` | `string modelName` | Set the name of the model, relative to the `models/` directory, including the `.mdl` extension |
| `$internalname` | `string internalName` | Set the internal name of the model. This will be used as the name of the `.ani` file |
| `$cdmaterials` | `string materialsPath` | Set the materials path |
| `$pushd` | `string directory` | Same as `$cd` but pushes the current directory to a stack before doing the cd |
| `$popd` | none | Return to the directory previous to the last `$pushd` call |
| `$scale` | `float flScale` | Scale the model on all axes by a scalar value |
| `$root` | `string boneName` | Set the name of the root bone |
| `$controller` | | |
| `$screenalign` | `string boneName, string type = ["sphere", "cylinder", "billboard"]` | Align bone with screen |
| `$worldalign` | `string boneName` | Align bone with world |
| `$keepupright` | `string boneName` | Keeps a bone upright |
| `$model` | | |
| `$collisionmodel` | `string modelName, [optional block]` | Set the collision model for the mesh |
| `$collisionjoints` | `string modelName, [optional block]` | Set the collision model for the mesh, with separate joints |
| `$collisiontext` | | |
| `$appendsource` | | |
| `$body` | | |
| `$prefer_fbx` | | |
| `$bodygroup` | | |
| `$appendblankbodygroup` | | |
| `$bodygrouppreset` | | |
| `$animation` | | |
| `$autocenter` | | |
| `$sequence` | | |
| `$append` | | |
| `$prepend` | | |
| `$continue` | | |
| `$declaresequence` | | |
| `$declareanimation` | | |
| `$cmdlist` | | |
| `$animblocksize` | | |
| `$weightlist` | | |
| `$defaultweightlist` | | |
| `$ikchain` | | |
| `$ikautoplaylock` | | |
| `$eyeposition` | | |
| `$illumposition` | | |
| `$origin` | | |
| `$originbones` | | |
| `$upaxis` | | |
| `$bbox` | | |
| `$bboxonlyverts` | | |
| `$cbox` | | |
| `$gamma` | | |
| `$texturegroup` | | |
| `$hgroup` | | |
| `$hbox` | | |
| `$hboxset` | | |
| `$surfaceprop` | | |
| `$jointsurfaceprop` | | |
| `$contents` | `string contents = ["grate", "ladder", "solid", "monster", "notsolid"]` | |
| `$jointcontents` | `string jointName, string contents = ["grate", "ladder", "solid", "monster", "notsolid"]` | |
| `$attachment` | | |
| `$redefineattachment` | | |
| `$bonemerge` | | |
| `$bonealwayssetup` | | |
| `$externaltextures` | | |
| `$cliptotextures` | | |
| `$skinnedLODs` | | |
| `$renamebone` | | |
| `$stripboneprefix` | | |
| `$renamebonesubstr` | | |
| `$collapsebones` | | |
| `$collapsebonesaggressive` | | |
| `$alwayscollapse` | | |
| `$proceduralbones` | | |
| `$skiptransition` | | |
| `$calctransitions` | | |
| `$staticprop` | none | Mark this model as a static prop |
| `$zbrush` | none | Enable some special processing for zbrush authored models. Models marked with this have their texcoords smoothed. This is very expensive! |
| `$realignbones` | | |
| `$forcerealign` | | |
| `$lod` | | |
| `$shadowlod` | | |
| `$poseparameter` | | |
| `$heirarchy` | | Lol, lmao|
| `$hierarchy` | | |
| `$insertbone` | | |
| `$limitrotation` | | |
| `$definebone` | | |
| `$jigglebone` | | |
| `$includemodel` | | |
| `$opaque` | none | Force this model to be opaque. Removes any transparency flags |
| `$mostlyopaque` | | |
| `$keyvalues` | `block` | Defines a block of key-value pairs. These will be embedded into the model |
| `$obsolete` | none | Marks this model as obsolete. It will show the obsolete material in-game |
| `$renamematerial` | | |
| `$renamematerialsubstr` | | |
| `$overridematerial` | | |
| `$stripmaterialpaths` | | |
| `$fakevta` | | |
| `$noforcedfade` | | |
| `$skipboneinbbox` | | |
| `$forcephonemecrossfade` | | |
| `$lockbonelengths` | | |
| `$unlockdefinebones` | | |
| `$constantdirectionallight` | `float flDirLightDot` | Set the constant directional light dot product. Must be between 0 and 1, floating point number |
| `$minlod` | `int minLod` | Set the min lod |
| `$allowrootlods` | | |
| `$bonesaveframe` | | |
| `$ambientboost` | none | Indicate that the model should be rendered with an ambient boost |
| `$centerbonesonverts` | | |
| `$donotcastshadows` | none | Indicate that the model should not cast any shadows |
| `$casttextureshadows` | none | Indicate that this model should cast texture-based shadows in vrad, only applies to prop_static |
| `$motionrollback` | | |
| `$sectionframes` | | |
| `$clampworldspace` | | |
| `$maxeyedeflection` | | |
| `$addsearchdir` | | |
| `$phyname` | | |
| `$subd` | none | Indicate that we have a quad-only catmull-clark subd mesh in the model |
| `$boneflexdriver` | | |
| `$maxverts` | `int maxVerts` | Set the max verts on the model. Must be in range [1024, 65536] |
| `$preservetriangleorder` | | |
| `$qcassert` | | |
| `$lcaseallsequences` | | |
| `$defaultfadein` | | |
| `$defaultfadeout` | | |
| `$cloth` | | |
| `$clothplanecollision` | | |
| `$allowactivityname` | | |
| `$collisionprecision` | | |
| `$erroronsequenceremappingfailure` | | |
| `$erroronsequenceremappingfailure_disable` | | |
| `$modelhasnosequences` | | |
| `$contentrootrelative` | | |
| `$adduvmapchannelto` | | |
| `$section` | | |
| `$sectionenable` | | |
| `$sectiondisable` | | |


