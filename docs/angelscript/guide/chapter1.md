---
title: Chapter 1 - Introduction
weight: 0
---

# Chapter 1 - Introduction

## What will you learn in this chapter
You will learn about:
- AngelScript as a programming language,
- Purpose of AngelScript in Strata Source,
- Client - Server model of the engine,
- How to load code in the game,
- Writing your own Hello World program.

> [!CAUTION]
> This guide assumes you have basic skills of programming in languages like Python, C/C++, Squirrel (VScript), etc.
> It is recommended you already have experience in programming, although this guide aims to be as begineer's friendly as possible.
> Basic concepts will **not** be taught.

---

## AngelScript
The [AngelScript's home page](https://www.angelcode.com/angelscript/) describes AngelScript as:
> The AngelCode Scripting Library, or AngelScript as it is also known, is an extremely flexible cross-platform scripting library designed to allow applications to extend their functionality through external scripts.

Besides that, you can treat AngelScript as some sort of hybrid between C++ and Python. In some areas it behaves like C++, for example it is staticly typed, meaning that when you are declaring a variable you also have to declare it's types, and it also implements it's own version of pointers (called handles); it also aims to help out users in writing code, whether by dissallowing certain operations or by assuming. More on that will be explained in later parts of the guide.

Its use cases vary, it is much closer to pure engine code than VScript, meaning that you can for example program in custom entities, or custom commands.

Its official documentation can be found here: [AS Official Docs](https://www.angelcode.com/angelscript/sdk/docs/manual/doc_script.html).


## What can you do with AngelScript
This question is not properly asked, because AngelScript will allow you to do mostly anything you want, however it's main task in Strata Source is to allow users to create custom entities, create custom commands, bind to in-game events, and more.

While VScript (mainly) sits between entities and handles the interactions between them, AngelScripts sits in a level above, where AS can be treated as entities *themselves*.

---

## AngelScript in Strata Source

### Client - Server model
Before we get into writing your first script, there is one more thing you need to know. Most engines including Source in general, operate on the client-server model. Meaning that client code is separate from the server code, even on singleplayer. When you start a map in singleplayer you essentially create a one-player server that runs beside the client. This is very important because AS code can be loaded on both. Some functionality will only be available on the server (like entities) and some functionality will only be available on the client (like Panorama/UI).


### Loading code
Your first question might be: Where do I place the files containing my code?
The answer is pretty simple, each file that contains your code should be ended with the **.as** extension and be placed in the **code/** folder of a respective `Game` searchpath. Example locations would be `p2ce/custom/my-addon/code/<files>` or just `p2ce/code/<files>` (the latter not being recommended).

You can name your files however you'd like. You can create custom directories, you can loosely place files, it all depends on what you're trying to achieve; in the long run it doesn't matter. What does matter are the "starting points" of sorts. The engine will not attempt to load any files besides 3 files placed **directly** in the **code/** folder:

1. `init.as` - Will get loaded by server and client.
2. `sv_init.as` - Will only get loaded by the server.
3. `cl_init.as` - Will only get loaded by the client.

### Your first script
Now, you should be ready to write your very first and own program that will print a Hello World message to the console. You might not know everything in the code below but don't get dissappointed! You should place this code into `cl_init.as` as it is a client command.

```cpp
[ClientCommand("HelloWorld", "")]
void MyCommand(const CommandArgs@ args) {
    Msg("Hello world from AngelScript!\n"); // You can place your own text here!
}
```

Now, the only thing left is to launch up the game, open the console and execute the *HelloWorld* command.

## Tips

> [!TIP]
> Reading console output can be tiresome as much more is happening in the console than just the script system. However, there is an easy way to just listen to the script system output. You can run `con_filter_text scriptsys; con_filter_enable 1` filter out anything that is not the script system.
