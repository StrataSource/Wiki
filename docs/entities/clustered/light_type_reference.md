---
title: "Light Type Reference"
features:
    - USE_CLUSTERED
---
# Light Type Reference

This is a reference page for the 4 light types.

## Static

This light type is mainly used for lights that cast baked direct and indirect light, with no need for dynamic shadows nor any specular lighting. The Shadowed spawnflag is non-functional with this light type.

These lights are the same as standard Source Engine lights.

| Direct | Indirect | Specular     |
| ------ | -------- | ------------ |
| baked  | baked    | *disabled* |

* Top: 3 Static-type lights, shadowed flag unchecked
* Bottom: 3 Static-type lights, shadowed flag checked. Note the lack of shadows on the walls.

![static unshadowed](images\unshadowed_static.jpg)

![static shadowed](images\shadowed_static.jpg)

For most use cases, Specular lights should be used, as the specular reflections properly use the metallic channel of PBR materials.

## Specular

This light type has baked direct and indirect lighting like the Static light type, except that it also includes dynamic Specular lighting.

Shadows can be enabled on this light type using the "Shadowed" spawnflag, however the shadows will be fainter than those of Static Bounce or Fully Dynamic. 

> [!WARNING]
> Specular highlights will travel through walls if the Shadowed spawnflag is not checked. If this will cause issues with your map, use the Static light type instead.

| Direct | Indirect | Specular          |
| ------ | -------- | ----------------- |
| baked  | baked    | **dynamic** |

* Top: 3 Specular-type lights, shadowed flag unchecked
* Bottom: 3 Specular-type lights, shadowed flag checked.

![specular unshadowed](images\unshadowed_specular.jpg)

![specular shadowed](images\shadowed_specular.jpg)

## Static Bounce

This light type casts static bounced lighting and dynamic direct lighting. Unlike the previous light types, direct lighting is dynamically generated, and therefore will shine through walls if the Shadowed spawnflag is unchecked.

| Direct            | Indirect | Specular          |
| ----------------- | -------- | ----------------- |
| **dynamic** | baked    | **dynamic** |

* Top: 3 Static Boucne-type lights, shadowed flag unchecked
* Bottom: 3 Static Bounce-type lights, shadowed flag checked.

![Static Bounce unshadowed](images\unshadowed_staticb.jpg)

![Static Bounce shadowed](images\shadowed_staticb.jpg)

This light is best used for static sources of light that need to cast dynamic shadows, such as observation rooms in Portal 2.

## Fully Dynamic

This light type casts dynamic direct lighting and specular highlights, without any indirect lighting generated.

| Direct            | Indirect     | Specular          |
| ----------------- | ------------ | ----------------- |
| **dynamic** | *disabled* | **dynamic** |

* Top: 3 Dynamic-type lights, shadowed flag unchecked. Note how the light bleeds through the window frame on to the floor outside the room.
* Bottom: 3 Dynamic-type lights, shadowed flag checked.

![specular unshadowed](images\unshadowed_dynamic.jpg)

![specular shadowed](images\shadowed_dynamic.jpg)

This light is best used for moving light sources, where prebaked bounce lighting will look out of place when the light source has moved, such as swinging ceiling lights or a movable desk lamp.
