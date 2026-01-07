---
title: Creating & Editing Articles
weight: 10
---

# Creating & Editing Articles

## Creating An Article

Articles on the Strata Source Wiki consist of Markdown files that are inside topics. Topics are the folders that make up certain sections of categories. Example of `Category/Topic/Article`: `Audio/Overview/Sound System`. These Markdown files are placed into where they should displayed in the Wiki.

For example, if you wish to add a article to the "Overview" topic in the "Panorama" category, all that needs to be done is to make a new Markdown file in the "docs/panorama/overview" folder.

For more information on the Wiki's structure, please read [Wiki Structure](./structure).

> [!NOTE]
> It highly recommended that the Markdown file names are named after the title of the article as well as not containing any spaces or symbols with the exception of dashes ("-") to replace spaces.
> Example: `article-title-here.md`.
>
> The same should go for creating new topic folders, keep it simple and understandable.

## Meta Block

Every article starts with a meta block like this:

```yaml
---
title: VScript Introduction
weight: 5
features:
    - USE_VSCRIPT
---
```

It contains metadata about the article you're currently viewing, like the title to display in the sidebar, the weight used for sorting or the [features flags](feature-flags) required for this page to be considered supported.

## Top Level Heading

By default no heading will be shown, **even if you specified the `title` property**. To make sure the user knows what the article is about, include a top level heading directly after the meta block like this:

```md
# VScript Introduction
```

While this doesn't need to be the same as the one you specified in the `title` property, it is generally recommended for them to be same.

## Writing The Article

After that follows the article content that'll get shown on the page. What is written usually doesn't follow a specific pattern.

## Adding Links To Articles

If another article needs to be linked in the Wiki, the path to the article Markdown file must be used without the extension. Relative paths can also be used instead of the full file path if desired.

```md
[Insert Article Here](./my-fantastic-article)
```

To add a link to other categories or topics on the Wiki, the same method is used, simply include the full or relative path.

```md
[Here's A Great topic](category/a-not-so-great-topic)
```
