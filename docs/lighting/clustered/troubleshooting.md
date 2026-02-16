---
title: "Known Issues"
weight: 40
features:
    - USE_CLUSTERED
---

# Troubleshooting and Known Issues

This is a list of currently known issues and some troubleshooting tips for any issues with clustered lighting.

### "My lights don't have shadows" / "My lights are shining through walls"

* For cheap static shadows, make sure "Direct light mode" is set to "Static Only" for your light entity. With this option, specular lighting will still travel through walls. If that's an issue for your map, you may need to use dynamic shadows or turn off specular.
* For dynamic shadows, make sure the "Shadowed" spawn flag is enabled on the light that should be casting shadows.

### "I set the Shadowed spawn flag, but there are still no shadows / light leaks through walls"

* You have too many dynamic shadows updating at once. Remember that **each shadow size level increases the shadow atlas size by a factor of 4**, and **the shadow atlas cannot have exceed a value of 7**, so if there are for example 2 `light_rt`s with shadow size of 6 close to each other, they will overlap and therefore will not produce any shadows. However, there is an unstable workaround, where by enabling `light_rt`s one by one they have a chance to keep their shadows.

### "My dynamic shadows are blurry"

* Set the "Initial Shadow Size" keyvalue of your light to something around 6. Remember that the higher the shadow size, the bigger piece of shadow atlas it will take.

### "My dynamic shadows are 'frozen' or don't update" / "Some entities like rockets don't cast shadows"

* Shadows are updated when entities move near the light source. Some entities aren't hooked up properly, this is a known issue. Most entities should be fixed (prop_dynamic, prop_physics), but if you find any entity that does not update shadows, make sure to let us know on the Strata issue tracker.

### "My dynamic shadows update in low fps"

* There is a cap on how many faces can get their shadows updated, and this cap is called the **shadow frame budget**. This is an optimization technique that prevents the game from lagging on low-end devices. You can increase the budget by using the `r_clustered_shadowframebudget` console command. Note that this will significantly lower your fps when used carelessly.

### "Shadows glitch or flicker when a light is moving"

* Clustered shadows update less frequently than the game itself, so if a moving clustered light entity cannot keep up updating the shadowmap, the shadows from that entity will flicker. This often happens in heavy maps with a lot of clustered lights, and rarely if the light peaks from a corner, especially when lighting up a huge area. There is no workaround other than not moving clustered lights too fast and using dynamic shadows only where necessary.

### "Everything is completely broken/corrupted and I can't fix it"

* Certain GPU models may have trouble running the clustered renderer. **If you experience this, let us know what GPU brand/model, operating system and other hardware specs you're using.** Clustered lights may act weird when running the game on Linux under DXVK on AMD platforms. However, the circumstances in which they break should not be possible in production.

## If you have any issues that are not addressed in this article, make sure to report it to us on the [Strata issue tracker.](https://github.com/StrataSource/Engine/issues)
