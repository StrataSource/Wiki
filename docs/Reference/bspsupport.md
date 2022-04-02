---
layout: default
title: BSP Support
parent: Reference
---

# BSP Support

This is an overview of which versions of the BSP map file format the Chaos
engine can launch. Some formats can be converted to a supported version by
manipulating the raw binary data, while others would need decompilation with an
appropriate tool, which might break certain properties without manual
intervention.

Furthermore, it's not guaranteed that every format that is listed as supported
works 100% since there might still be game-specific incompatiblities.

Source 2 is not supported at all as its formats aren't documented and completely
different from what's supported in Source.

For more details, see
[the Valve Developer Wiki page](https://developer.valvesoftware.com/wiki/Source_BSP_File_Format).

| Engine  | Version(s) | Games                                                     | Supported | Planned      | Details                                                                  |
| ------- | ---------- | --------------------------------------------------------- | --------- | ------------ | ------------------------------------------------------------------------ |
| IdTech  | Any        | Quake 1/2/3                                               | No        | No           | Too different from modern Source                                         |
| GoldSrc | Any        | Half-Life, Team Fortress Classic, CS 1.6                  | No        | No           | Too different. It's possible to decompile, and then recompile for Source |
| Source  | ≤18        | Vampire: the Masquerade, very old HL2                     | Untested  | No           | Might work with manual binary editing                                    |
| Source  | 19-20      | HL2, TF2, CSS                                             | Yes       | -            | Fully supported                                                          |
| Source  | 20         | GMod, L4D, Black Mesa                                     | Yes       | -            | Map loads, parts might be broken due to missing shaders/scripting, etc.  |
| Source  | 21         | Portal 2, CSGO, Alien Swarm, any Chaos VBSP compiled maps | Yes       | -            | Natively supported, preferred for any Chaos game                         |
| Source  | 21         | Left 4 Dead 2                                             | No        | Probably not | Can be fixed by swapping entries in lump headers around, see link above  |
| Source  | ≥22        | pre-Reborn Dota 2, Contagion, any Respawn Source games    | No        | No           | Too many undocumented differences to make it worth                       |
