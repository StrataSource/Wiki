---
title: Feature flags
weigth: 20
---

# Feature flags

To make following the wiki easier, each article that requires features is tagged appropriately. As soon as this feature isn't available in one of the games, the wiki will automatically show a warning indicating limited support.

This further supports the user when they select a game, as the wiki can automatically determine if an article is relevant or even possible in the selected game.

## Setting feature flags

Features required for an article are set in its [Meta Block](editing-articles#meta-block). If more than one feature is specified, the game needs to have all of them in order for the wiki to consider it supported.

```yaml
features:
    - USE_UGC
    - USE_VSCRIPT
```

In this example, the article will only be considered supported for games that have both the `PANORAMA` and the `VSCRIPT` features.
