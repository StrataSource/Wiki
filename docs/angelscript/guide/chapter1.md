---
title: Chapter 1 - Introduction
weight: 0
---

# Chapter 1 - Introduction

## What You Will Learn
In this chapter you will learn about:
- [AngelScript as a programming language](#angelscript)
- [Purpose of AngelScript in Strata Source](#what-can-you-do-with-angelscript)
- [Client-Server model of the engine](#client---server-model)
- [How to load code in the game](#loading-code)
- [Writing your own Hello World program](#your-first-script)
- [Testing out your own code](#how-to-test-out-your-code-in-a-basic-way)
- [Additional tips that might help you](#additional-tips)

> [!TIP]
> In each chapter, you can easily navigate the page by clicking the links in the "What You Will Learn" section.

> [!CAUTION]
> This guide assumes you have basic programming skills in languages such as Python, C, C++, Squirrel (VScript), etc.
> It is recommended you already have *some* experience in programming, although this guide aims to be as beginner-friendly as possible.
> Basic concepts will **not** be taught.

> [!NOTE]
> It is recommended to try out what you learn in this guide as you go through it. This guide will include example tasks for you to attempt as practice.

---

## AngelScript
[AngelScript's home page](https://www.angelcode.com/angelscript/) describes AngelScript as:
> The AngelCode Scripting Library, or AngelScript as it is also known, is an extremely flexible cross-platform scripting library designed to allow applications to extend their functionality through external scripts.

Besides that, AngelScript commonly behaves like C++ - for example, when it is statically typed. Just as in C++, when you declare a variable in AngelScript, you also must declare its types. In addition, AngelScript also implements its own version of pointers (called handles). It also aims to help users in writing its code, whether by disallowing certain operations or by assuming. More on that will be explained in later parts of the guide.

Use cases for AngelScript vary heavily. It is much closer to pure engine code than VScript, meaning that you can achieve outputs not possible in VScript, such as programming in custom entities and custom commands.

AngelScript's official documentation can be found here: [AS Official Docs](https://www.angelcode.com/angelscript/sdk/docs/manual/doc_script.html).


## What Can You Do With AngelScript
ngelScript allows for a closer connection to the internal engine code by having the engine provide various APIs to its internal classes. This allows you to do various things, such as creating custom entities, creating your own ConCommands and ConVars, making custom weapons - all things that aren't normally easy to do with VScript.

While VScript (mainly) sits between entities and handles the interactions between them, AngelScripts sits in a level above, being able to *create* entities and define their behavior.

---

## AngelScript in Strata Source

### Client - Server Model
Before you write your first script, there is one more thing you need to know. Most engines, including the Source engine, operate on the client-server model. This means that client code is separate from the server code, even in singleplayer. When starting a map in singleplayer, you essentially create a one-player server that runs beside the client. This is very important to remember as AS code can be loaded on both. Some functionality will only be available on the server (such as entities) and some functionality will only be available on the client (such as Panorama/UI).


### Loading Code
Where should you place the files containing your code?
Each file that contains your code should end with the **.as** extension and be placed in the **code/** folder of your respective `Game` searchpath. Example locations would be `p2ce/custom/my-addon/code/<files>` or just `p2ce/code/<files>` (the latter is not recommended).
Code can also be placed inside the `code` folder of an addon created with the SDK Launcher.

You may name your files however you'd like. You can create custom directories or you can place your files loosely - it all depends on what you're trying to achieve. In the long run, it's not important. What *is* important is where you place the "starting points". The engine will not attempt to load any files except for these 3 files placed **directly** in the **code/** folder:

1. `init.as` - Will get loaded by server and client.
2. `sv_init.as` - Will only get loaded by the server.
3. `cl_init.as` - Will only get loaded by the client.

### IDE and Testing Environment
It is suggested to use Visual Studio Code with the [AngelScript Language Server (sashi0034.angel-lsp)](https://marketplace.visualstudio.com/items?itemName=sashi0034.angel-lsp) extension. From there, you can open the `code/` folder of your choice as a project and begin development.
The engine compiles scripts on every map load (you can use the `reload` command to recompile the scripts).

### Your First Script
You should now be ready to begin writing your very first program. For now, let's just print a Hello World message to the console. Though the code below may look foreign for now, don't be dissuaded! Place this code into `cl_init.as` as it is a client command.

```cpp
[ClientCommand("HelloWorld", "")]
void MyCommand(const CommandArgs@ args) {
    Msg("Hello world from AngelScript!\n"); // You can place your own text here!
}
```

Now, the only thing left to do now is launch the game, open the console, and execute the *HelloWorld* command.

> ### TASK 1: 
> Run the HelloWorld program mentioned above.

## How To Test Out Your Code in a Basic Way
For now, you will need to know how to run your code so that you can complete the tasks given to you within this guide.
In `sv_init.as` include:
```cpp
[ServerCommand("CodeTest", "")]
void CodeTest(const Command@ args) {
    // Here you can put your code
}
```

The code in this function will run whenever you run the `CodeTest` command in game. Remember to `reload` to see the changes!
The `Msg(string)` function will serve as a way to view your variables (like print or cout). Just type `Msg(a)` where *a* is your variable, and *a* will be printed to the console.
Remember to add `"\n"` to the input of Msg (or just call `Msg("\n");` after your message), otherwise everything will print in one line. To avoid having to do this, you can use the `Msgl(string)` which will automatically append an `"\n"` to the end of each message.

> [!BUG]
> Some types such as `int` cannot be directly converted to string, and as such, you won't be able to put them directly into Msg().
> > [!TIP]
> > In order to avoid this issue, you can append to an empty string. Just do `"" + a` and in most cases this will work: `Msg("" + a);`

### Compilation Errors
Scripts will often report errors before they are ran, usually on map load. If you don't see your functionality (such as a command not being the console), scroll up and check the error. Additionally, you can use the first tip in the [tip section](#additional-tips) and then use `reload`.


## Additional Tips

> [!TIP]
> Reading console output can be tiresome, as much more is happening in the console than just the script system. To overcome this problem, you can run `con_filter_text scriptsys; con_filter_enable 1` to filter out anything that is not the script system.
