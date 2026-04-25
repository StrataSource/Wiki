---
title: Source Mods
features:
    - USE_CAMPAIGNMANAGER
weight: 90
---

# Source Mods
P2:CE and its menu system was designed as a gateway to sourcemods/standalone games. If a default campaign is specified (cvar: `campaign_default`), the game will use that campaign as the base menu state instead of the standard P2:CE menu. This can be helpful for mods that cannot or do not want to create a custom menu system (or simply as a starting platform while developing the mod).

> [!NOTE]
> **There are extra considerations to take when developing a menu script that leverages the campaign system. Full details can be found on [the Technical Notes page](/modding/p2ce-campaigns/technical-notes).**
