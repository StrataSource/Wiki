---
title: vrad
---

# vrad

VRad, or Valve Radiosity Simulator, is the compile tool responsible for generating lighting data for your map. It's available for both Windows and Linux.

## Strata Source Additions

Changes over CSGO/Portal2 VRad:
* Lighting that passes through world portals (See `-PortalTraversalLighting`)
* `_removeaftercompile` flag for lights so they only contribute to lighting the world. They will not be emitted into the world lighting lump.
* Improved texture shadows
* Huge performance improvements
* Expanded/removed limits
* Much more!

## Portal Traversal Lighting

If enabled by `-PortalTraversalLighting`, light rays can be traced through static world portals. This can help avoid jarring lighting transitions that are often
seen through world portals.

'static' world portals must have their `isstatic` key set to 1, and a valid partner with the same configuration.

## Ambient Occlusion

>[!NOTE]
> Baked ambient occlusion disables the use of runtime XeGTAO on brush geometry. XeGTAO provides a much higher quality form of AO with a higher runtime cost.
> In most cases you should prefer XeGTAO over this feature.

Baked ambient occlusion is a cheap alternative to more computationally expensive runtime SSAO algorithms. 
VRad's implementation of AO is from CSGO, with some additional performance optimizations made to reduce map compile times.

Baked AO is only rendered onto lightmaps and generally looks best on lower lightmap scales. While static props are treated as occluders, they cannot receive
any of the AO themselves.

>[!NOTE]
> VRad AO significantly impacts map compile times, sometimes even doubling them. It's recommended to only enable it while doing a final lighting pass,
> or to use XeGTAO instead.

The following VRad parameters can be used to tweak the look of AO:
* `-aoscale <number>`: Sets the ambient occlusion scale. Higher values yield stronger effects. Can't be used with `-aoradius`.
* `-aosamples <number>`: Number of samples to take (Default: 32) 
* `-aoradius <number>`: Sets the AO radius, in units. Higher values yield stronger effects. Can't be used with `-aoscale`
* `-noao`: Disables baked ambient occlusion entirely.
* `-PortalTraversalAO`: Allows baked ambient occlusion to traverse static world portals.

## Light Culling

Experimental light culling can be enabled with `-culllights`. This option will attempt to cull lights that are contributing an insignificant amount
of light to a given texel, leading to a performance boost.

Some artifacting or other bugs may occur, use with caution!

## Help Text

```
Valve Software - vrad.exe AVX2 (Mar  9 2024)

      Valve Radiosity Simulator
Command line: "vrad.exe" "-game" "p2ce"

usage  : vrad [options...] bspfile
example: vrad c:\hl2\hl2\maps\test

Common options:

  -v (or -verbose): Turn on verbose output (also shows more command
  -bounce #       : Set max number of bounces (default: 100).
  -fast           : Quick and dirty lighting.
  -fastambient    : Per-leaf ambient sampling is lower quality to save compute time.
  -final          : High quality processing. equivalent to -extrasky 16.
  -finitefalloff  : use an alternative falloff model that falls off to exactly zero at the zero_percent_distance.
  -extrasky n     : trace N times as many rays for indirect light and sky ambient.
  -low            : Run as an idle-priority process.
  -mpi            : Use VMPI to distribute computations.
  -rederror       : Show errors in red.

  -vproject <directory> : Override the VPROJECT environment variable.
  -game <directory>     : Same as -vproject.
  -report         : Write compile report next to vmf.

Other options:
  -dump           : Write debugging .txt files.
  -dumpnormals    : Write normals to debug files.
  -dumptrace      : Write ray-tracing environment to debug files.
  -threads        : Control the number of threads vbsp uses (defaults to the #
                    or processors on your machine).
  -lights <file>  : Load a lights file in addition to lights.rad and the
                    level lights file.
  -noextra        : Disable supersampling.
  -debugextra     : Places debugging data in lightmaps to visualize
                    supersampling.
  -smooth #       : Set the threshold for smoothing groups, in degrees
                    (default 45).
  -dlightmap      : Force direct lighting into different lightmap than
                    radiosity.
  -stoponexit      : Wait for a keypress on exit.
  -mpi_pw <pw>    : Use a password to choose a specific set of VMPI workers.
  -nodetaillight  : Don't light detail props.
  -centersamples  : Move sample centers.
  -luxeldensity # : Rescale all luxels by the specified amount (default: 1.0).
                    The number specified must be less than 1.0 or it will be
                    ignored.
  -loghash        : Log the sample hash table to samplehash.txt.
  -onlydetail     : Only light detail props and per-leaf lighting.
  -maxdispsamplesize #: Set max displacement sample size (default: 512).
  -softsun <n>    : Treat the sun as an area light source of size <n> degrees.                    Produces soft shadows.
                    Recommended values are between 0 and 5. Default is 0.
  -FullMinidumps  : Write large minidumps on crash.
  -chop           : Smallest number of luxel widths for a bounce patch, used on edges
  -maxchop      : Coarsest allowed number of luxel widths for a patch, used in face interiors
  -LargeDispSampleRadius: This can be used if there are splotches of bounced
                          light on terrain. The compile will take longer, but
                          it will gather light across a wider area.
  -StaticPropLighting   : generate baked static prop vertex lighting
  -StaticPropLightingFinal   : generate baked static prop vertex lighting (uses higher/final quality processing)
  -StaticPropPolys   : Perform shadow tests of static props at polygon precision
  -OnlyStaticProps   : Only perform direct static prop lighting (vrad debug option)
  -StaticPropNormals : when lighting static props, just show their normal vector
  -StaticPropBounce  : Enable static props to bounce light. Experimental option, doesn't work with VMPI right now.
  -textureshadows : Allows texture alpha channels to block light - rays intersecting alpha surfaces will sample the texture
  -noskyboxrecurse : Turn off recursion into 3d skybox (skybox shadows on world)
  -nossprops      : Globally disable self-shadowing on static props

  -PortalTraversalLighting : Allow light to teleport through (static) portals.
  -PortalTraversalAO       : Allow AO calculations to teleport through (static) portals. SLOW!

  -aoscale <float>  : Sets the ambient occlusion scale. Can't be used with -aoradius
  -aoradius <float> : Sets the ambient occlusion radius
  -aosamples <int>  : Sets the number ambient occlusion samples. Default is 32
  -noao                  : Disable baked ambient occlusion  -ambient <vector> : Sets the ambient term. Can be used to tweak lightmap color
  -reflectivityscale <float> : Sets the reflectivity scale for all surfaces. Defaults to 1.0
  -disppatchradius <float> : Sets the maximum radius allowed for displacement patches
  -dispchop <float> : Number of luxel widths for a patch. Default is 8
  -staticpropsamplescale <float> : Extra sampling factor for indirect light for static props
  -ambientfromleafcenters : Samples ambient lighting from the center of the leaf
  -LeafAmbientSampleReduction <float> : Reduction factor for ambient samples. Defaults to 1.0
  -unlitdetail      : Disables lighting for detail props
  -IndirectOnly     : Only compute radiosity lighting, and disable direct lighting
  -culllights       : Cull lights during BuildFacelights
```
