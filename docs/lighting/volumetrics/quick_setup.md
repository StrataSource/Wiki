---
title: Quick Setup
weight: 20
features:
    - USE_CLUSTERED
---

# Quick Setup

You can set up volumetrics in 3 different ways: 
1. By using the corresponding KeyValues in `light_rt`, `light_rt_spot` and `env_projectedtexture`;
2. By using `obb_fogvolume` that defines volumetric rays specifically for the fog volume it produces;
3. Through the [Clustered Volumetric Inspector](/misc/devui/graphics) in the Developer UI menu.

### Using KeyValues:

**For Light_rt and light_rt_spot**
1. Add a light_rt or light_rt_spot entity
2. Set the "Volumetric Light Scale" KeyValue to some value between 0.1 and 1.0
3. Set the "Volumetric Density" KeyValue to some value between 0.1 and 1.0
4. Make sure the "Shadowed" flag is **checked**
5. Compile the map. The volumetrics should appear.

> [!NOTE]
> It is *not* necessary to have the "Shadowed" flag enabled for the volumetrics to appear.

![light_rt KV](images/light_rt_kv.png)

**For env_projectexture**
 
1. Add an env_projectexture entity
2. Set the "Enable Volumetrics" KeyValue to Yes
3. Set the "Volumetric Intensity" KeyValue to some value between 0.1 and 1.0
4. Compile the map. The volumetrics should appear.

> PHOTO FOR env_projectedtexture

### Using `obb_fogvolume`:

1. Add an obb_fogvolume entity
2. Set the KeyValue to some value
3. Set the KeyValue to some value
3. Set the KeyValue to some value
3. Set the KeyValue to some value
3. Set the KeyValue to some value
3. Set the KeyValue to some value
3. Set the KeyValue to some value
3. Set the KeyValue to some value
3. Set the KeyValue to some value
4. Compile the map. The volumetric cloud should appear

> PHOTO FOR obb_fogvolume

### Using Clustered Volumetric Inspector:

You can configure and change the volumetric Lighting settings on the maps. 
You can disable and enable it. 
You can also change the Volumetric density and the light scale.

![Clustered Volumetric Inspector](images/clustered_light_inspector_volumetric.jpg)

# How to make it work for Cascade Shadow Mapping

Currently, there are no KeyValues to enable volumetrics in `env_cascade_light` entity. However, there are two ways to make them appear - by using `obb_fogvolume` entity, or through the [Clustered Volumetric Inspector](/misc/devui/graphics).

![Volumetric effect of the Cascade Shadow Mapping](images/obb_volumefog_csm_interact_workaround.jpg)
