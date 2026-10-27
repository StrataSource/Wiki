---
title: Physics Object
weight: 40
---

# Physics Object

This script demonstrates how to access and modify physics objects.

```as
// Applies a random impulse to cubes when you trip and stub your toe
[GameEvent("player_hurt")]
void MyCommand(const GameEvent@ event)
{
    // Find all prop_weighted_cube
    CBaseEntity@ ent = null;
    while ((@ent = EntityList().FindByClassname(ent, "prop_weighted_cube")) != null) {
        Msg("Bumped cube " + ent.GetDebugName() + "\n");
        auto@ obj = ent.GetPhysicsObject();
        if (@obj != null) {
            // Wake the object; cubes will go to sleep when powered by a laser or after chillin for a while.
            obj.Wake();

            // Apply random velocity and angular impulse
            obj.AddVelocity(RandomVector(-2000, 2000), RandomVector(-5000, 5000));
        }
    }
}
```

[Link to Original `sample-content` Example File](https://github.com/StrataSource/sample-content/blob/main/code/server/physics_object.as)
