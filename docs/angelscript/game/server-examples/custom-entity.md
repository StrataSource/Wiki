---
title: Custom Entity
weight: 20
---

# Custom Entity

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

[Link to Original `sample-content` Example File](https://github.com/StrataSource/sample-content/blob/main/code/server/entity_remove.as)
