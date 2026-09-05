---
title: Server-Client Code
weight: 1
features:
    - USE_ANGELSCRIPT_GAME
---

# Server-Client Code

## Introduction

AngelScript, like the Source Engine itself, has both Server and Client code. Server code is always loaded prior to the client code, even for hosts.

Server and Client code can be loaded in several ways:

* `init.as`: This initialization file is executed for both Server and Client contexts.
* `sv_init.as`: This file is executed for only Server code.
* `cl_init.as`: This file is executed for only Client code.

If using `init.as`, special care must be taken to make sure the AngelScript system won't error if Server or Client code comes across classes, functions, or other bindings that aren't defined to be on one or the other. The solution to this is using preprocessor macros.

The AngelScript system supports two macros, `SERVER` and `CLIENT` each respectively defined when either the Server or Client code is ran. `#if` and `#endif` are used to define the bounds of where these two macros operate. Together with includes, this helps ensure that your AngelScript code can be loaded in both contexts if using a `init.as` file. Then again, `sv_init.as` and `cl_init.as` can be separately used to make sure that the compiler only uses Server or Client contexts. The macros are required if you have a file with shared code that is used between both contexts.

```c++
#if SERVER

[LevelInitPreEntity]
void OnLevelInitPreEntity()
{
    Msgl("LOADING SERVER!");
}

[LevelShutdownPreEntity]
void OnLevelShutdownPreEntity()
{
    Msgl("SHUTTING DOWN SERVER!");
}

#include "my_server_code.as"
#include "server/my_other_server_code.as"

#endif

#if CLIENT

[LevelInitPreEntity]
void OnLevelInitPreEntity()
{
    Msgl("LOADING CLIENT!");
}

[LevelShutdownPreEntity]
void OnLevelShutdownPreEntity()
{
    Msgl("SHUTTING DOWN CLIENT!");
}

#include "my_client_code.as"
#include "client/my_other_client_code.as"

#endif
```

## GameEvents

As of writing, 2026/09/02, Server and Client contexts have no exact direct way of communicating to one another through code. However, client side code is able to receive GameEvents that were sent from the Server and vise versa. This isn't a intuitive way of Server-Client communication and is not recommended for anything too intensive. On top of this, custom game events are not possible through addons as GameEvents require event definitions to be defined in the `gameevents.res` or `modevents.res` file which are only loaded at engine start. SourceMods can use their own versions of the GameEvent definition files to load custom events.

For more information on how to use GameEvents, please check out the [GameEvents guide](gameevents).
