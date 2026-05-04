---
title: Code Blocks
weight: 10
---

# Code Blocks

The Wiki supports using backticks ( \` ) and triple backticks ( \``` ) to make code blocks for file content. Tildes ( ~ ) can also be used but most often backticks are used. Tildes are useful if triple backticks need to be escaped. (`~~~ ``` content ``` ~~~`) Single backticks are used for small singular lines or phrases while triple backticks are used for larger multiline code blocks. Double backticks can be used to to escape backticks if a literal backtick is needed.

Code blocks allows for nice highlighting for various programming languages and making it easy to read files and code. Code blocks support highlighting for specific languages. Highlighting support has been added for VDF and KV files for the Source Engine. A full list of available languages that can be highlighted can be found here: <https://highlightjs.readthedocs.io/en/latest/supported-languages.html>

Using triple backticks followed by the language of choice, the code block will highlight various syntax, types, and keywords with various coloring.

Examples:

Markdown: `` `Single Backticks` `` Preview: `Single Backticks`

Markdown:

~~~markdown
```cpp
[ClientCommand("HelloWorld", "")]
void MyCommand(const CommandArgs@ args) {
    Msgl("Hello world from AngelScript!");
}
```
~~~

Preview:

```cpp
[ClientCommand("HelloWorld", "")]
void MyCommand(const CommandArgs@ args) {
    Msgl("Hello world from AngelScript!");
}
```

The Wiki adds a special feature with code blocks where a file can also be specified with the highlighting type.

Example:

~~~markdown
```kv :: example_rectmap.rect
Rectangles
{
    rectangle
    {
        min "0 0"
        max "512 32"
    }
    rectangle
    {
        min "512 0"
        max "768 32"
    }
}
```
~~~

Preview:

```kv :: example_rectmap.rect
Rectangles
{
    rectangle
    {
        min "0 0"
        max "512 32"
    }
    rectangle
    {
        min "512 0"
        max "768 32"
    }
}
```
