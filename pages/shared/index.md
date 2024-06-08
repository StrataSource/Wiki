# Strata Source Wiki

Welcome to the Strata Source wiki! This wiki contains documentation that is
common to all Strata Source-based games.

The markdown sources of the wiki are located here:
[https://github.com/StrataSource/Wiki](https://github.com/StrataSource/Wiki)

If you'd like to contribute, see the Contributing section of this document for
more information.

## Features

Strata Source started development in mid-2020 as a fork of CSGO's engine branch
with Portal 2 features ported over. Since its inception, many features, fixes and
other improvements have been made to Strata Source, including:

- Native DirectX 11 renderer
- Panorama UI
- DXVK support on Linux for DirectX 11
- 64-bit support (32-bit support has been completely dropped)
- Expanded map limits (128k x 128k x 128k) and increased entity cap via BSPv25
- PBR shading
- CSM (Originally from CSGO)
- Backwards compatibility with BSP v19-21
- Backwards compatibiltiy with TF2/HL2/L4D1/ASW branch models
- webm video support, replacing older Bink videos
- Many improvements to Linux support
- Fully cross platform engine tools and utils
- Steam Audio for HRTF and basic occlusion
- MP3, OGG and FLAC support
- Support for Portals and paint even in non-Portal based mods
- VTF v7.6 with lossless DEFLATE compression support
- Many improvements to the Hammer level editor
- Many code quality improvements (Refactors, cleanup and C++23)
- Sentry crash report integration
- ImGui support in-game for tools (vprof, fogui, etc.)
- And much much more!

## Projects Using Strata

Right now, the following games are using Strata:

- [Momentum Mod](https://momentum-mod.org/)
- [Portal 2: Community Edition](https://portal2communityedition.com/)
- [Portal: Revolution](https://www.moddb.com/mods/portal-revolution-spyce-software)

## Contributing

Anyone can contribute to the wiki. Just fork the repo, commit your changes and
open a pull request. Make sure to use appropriate language, and be willing to
take feedback on your PR.

### Guidelines

Pull requests are thoroughly reviewed before being accepted. All contributions
must adhere to these guidelines

#### Pages have to

- be related to Strata Source
- not be a duplicate of an existing page
- contain formal, passive language (No `I think` or `Next you go to`)

#### Please do

- embed images or videos that showcase what is being explained
- add links wherever possible
- use proper, rich
  [markdown styling](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

#### Please don't

- create pages for general Hammer Editor tutorials
- advertise
- add malicious links or (any) downloads

### Images and other media

Images should be kept in this git repository, as this helps versioning and it
ensures the images will always be available.
