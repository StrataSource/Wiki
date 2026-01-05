---
title: Game Examples
weight: 10
---

# Game Examples

This page contains various examples of how to use AngelScript with Strata Source games themselves.

To use the examples, create a new file inside the `(game folder)/code` folder (create the folder if it does not exist yet). `game folder` is Strata Source game sepecific, example for Portal 2: Community Edition: `p2ce`. The scripts have to be saved with the extension `.as`.

Below are examples covering several topics implemented into the latest (as of `5114609d`) Strata Source version for Portal 2: Community Edition. These examples originated from the [StrataSource/sample-content](https://github.com/StrataSource/sample-content) repository and can also be viewed from there under the `code` folder.

## Client

### `ConVar Reference` (`client/cvar_ref.as`)

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

### `Persistant Storage` (`client/persistent_storage.as`)

This script demonstrates how to use the persistent storage API. This implementation closely mirrors the VScript implementation, and the two scripting systems share a backend.

This system may be used to store data in a common area where both VScript and AngelScript can access it.

> [!NOTE]
> This data is NOT networked and is only stored locally!

```as
[ClientCommand("cl_example_storage_show", "Example of how to show script storage data")]
void ShowScriptStorage(CommandArgs@ args)
{
    // Create a storage scope that references "myTest"
    StorageScope s("myTest");

    // Display the values
    Msg("int " + s.GetInt("int") + "\n");
    Msg("float " + s.GetFloat("float") + "\n");
    Msg("string " + s.GetString("string") + "\n");
}

[ClientCommand("cl_example_storage_set", "Example of how to set script storage")]
void SetScriptStroage(CommandArgs@ args)
{
    // Set the values. These will persist across map loads and game restarts, until set or cleared again
    StorageScope s("myTest");
    s.SetInt("int", 1234);
    s.SetFloat("float", 21.25);
    s.SetString("string", "Hello world");
}

[ClientCommand("cl_example_storage_clear", "Clear stuff")]
void ScriptStorageClear(CommandArgs@ args)
{
    // Clear all entries in the myTest storage scope
    StorageScope s("myTest");
    s.ClearAll();
}
```

## Server

### `Entity Iteratiors` (`server/entity_iterator.as`)

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

### `Custom Entity` (`server/entity_remove.as`)

This script demonstrates a custom entity that spawns itself and removes itself when an input is triggered.

> [!WARNING]
> As of writing for current Strata Source version `5114609d`, outputs for entities are not currently implemented and will not work if defined.

```as
[Entity("prop_remove_self")]
class PropRemoveSelf : CBaseAnimating
{
    string m_szModelName = "models/gibs/airboat_broken_engine.mdl";

    void Precache() override
    {
        PrecacheModel( m_szModelName );
    }

    void Spawn() override
    {
        Precache();
        SetModel( m_szModelName );

        SetSolid( SOLID_BBOX );

        Vector vBounds = Vector( 20, 20, 20 );
        SetCollisionBounds( -vBounds, vBounds );
    }

    [Input("UtilRemove")]
    void InputUtilRemove( const InputData &in data )
    {
        Msg("Removing ourselves\n");

        CBaseAnimating@ anim = cast<CBaseAnimating@>(this);
        CBaseEntity@ ent = cast<CBaseEntity@>(anim);
        util::Remove(ent);
    }

    [Input("ClassRemove")]
    void InputClassRemove( const InputData &in data )
    {
        Msg("Removing ourselves\n");

        Remove();
    }
}
```

### `Game Event System` (`server/game_event_system.as`)

This script demonstrates how to use the GameEventManager system to fire and listen for game events.

Game events are optionally networked and are ordinarily used to communicate server data to the client for display on the UI.

Event networking is unidirectional, always going from server -> client. Events fired on the client-side are not sent to the server. Events on the server may also be fired with the 'bBroadcast' parameter set to false to prevent them from being networked.

```as
[ServerCommand("sv_firegameevent_server", "")]
void sv_firegameevent_server(const CommandArgs@ args)
{
    GameEvent@ event = GameEventManager().CreateEvent("player_spawn");

    event.SetBool("BoolValue", true);
    event.SetInt("IntValue", 42);
    event.SetUint64("UInt64Value", 18446744073709551615);
    event.SetFloat("FloatValue", 3.141592);
    event.SetString("StringValue", "suspicious imposter");

    GameEventManager().FireEvent(event);
}

[ServerCommand("sv_firegameevent_client", "")]
void sv_firegameevent_client(const CommandArgs@ args)
{
    GameEvent@ event = GameEventManager().CreateEvent("player_spawn");

    event.SetBool("BoolValue", true);
    event.SetInt("IntValue", 42);
    event.SetUint64("UInt64Value", 18446744073709551615);
    event.SetFloat("FloatValue", 3.141592);
    event.SetString("StringValue", "suspicious imposter");

    GameEventManager().FireEventClientSide(event);
}

[GameEvent("player_spawn")]
void OnPlayerSpawn(const GameEvent@ event)
{
    Msg("Player spawned got fired\n");

    Msg("We got bool value of: " + event.GetBool("BoolValue") + "\n");
    Msg("We got int value of: " + event.GetInt("IntValue") + "\n");
    Msg("We got uint64 value of: " + event.GetUint64("UInt64Value") + "\n");
    Msg("We got float value of: " + event.GetFloat("FloatValue") + "\n");
    Msg("We got string value of: " + event.GetString("StringValue") + "\n");


    Msg("Should be empty: " + event.IsEmpty("DoesNotExistAtAll") + "\n");
    Msg("Should be not empty: " + event.IsEmpty("BoolValue") + "\n");

    Msg("Is Reliable: " + event.IsReliable() + "\n");
    Msg("Is Local: " + event.IsLocal() + "\n");
}
```

### `Physics Object` (`server/physics_object.as`)

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

## Shared

### `Custom Commands` (`server/custom_commands.as`)

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

### `Core Events Types` (`server/init_events.as`)

This script demonstrates/tests various core event types. These are invoked during the game init process.

```as
[LevelInitPreEntity]
void OnLevelInitPreEntity()
{
    Msg("level init pre-entity\n");
}

[LevelInitPostEntity]
void OnLevelInitPostEntity()
{
    Msg("level init post-entity\n");
}

[LevelShutdownPreEntity]
void OnLevelShutdownPreEntity()
{
    Msg("Level shutdown pre-entity\n");
}

[LevelShutdownPostEntity]
void OnLevelShutdownPostEntity()
{
    Msg("Level shutdown post-entity\n");
}
```
