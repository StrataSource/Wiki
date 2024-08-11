---
title: Editing articles
weight: 10
---

# Editing articles

## Meta block

Every article starts with a meta block like this:

```yaml
---
title: VScript Introduction
weight: 5
features:
    - VSCRIPT
---
```

It contains metadata about the article you're currently viewing, like the title to display in the sidebar, the weight used for sorting or the [features flags](feature-flags) required for this page to be considered supported.

## Top level heading

By default no heading will be shown, **even if you specified the `title` property**. To make sure the user knows what the article is about, include a top level heading directly after the meta block like this:

```md
# VScript Introduction
```

While this doesn't need to be the same as the one you specified in the `title` property, it is generally recommended for them to be same.

## Writing the article

After that follows the article content that'll get shown on the page and usually doesn't follow a specific pattern.
