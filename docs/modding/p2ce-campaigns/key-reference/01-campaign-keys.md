---
title: "Keys for Campaigns"
weight: 1
features:
  - USE_CAMPAIGNMANAGER
---
# Keys for Campaigns

| Key          | Type    | Details                                                                                                                                          | Optional |
|--------------|---------|--------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| `title`      | string  | This is the name of the campaign. If a translation key is provided, it will be localized.                                                        | No       |
| `unlock_all` | boolean | Determines if all chapters are unlocked and no unlock state should be tracked. (This is set to `false` by default)                               | Yes      |
| `meta`       | block   | [Meta keys](/modding/p2ce-campaigns/key-reference/meta-keys) for the P2:CE interface. These values apply to all chapters/maps unless overridden. | Yes      |
| `chapters`   | array   | Array of chapters.                                                                                                                               | No       |