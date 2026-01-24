---
title: "General Information"
--- 
# General Information 
Full native Linux support, for both games and modding tools, is a major goal of the Strata engine, but in the current state of the project, only the games and any tools entirely developed by the Strata team are fully Linux compatible, with many tools being Windows-only due to outdated GUI elements or otherwise old code. However, thanks to tools like Wine, it is possible to run some of these incompatible tools on Linux devices, with little to no tweaks. This category will go over the basics of what tools are and are not compatible with Linux via Wine, and if any tweaks are necessary to make them function properly. Most native applications can be found in `<game name>/bin/linux64`, with any Windows-only applications being located in `<game name>/bin/win64`.

| Tool         | Compatibility            | Notes |
| ------------ | ------------------------ | ----- |
| Hammer       | *Combatible thru Wine*   | Needs to be run with `-winecompat`, see [Running Windows Tools on Linux](./tools_on_linux) |
| HLMV         | *Combatible thru Wine*   | Same with Hammer |
| Faceposer    | *Compatible thru Wine*         | Requires minimum Wine 11. Same process as Hammar. |
| vbsp/vvis/vrad | Native                 | When running Hammer under Wine, make sure to point to the Win64 versions for Compatibility |
| vtex(2)      | Native                   | None |
| SDK launcher | Native                   | Must use version in `Portal 2 Community Edition/bin/linux64`, launching from Steam does not work |
