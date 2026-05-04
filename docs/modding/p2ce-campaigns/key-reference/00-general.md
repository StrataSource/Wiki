---
title: "General Information"
weight: 0
features:
  - USE_CAMPAIGNMANAGER
---
# General Information
These pages function as a documentation for the various fields in the P2:CE campaigns.

- [Keys for Campaigns](/modding/p2ce-campaigns/key-reference/01-campaign-keys)
- [Keys for Chapters](/modding/p2ce-campaigns/key-reference/02-chapter-keys)
- [Keys for Maps](/modding/p2ce-campaigns/key-reference/03-map-keys)

There are also [meta keys](/modding/p2ce-campaigns/key-reference/meta-keys) specifically for the P2:CE default interface.

> [!TIP]
> **SEE ALSO:** [Example implementations for Portal 1, Portal 2 & Half-Life 2](https://github.com/StrataSource/p2ce-addons/tree/feat/campaign-tests)

## Overrides
Properties can be overridden for each level (Campaign, Chapter, Map). For example, defining the `background_image` property in both the **Campaign** and **Chapter** block will set the background image to the one defined in the **Chapter** block if the player is currently in that chapter.

This way your campaign can have a customized interface for each chapter.