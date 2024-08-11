---
title: Wiki Structure
---

# Wiki Structure

The wiki is structured on 3 levels:

-   Category
-   Topic
-   Article

## Categories

Categories group articles together by a specific feature set, like Panorama UI.

Categories are located inside the [`docs` folder](https://github.com/StrataSource/Wiki/tree/main/docs) in the repo and all contain a `meta.json` file. This file includes all information needed about the category, like it's title:

```json
{
    "title": "Contribute"
}
```

## Topics

Topics, also knows as Subcategories, divide categories into different sections like `Overview`, `Controls` and `Reference`.

Topics are folders inside categories and also have their own `meta.json` file:

```json
{
    "title": "Basics",
    "weight": 10
}
```

The `weight` property is optional and tells the wiki how to sort the topics: Bigger weight means a topic will move further down. If no weight is specified, the wiki will default to infinite weight, making the topic appear at the bottom of the list.

## Articles

Articles are the pages that make up the content of the wiki. Most articles are written by hand, but some are automatically generated from engine dumps and enhanced by manually written content.

Articles that are fully manually written can be found as Markdown files inside topics. You can read about how these files are structured in [Editing Articles](../basics/editing-articles).
