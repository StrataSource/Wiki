---
title: "General Information"
--- 
# General Information 
Full native Linux support, for both games and modding tools, is a major goal of the Strata project, but in its current state, only the games and any tools entirely developed by the Strata team are fully Linux compatible, with many tools being Windows-only due to outdated GUI elements or otherwise old code. However, thanks to tools like Wine, it is possible to run some of these incompatible tools on Linux devices, with little to no tweaks. This category will go over the basics of what tools are and are not compatible with Linux via Wine, and if any tweaks are necessary to make them function properly. Most native applications can be found in `<game name>/bin/linux64`, with any Windows-only applications being located in `<game name>/bin/win64`.
>[!NOTE]
>This table only contains tools included with most builds of Strata, and does not cover any Third-Party tools like VTFEdit or GCFScape. Any official tool not listed here likely has a Linux native version, is compatible thru Wine without any tweaks necessary, or has yet to be tested.

| Tool         | Compatibility            | Notes |
| ------------ | ------------------------ | ----- |
| Hammer       | *Combatible thru Wine*   | Needs to be run with `-winecompat`, see [Running Windows Tools on Linux](./tools_on_linux). |
| HLMV         | *Combatible thru Wine* | Same with Hammer. |
| Faceposer    | *Compatible thru Wine* | Requires minimum Wine 11. Same process as Hammer. |
| Postcompiler (TeamSpens HA) | *Compatible thru Wine* | While no Linux-native version is released, the program can be compiled for Linux by following instructions on the [Github Page](https://github.com/TeamSpen210/HammerAddons?tab=readme-ov-file#building-from-source). |
| vbsp/vvis/vrad | Native | Only for use in shell scripts/wrappers. When running Hammer under Wine, make sure to point to the Win64 versions for compatibility. |
| `.ps1` scripts | Native | Requires [Powershell](https://learn.microsoft.com/en-us/powershell/scripting/install/install-powershell-on-linux?view=powershell-7.5) to be installed. |
| All engine tools (particle editor, material editor, etc)| Native | None |
| SDK launcher | Native | Must use version in `Portal 2 Community Edition/bin/linux64`, launching from Steam will launch the .exe version. |
