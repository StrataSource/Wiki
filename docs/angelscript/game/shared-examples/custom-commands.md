---
title: Custom Commands
weight: 10
---

# Custom Commands

This script demonstrates how to use ServerCommand and ClientCommand attributes to register custom commands.

```as
#if SERVER
[ServerCommand("sv_example_server_command", "A fun and awesome server command")]
void MyCommand(const CommandArgs@ args)
{
    Msg("This is my server command, called from the server\n");
}
#endif

#if CLIENT
[ClientCommand("cl_example_client_command", "A fun and awesome cheat client command", FCVAR_CHEAT)]
void MyClientCommand(const CommandArgs@ args)
{
    if (args.ArgC() < 2)
        Msg("Woah, pass more args to see something epic!");
    else
        Msg("Arg0 " + args.Arg(0) + ", Arg1 " + args.Arg(1));
}
#endif
```

[Link to Original `sample-content` Example File](https://github.com/StrataSource/sample-content/blob/main/code/shared/custom_commands.as)
