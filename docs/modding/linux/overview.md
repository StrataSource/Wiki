---
title: "General Information"
--- 
# General Information 
Full native Linux support, for both games and modding tools, is a major goal of the Strata engine, but in the current state of the project, only the games and any tools entirely developed by the Strata team are fully Linux compatible, with many tools being Windows-only due to outdated GUI elements or otherwise old code. However, thanks to tools like Wine, it is possible to run some of these incompatible tools on Linux devices, with little to no tweaks. This category will go over the basics of what tools are and are not compatible with Linux via Wine, and if any tweaks are necessary to make them function properly. Most native applications can be found in `<game name>/bin/linux64`, with any Windows-only applications being located in `<game name>/bin/win64`.

| Tool         | Compatibility            | Notes                                                                                       |
| ------------ | ------------------------ | ------------------------------------------------------------------------------------------- |
| Hammer       | *Combatible thru Wine*   | Needs to be run with `-winecompat`                                                          |
| HLMV         | *Combatible thru Wine*   | None                                                          |
| vbsp/vvis/vrad | Native                 | None                                                                                        |
| vtex(2)      | Native                   | None                                                                                        |
| Faceposer    | **Incompatible**         | Frequent crashes or instabilities.                                                          |
| SDK launcher | Native                   | Must use version in `Portal 2 Community Edition/bin/linux64`, launching from Steam does not work |


TODO: Page for getting hammer/hlmv to work thru Wine. Add more tools to this table.
