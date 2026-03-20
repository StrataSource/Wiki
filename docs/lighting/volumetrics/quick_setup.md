---
title: Quick Setup
weight: 20
features:
    - USE_CLUSTERED
---

# Quick Setup

## How to make it work for Clustered entities

You can set up volumetrics in 3 different ways: 
1. By using the corresponding KeyValues in `light_rt`, `light_rt_spot` and `env_projectedtexture`;
2. By using `obb_fogvolume` that defines volumetric rays specifically for the fog volume it produces;
3. Through the [Clustered Volumetric Inspector](/misc/devui/graphics) in the Developer UI menu.

### Using KeyValues

**Light_rt and light_rt_spot**
1. Click on your light_rt.
2. change "volumetric Density" to a value above(e.g 0.1)
3. Now your volumetric should work
> [!NOTE]
> If you want occlude effect, in the flag tabs by default "Shadowed" is disabled, you need to click on it for enabled it.

![light_rt KV](images/light_rt_kv.png)

[should we put "NOTICE" here ? like [note, tip etc]]

Red meaning you need to enable it and configure to make it work

Blue meaning not obligatory to have it but necessary for having ocluding effect

**env_projectexture**
[should we put "NOTICE" here ? like [note, tip etc]]
env_projectexture are temporary and will be changed
 
1. Click on your env_projectexture
2. On the KeyValue "Enable Volumetrics" make it to Yes
3. Now your volumetric should work

### Using `obb_fogvolume`

1. Create an entity call obb_fogvolume
2. Configure it.
3. it's should work

### Using Clustered Volumetric Inspector

> [!TIP]
> Position bars are scrollable!
[volumetric lighting]

![Clustered Volumetric Inspector](images/clustered_light_inspector_volumetric.jpg)

You can Configure and change the volumetric Lighting settings on the maps.

You can change to disable and enable it. You can also change the Volumetric density and the light scale.

[Volumetric fog]

1. You can enable the Clustered Volumetrics Inspector UI using the  ```devui_show light_editor``` console command.
entity. :
1.You can change the obb_volumefog parameters on map that are already set.
[should we put "NOTICE" here ? like [note, tip etc]]
> useful for here for changing parameter on your entity and replicate it on hammer 

Fog value globally:
You can have a volumetric fog across the entire map, practical when global fog is implemented, This also Interact with Env_cascade_light

![Clustered Volumetric Inspector](images/fog_inspector.png)

## How to make it work for Cascade Shadow Mapping

Currently, there are not KeyValues to enable volumetrics in `env_cascade_light` entity. However, there are two ways to make them appear - by using `obb_fogvolume` entity, or through the [Clustered Volumetric Inspector](/misc/devui/graphics).

![Volumetric effect of the Cascade Shadow Mapping](images/obb_volumefog_csm_interact_workaround.jpg)

****

# Troubleshooting

## The volumetrics don't show up!

Skill issue.

## The volumetrics are too intense!

Same issue.

## My Volumetrics are broken and corrupt!

We FUCKED all the AMD GPUs in the ASS! Go buy an nvidia, we don't care.

## How do I get to use it? I don't have P2CE

Dude... ugh. Just shut up. Open beta in 2 months.
