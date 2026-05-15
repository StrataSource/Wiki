---
title: ConVar Reference
weight: 10
---

# ConVar Reference

This script demonstrates ConVar refences. These are the preferred way to interact with ConVars, and the only way to interact with ones registered outside of your script.

```as
[ClientCommand("cl_example_cvarref")]
void MyCvarRefDemo(const CommandArgs@ args)
{
    ConVarRef intensity("r_portal_light_intensity");

    Msg("is r_protal_light_intensity valid? " + intensity.GetBool() + "\n");
    Msg("current val: " + intensity.GetFloat() + "\n");

    intensity.SetValue(1);
    Msg("New val: " + intensity.GetFloat() + "\n");

    ConVarRef invalid_cvar("my_invalid_thingy");
    Msg("is my_invalid_thingy valid? " + invalid_cvar.IsValid() + "\n");
}
```

[Link to Original `sample-content` Example File](https://github.com/StrataSource/sample-content/blob/main/code/client/cvar_ref.as)
