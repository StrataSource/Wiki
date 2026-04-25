---
title: "Keys for Chapters"
weight: 2
features:
  - USE_CAMPAIGNMANAGER
---
# Keys for Chapters

| Key            | Type   | Details                                                                                                                                 | Optional |
|----------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------|----------|
| `title`        | string | This is the name of the chapter. If a translation key is provided, it will be localized.                                                | No       |
| `save_comment` | string | A string that will be appended to the save file. [More information](/modding/p2ce-campaigns/campaign-progression)                       | Yes      |
| `meta`         | block  | [Meta keys](/modding/p2ce-campaigns/key-reference/meta-keys) for the P2:CE interface. These values apply to all maps unless overridden. | Yes      |
| `maps`         | array  | Array of maps.                                                                                                                          | No       |