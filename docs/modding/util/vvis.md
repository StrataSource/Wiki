---
title: vvis
---

# vvis

vvis is a command line utility that builds the visibility tree for BSP files. It is available for Windows and Linux.

## Help Text
```
Valve Software - vvis.exe (Nov  9 2024)

usage  : vvis [options...] bspfile
example: vvis -fast c:\hl2\hl2\maps\test

Common options:

  -v (or -verbose): Turn on verbose output (also shows more command
  -fast           : Only do first quick pass on vis calculations.
  -mpi            : Use VMPI to distribute computations.
  -low            : Run as an idle-priority process.

  -vproject <directory> : Override the VPROJECT environment variable.
  -game <directory>     : Same as -vproject.

Other options:
  -radius_override: Force a vis radius, regardless of whether an env_fog_controller specifies one.
  -mpi_pw <pw>    : Use a password to choose a specific set of VMPI workers.
  -threads        : Control the number of threads vbsp uses (defaults to the # or processors on your machine).
  -nosort         : Don't sort portals (sorting is an optimization).
  -tmpin          : Make portals come from \tmp\<mapname>.
  -tmpout         : Make portals come from \tmp\<mapname>.
  -trace <start cluster> <end cluster> : Writes a linefile that traces the vis from one cluster to another for debugging map vis.
  -FullMinidumps  : Write large minidumps on crash.
```