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

1. Do this
2. Then do this
3. And here it should be done

PHOTO

### Using `obb_fogvolume`

1. Do this
2. Then do this
3. And here it should be done

### Using Clustered Volumetric Inspector

1. Do this
2. Then this
3. And done

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
