---
title: "Introducing Volumetrics"
weight: 10
features:
    - USE_CLUSTERED
---

> [!NOTE]
> This page is work in progress. Please be patient!
> TODO fill me.

# Volumetric Lighting

Volumetric Lighting is ... 
It allows light to ...

![Volumetrics](images/basic_volumetric.gif)

Player model also interacts with volumetric lighting, even in the firstperson.

![Volumetrical Player Shadow](images/vol_playershadow.png)

## Light Cookies and WebM support

Volumetrics support light cookies from `light_rt` and `light_rt_spot`, as well as WebM videos from `env_projectedtexture` entity. The volumetrics casted by the lights that use light cookies and WebM videos will update and show up correctly.

![WebM Volumetrics](images/ptex_vol.gif)

****

## Volumetrical Fog

Explanation about `obb_fogvolume` entity.

PHOTO

## Setup for Global Volumetrical Fog

You can configure the global volumetrical fog in the Clustered Volumetric Inspector.

![Clustered Volumetric Inspector](images/fog_inspector.png)
