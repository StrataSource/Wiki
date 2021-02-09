# Markdown Help

This page may only be interesting to people that wish to [contribute](https://github.com/ChaosInitiative/Wiki) to the wiki.

Markdown syntax is used for wiki pages, that then get converted into HTML. Here is a summary of some of markdown's capabilities
# Standard features

## Headings

Headings in markdown are written like this
```
# This is a level 1 heading (page title)
## This is a level 2 heading (page chapters)
### This is a level 3 heading (subchapters)
#### This is a level 4 heading (sub-subchapters)
##### This is a level 5 heading ...
###### This is a level 6 heading ...
```

On this wiki, all headings have an anchor next to it which redirects the user to the current page but scrolled down to the clicked heading. This is very useful for sharing links with others that jump them straight to the desired heading.

## Emphasis
Text can be highlighted in multiple ways. **Bold**, *Italic* and ~~strikethrough~~.
```
I am **bold**
I am *Italic* and _I am too_
I am ~~deleted~~
```

## Links
Links can be embedded right into a markdown document. The display text of the link can be chosen as well
```
Visit our homepage [here](https://chaosinitiative.com)
```

Visit our homepage [here](https://chaosinitiative.com)

## Lists
Lists and nested lists can be created in multiple ways
```
- I am a list
- With some elements
* You can also use this character,
* but it will create a separation from the other
* characters
+ plus also works
+ and the enumeration symbol at the start will always be the same
```
- I am a list
- With some elements
* You can also use this character,
* but it will create a separation from the other
* characters
+ plus also works
+ and the enumeration symbol at the start will always be the same

Ordered lists are simple. No matter which digit is used at the start, the list items will always increment
```
1. Element 1
1. Element 2
1. Element 3
1. Element 4
```
1. Element 1
1. Element 2
1. Element 3
1. Element 4

## Codeblocks
Code is essential for developers and should **always** be put into codeblocks and never as normal text.
```
a```
This is a normal codeblock without any syntax highlighting
Don't actually put the a at the start. It's only there because writing
code blocks inside code blocks is otherwise really tough
a```
```

```
This is a normal codeblock without any syntax highlighting
```
Code can also be syntax-highlighted
```
a```javascript
// This is a comment
function hello(b) {
    let a = b * 2;
    console.log("This is some javascript");
}
a```
```
```js
// This is a comment
function hello(b) {
    let a = b * 2;
    console.log("This is some javascript");
}
```

Inline code blocks can be used to highlight text like file paths or names.

```
This paragraph has some `inline` code `inserted into it`.
```
This paragraph has some `inline` code `inserted into it`.


## Horizontal rule
Horizontal rules can be used to visually split up a document
***
There is a horizontal rule right between here

```
***
```
## Quotes
Quotes can be used to add some visual interest to some important text that shouldn't be treated as code

> I am a quote

> Quotes  
> can be multiline



## Images
Images are easy to embed. Please upload images to some external provider like [imgur](https://imgur.com/)
![This text will be displayed if the image can't be loaded](https://imgur.com/JGrpYBw.png)
```
![This text will be displayed if the image can't be loaded](https://imgur.com/JGrpYBw.png)
```

> Tip: Quotes and images can be combined to provide subtitles for an image

![This text will be displayed if the image can't be loaded](https://imgur.com/JGrpYBw.png)
> Logo of Portal 2: Community Edition 

## Tables
Tables are rather complex and only a simple example will be shown here.

| Feature | Portal 2: Community Edition | Momentum Mod |
| ------- | :---: | :---: |
| Ladders | ✔ | ✔ |
| Multiple projected textures | ✔ | ✔ |
| Paintgun | ✔ | ❌ |
| Sticky bombs | ❌ | ✔ |
| Source 2 | ❌ | ❌ |

# Non standard features
This wiki uses extended markdown syntax. Sites like GitHub won't be able to display it properly, but the wiki can display it. These are the available extensions:

## Footnotes
Footnotes can be used to add references in text that link to the bottom of the page for further clarification. Useful for citations.
```
Here is a footnote reference,[^1] and another.[^longnote]

This is another reference to [^1]

[^1]: Here is the footnote.

And another reference to [^longnote]

[^longnote]: Here's one with multiple blocks.

    Subsequent paragraphs are indented to show that they
belong to the previous footnote.

    > This is a block quote
    > Inside a footnote

        { some.code }

    The whole paragraph can be indented, or just the first
    line.  In this way, multi-paragraph footnotes work like
    multi-paragraph list items.

```
Here is a footnote reference,[^1] and another.[^longnote]

This is another reference to [^1]

[^1]: Here is the footnote.

And another reference to [^longnote]

[^longnote]: Here's one with multiple blocks.

    Subsequent paragraphs are indented to show that they
belong to the previous footnote.

    > This is a block quote
    > Inside a footnote

        { some.code }

    The whole paragraph can be indented, or just the first
    line.  In this way, multi-paragraph footnotes work like
    multi-paragraph list items.

This paragraph won't be part of the note, because it
isn't indented.
.

## Emoji
Emoji can be used the same way as on Discord, Youtube and many other platforms :ok_hand: :sunglasses: :flushed:

```
:ok_hand: :sunglasses: :flushed:
```

## Alerts and other containers
Custom containers can be created like this
```
:::
This text is in a custom container
:::
```

```
This text is ::inline::
```

This isn't useful on its own, however, it is possible to add style classes to these containers. This can be used to create alerts for bug notices or the like.

This can be used for badges ::Like this::{.badge .badge-primary}

```
This can be used for badges ::Like this::{.badge .badge-primary}
```

:::{.alert .alert-success}
I'm making a note here: Huge success!
:::

:::{.alert .alert-info}
This is very awesome!
:::

:::{.alert .alert-warning}
Be warned, I'm yellow
:::

:::{.alert .alert-danger}
Something is wrong here
:::

```
:::{.alert .alert-success}
I'm making a note here: Huge success!
:::

:::{.alert .alert-info}
This is very awesome!
:::

:::{.alert .alert-warning}
Be warned, I'm yellow
:::

:::{.alert .alert-danger}
Something is wrong here
:::
```

## Extra Emphasis
In addition to the normal emphasis, this wiki allows for some additional styles.

H~2~O is a liquid. 2^10^ is 1024

```
H~2~O is a liquid. 2^10^ is 1024
```

This paragraph contains ++Inserted text++ right here

```
This paragraph contains ++Inserted text++ right here
```

To make an important part of a sentence really stand out ==text can be marked== like this

```
To make an important part of a sentence really stand out ==text can be marked== like this
```
