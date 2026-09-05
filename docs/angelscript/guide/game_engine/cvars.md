---
title: ConVars & ConCommands
weight: 2
features:
    - USE_ANGELSCRIPT_GAME
---

# ConVars & ConCommands

Sections in this article:

- [Introduction](#introduction)
- [ConVars](#convars)
  - [ConVar Basics](#convar-basics)
  - [Reading and Writing To ConVars](#reading-and-writing-to-convars)
  - [Referencing ConVars With ConVarRef](#referencing-convars-with-convarref)
  - [ConVar Callbacks](#convar-callbacks)
- [ConVar & ConCommand Flags](#convar--concommand-flags)
- [ConCommands](#concommands)
  - [Setting Up ConCommands](#setting-up-concommands)
  - [ConCommand Arguments](#concommand-arguments)

## Introduction

Console Variables and Console Commands, ConVar and ConCommand for short, are various variables and commands that can be inputted into the Source Engine console. ConVars are able to store numbers, strings, and other variable types for the engine whether you are a in a map are not. ConCommands are similar, but they are used to run various actions for the engine, they also support arguments.

Strata Source's AngelScript supports being able to read and create both ConVars and ConCommands for the engine at runtime. ConVars are able to store various information for you or users to use while in game, but they can persist between game sessions and can be modified in the console. ConCommands however can not be executed when not in a game session since the code for them is not available outside of the game session.

ConVars and ConCommands for AngelScript behave similarly as they do in normal engine code, so information about them on the VDC will be mostly accurate for AngelScript. The following links can help provide any additional information that might not be here, still though not everything will apply or be accurate for Strata's AngelScript.

- ConVars: <https://developer.valvesoftware.com/wiki/ConVar>
- ConCommands: <https://developer.valvesoftware.com/wiki/Developer_Console_Control>

If you wish to instead of reading, but watch a tutorial on working with AngelScript and getting started with ConVars and Commands, the Portal Mapping and Modding YouTube Channel has a video covering them both.

![PMAM AS Tutorial](https://youtu.be/qJuLpiMoE0E)

## ConVars

### ConVar Basics

ConVars are easy to setup and get working. For making ConVars, it is a single line of code done in the global scope of your script file.

```c++
ConVar the_convar("the_convar", "1", FCVAR_NONE);
```

In the example above, we are constructing a variable named `the_convar` that will represent a ConVar name "the_convar". The variable name and the name of the ConVar to be made do not need to match, but its helpful when needing to reference your ConVar to get information from it in your script file.

The second parameter of the constructor is a string representing the default value of your ConVar. Whether you value is a integer, bool, color, etc, it needs to be inputted as a string. This value is referenced when you wish to reset your ConVar to its default value using `ConVar::Reset()` or `ConVarRef::Revert()`, or simply getting what the default value is with `ConVar::GetDefault()` or `ConVarRef::GetDefault()`.

Last parameter is the flags for the ConVar. By default this is `FCVAR_NONE`, which is a enum stand in for `0`. This means that the ConVar has no special behaviors or functionality to it for the engine to handle. `the_convar` will simple store its value and will be destroyed when the game is closed.

ConVars can be created with various flags for the engine to perform various actions based on ConVar changes or make the ConVar behave in certain ways. These flags also work for ConCommands. All the available flags for ConVars and ConCommands are defined in the `EConVarFlag` enum. `FCVAR_NONE` is one of these enums and is a stand in for `0` which means that ConVar will behave without any special behavior and simply store values. Note, that once flags are set, they can not be changed later. Flags in ConVars can only be retrieved with `ConVarRef::GetFlags()`. For more information on flags, please read [ConVar & ConCommand Flags](#convar--concommand-flags).

ConVars are able to be made in both Server and Client contexts without any difference, only issue being that each context can only directly access a ConVar in their respective context. If a Server side ConVar must be accessed by the Client and vise-versa, then [ConVarRef](#referencing-convars-with-convarref) should be used.

### Reading and Writing To ConVars

Once you have created you ConVar, you would want to be able to read the value and change its value. The ConVar class comes with getter and setter functions that can be used to read and write to and from ConVars. Note that even though the initial value of the ConVar is set as a string, it can be set later using more direct values and can be retrieved as various types. You can also see below how `ConVar::Reset()` can be used to reset the ConVar back to its initial value.

```c++
void Func()
{
    Msgl(the_convar.GetString()); // Prints "1"

    the_convar.SetValue(123);
    Msgl(the_convar.GetInt()); // Prints "123"

    the_convar.SetValue(24.123);
    Msgl(the_convar.GetInt()); // Prints "24"
    Msgl(the_convar.GetFloat()); // Prints "24.123"

    Msgl(the_convar.GetDefault()); // Prints "1"
    the_convar.Reset();
    Msgl(the_convar.GetString()); // Prints "1"

    tho_convar.SetValue("some_characters");
    Msgl(the_convar.GetString()); // Prints "some_Characters"
    Msgl(the_convar.GetInt()); // Prints nothing, there is no valid number to pull from string
    tho_convar.SetValue("some_characters_20");
    Msgl(the_convar.GetString()); // Prints "some_Characters_20"
    Msgl(the_convar.GetInt()); // Prints "20"

}
```

### Referencing ConVars With ConVarRef

While it is easy to access any created ConVars in the global scope of your script file, what if you wanted to access other ConVars in other script files you have? Or what if you wanted to read and write to ConVars that are part of the engine already?

For the former, you could include the script file in your current script file to access its ConVars, but this is generally not very recommended. As for the latter, you will need something specific to get your hands on them.

`ConVarRef` comes to the rescue as it allows you to reference ConVars without needing access to the original ConVar definition.

```c++
void Func()
{
    // Engine ConVar
    ConVarRef sv_cheats("sv_cheats");
    if (!sv_cheats.IsValid())
    {
        Msgl("Uhh this should exist???");
        return;
    }

    // Script made ConVar
    ConVarRef the_convar("the_convar");
    if (!the_convar.IsValid())
    {
        Msgl("Woops, you messed up something!");
        return;
    }

    string strVal = sv_cheats.GetString();
    Msgl(strVal);
    strVal = the_convar.GetString();
    Msgl(strVal);
}
```

### ConVar Callbacks

Last part of a ConVar constructor is a optional parameter for a `ChangeCallback` function. What this is a callback function that's called whenever the ConVar changes it's value. This allows for checking set values, previous values and other aspects fo the ConVar to further work with it.

```c++
ConVar(const string&in name, const string&in defValue, EConVarFlag flags, ConVar::ChangeCallback&in changeCallback);

funcdef void ChangeCallback(ConVar&in, const string&in prevStr, float prevVal);
```

```c++
void MyConVarCallback(ConVar&in cv, const string&in prevStr, float prevVal)
{
    Msgl("ConVar previous value, string: {}".format(prevStr));
    // This line won't work properly if characters are used instead of numerical values.
    Msgl("ConVar previous value, float: {}".format(prevVal));

    Msgl("ConVar current value: {}".format(cv.GetFloat()));

    if (cv.GetBool())
    {
        Msgl("The ConVar value is greater than zero!");
    }
    if (cv.GetString().length > 0)
    {
        Msgl("ConVar has a string value!");
    }
}

// The parameter for ConVar flags is required since no overload is available without it. FCVAR_NONE can be used if one is not wanted.
ConVar the_convar("the_convar", "0", FCVAR_NONE, MyConVarCallback);
```

## ConVar & ConCommand Flags

Flags are used to make ConVars and ConCommand behave in certain ways or have the engine do specific things with them. Flags can be set to ConVars and ConCommands when they are created, but flags can not be modified afterward, only retrieved with `ConVarRef::GetFlags()`. This also applies to engine made ConVars adn ConCommands.

Flags can be combined using bitwise OR with other flag enum values, or you can use a direct value that is equivalent combination of the flags, but the former is more recommended.

> [NOTE!]
> Not all flags work on either ConVars or ConCommands a lot of them are designed to be used for just ConVars, like `FCVAR_ARCHIVE`.

```c++
ConVar the_convar_with_more_flags("the_convar_wmfs", "1", FCVAR_HIDDEN | FCVAR_NOTIFY | FCVAR_CHEAT);
```

Below are some flags that can be useful with AngelScript with a small description:

- `FCVAR_HIDDEN`: CVars defined with this will not show up in the console autocomplete, but can still be used normally.
- `FCVAR_SPONLY`: CVars defined with this can only be changed when clients are not connected to a server
- `FCVAR_ARCHIVE`: **ConVars** defined with this will be saved the ConVar locally to disk, more specifically to the `Steam\userdata\(userid)\440000\local\p2ce\cfg\config.cfg` and `Steam\userdata\(userid)\440000\remote\p2ce\cfg\config.cfg` directories where ConVars can be set on game load. (ACTUALLY TEST IF IT CAN SET THE PREVIOUSLY DUMPED CVARS ONCE ANGELSCRIPT INITS THE CVARS AGAIN)
- `FCVAR_NOTIFY`: ConVars defined with this will send a message in the chat that the ConVar's value has changed and the value it changed to.
- `FCVAR_CHEAT`: CVar defined with this require `sv_cheats` to be enabled for it to be changed or executed.

## ConCommands

### Setting Up ConCommands

ConCommands behave differently from ConVars in how they are defined. They follow the [Server-Client](server-client) structure more strictly than ConVars. ConVars have the benefit of being able be access Server or Client side freely using [ConVarRef](#referencing-convars-with-convarref), ConCommands do not have this benefit.

ConCommands are defined using attribute tags applied to functions that declare which type of ConCommand should be created. For Server side code, they are defined with `ServerCommand` while Client is defined with `ClientCommand`. A required piece for either ConCommand type is having the `const CommandArgs@ args` parameter for the engine to pass the arguments inputted into the console to the ConCommand. Without the parameter, the script will not compile. Look below for more information on [ConCommand arguements](#concommand-arguments).

```c++
#if SERVER

[ServerCommand("sv_my_server_command", "A fun and awesome server command!")]
void MyCommand( const CommandArgs@ args )
{
    Msgl("This is my server command, called from the server!");
}

#endif

#if CLIENT

[ClientCommand("cl_my_client_command", "A fun and awesome cheat client command", FCVAR_CHEAT)]
void MyClientCommand(const CommandArgs@ args)
{
    // The arguments are made up by the whole command, so when a command is inputted by itself with no arguments, there will always be at least one argument.
    if (args.ArgC() < 2)
    {
        Msg("Woah there! You gotta pass more args than that buddy!");
    }
    else
    {
        // CommandArgs has a operator overload for [] to allow getting arguments without using the `Arg(int idx)` function.
        Msg("Arg0 " + args.Arg(0) + ", Arg1 " + args[1]);
    }
}

#endif
```

Whether it's in the Server or Client context, the ConCommands themselves operate the same, just that any Client ConCommands will only be registered for the client the code executed for. This is useful in multiplayer situations where there should be commands that only the client can execute on itself.

### ConCommand Arguments

The `const CommandArgs@ args` parameter is required on all ConCommand definitions in order for the engine to pass parameters inputted into the console to the ConCommand. The script will not compile without it.

`CommandArgs` is a class object that is passed in that can be accessed to read inputted parameters, know how many arguments were passed, and get the full string that was passed into the console. You can

```c++
class CommandArgs
{
    int ArgC() const;
    string GetCommandString() const;
    string Arg(int idx) const;
    string opIndex(int idx) const;
}
```

> [!NOTE]
> The arguments come from a zero indexed array, meaning that the 0th argument is the ConCommand itself that has been entered. The arguments are made up by the whole command, so when a command is inputted by itself with no arguments, there will always be at least one argument which is the ConCommand itself.
