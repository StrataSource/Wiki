---
title: "Light Cookies"
weight: 40
features:
    - USE_CLUSTERED
---

# Light Cookies

Light cookies, also known as cookie textures, are supported by clustered lights (`light_rt` and `light_rt_spot`). They can be used to apply a pattern to a light, controlling its shape and brightness. If you're not familiar with the concept of light cookies, imagine them like putting a piece of paper over a flashlight. If you were to cut out a shape from the paper, it would allow light to pass through, projecting a specific shape. Light cookies also have a similar effect to projected textures (`env_projectedtexture`).

In Hammer, light cookies can be added to a light using the "Cookie Texture Name" and "Cookie Texture Frame" properties. When looking at lights through the Light Inspector, the texture can be set under "Pattern".

Volumetric lighting also works with light cookies.

![Volumetrics & light cookies](images/volumetrics.png)

## How to use

Light cookies are grayscale textures that imitate shadows, and setting up cookie textures is as easy as setting up a texture for `env_projectedtexture` in vanilla Portal 2.

#### Preparing the image

explanation

> image showing the preps

#### Converting to VTF format

explanation

> image showing the convertion

#### Inserting into a clustered light

explanation

> [!NOTE]
> TODO: in this note, mention if .vtf extention is needed

> image showing the KV

## Where to find cookies

Officially, there are no pre-made cookies.

On the workshop, there is an [addon](https://steamcommunity.com/sharedfiles/filedetails/?id=3753568885) that includes ~150 ready-to-use light cookies made by Kenney.NL and ported to VTF by Mae.

> image showing the addon
