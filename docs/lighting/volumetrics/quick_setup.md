---
title: Quick Setup
weight: 20
features:
    - USE_CLUSTERED
---

# Quick Setup

## How do I make it work for Clustered entities?

For Setup Volumetric 

light_rt and light_rt_spot

you need to enable the KV Volumetric density by default it's on "0" change it and make it to the values you need it.
By default volumetric light scale are on the value "1" and by default volumetric light mode are on dynamic Only
After you change Volumetric density, Volumetric should work but you will probably don't have the occlusion effets, you need to enable "Shadowed" in the flags

Env_projectextures

[!NOTE]
The KV on env_projectextures are based on the old volumetric implementation based on the SFM, this one will change to fit the light_rt and light_rt_spot KV

Photo showing how it's done.

## How do I make it work for Cascade Shadow Mapping?

Explanation (there is no way except for the devui menu lmao, link it)

A pic showing how it's done

## How do I make it work for Cascade Shadow Mapping?

it's plan  density contribution to the csm light, but at the time being there is a 

workaround : obb_volumefog interact with CSM 

# Troubleshooting

## The volumetrics don't show up!

Skill issue.

## The volumetrics are too intense!

Same issue, lower the values.

## How do I get to use it? I don't have P2CE

Dude... ugh. Just shut up. Open beta is in 2 months.
