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

There are 3 KeyValues in `light_rt` and `light_rt_spot` entities: `Volumetric Light Mode` **`Volumetric Density`** and **`Volumetric Light Scale`**. `Volumetric Light Mode` toggles the volumetric lighting for this entity, can be set to either *None* or *Dynamic Only*. `Volumetric density` is a floating number between 0 and 1, where 1 is fully opaque and 0 is completely invisible. `Volumetric Light Scale` is a floating number that scales the color of the volumetric lighting casted by this entity, it is not recommended to set higher than 1, even though the number can go up infinitely.

`env_projectexture`, except for `Enable Volumetrics`, have only volumetric-related KeyValue - `Volumetric Intensity`, which is identical to `Volumetric Density`. But unlike all the other entities that produce volumetrics, projected texture volumetrics work with WebM videos.

PHOTO

### Using `obb_fogvolume`

**StudioMDL, you need to literally tell how to do that. [As example, use this.](/lighting/clustered/quick_start)**

PHOTO

### Using Clustered Volumetric Inspector

[Clustered Volumetric Inspector](/misc/devui/graphics).

PHOTO

## How to make it work for Cascade Shadow Mapping

Currently, there are not KeyValues to enable volumetrics in `env_cascade_light` entity. However, there are two ways to make them appear - by using `obb_fogvolume` entity, or through the [Clustered Volumetric Inspector](/misc/devui/graphics).

PHOTO

****

# Troubleshooting

## The volumetrics don't show up!

Skill issue.

## The volumetrics are too intense!

Same issue.

## How do I get to use it? I don't have P2CE

Dude... ugh. Just shut up. Open beta in 2 months.
