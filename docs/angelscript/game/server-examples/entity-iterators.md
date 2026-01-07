---
title: Entity Iteratiors
weight: 10
---

# Entity Iteratiors

This script demonstrates entity iterators. This system is nearly identical to the VScript system, except that the global object is named differently.

```as
[ServerCommand("sv_test_entity_iterator", "")]
void EntityIteratorExample(CommandArgs@ args)
{
    // Print a list of all func_brushes in the map
    Msg("All func_brushes in this map:\n");
    for (auto@ ent = EntityList().First(); @ent != null; @ent = EntityList().Next(ent)) {
        if (ent.GetClassname() != "func_brush")
            continue;
        Msg(" " + ent.GetEntityIndex() + ": " + ent.GetClassname() + " " + ent.GetDebugName() + "\n");
    }

    // Find the player entity to base our search on
    auto@ player = EntityList().FindByClassname(null, "player");

    if (@player != null) {
        Msg("Entities within 128 units of the player:\n");

        // Search through all entities within 128 units of the player.
        // note that we're repeatedly calling FindInSphere, and not using Next()
        CBaseEntity@ ent = null;
        while ((@ent = EntityList().FindInSphere(ent, player.GetAbsOrigin(), 128)) != null) {
            Msg("  " + ent.GetClassname() + " " + ent.GetDebugName() + "\n");
        }

        // Search for func_brush entities within 2048 units of the player
        Msg("func_brush entities within 2048 units of the player:\n");
        @ent = null;
        while ((@ent = EntityList().FindByClassnameWithin(ent, "func_brush", player.GetAbsOrigin(), 2048)) != null) {
            Msg("  " + ent.GetClassname() + " " + ent.GetDebugName() + "\n");
        }
    }
    else {
        Msg("Unable to find player entity\n");
    }
}
```

[Link to Original `sample-content` Example File](https://github.com/StrataSource/sample-content/blob/main/code/server/entity_iterator.as)
