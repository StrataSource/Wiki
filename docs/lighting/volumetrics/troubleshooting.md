---
title: Troubleshooting
weight: 30
features:
    - USE_CLUSTERED
---

# Troubleshooting

This is a list of currently known issues and some troubleshooting tips for any issues with volumetric lighting.

### "The volumetrics don't show up!"

* Make sure you have `Volumetric Light Mode` set to `Dynamic Only` or `Enable Volumetrics` enabled.
* Make sure `Volumetric Density` or `Volumetric Intensity`is not 0.
* Make sure the light is actually working and/or visible.

### "The volumetrics are too intense!"

* Seems like the `Volumetric Density` KeyValue is set too high. The value of 1.0 makes the volumetric ray completely opaque, so make sure it is set to something around 0.1 for more realistic results.

### "The volumetrics for a light source are everywhere, even behind walls!"

* Volumetric lighting is shadow dependant, you need to make sure the `Shadowed` flag is checked when making shadowed volumetrics. If the flag is enabled but volumetrics are still leaking, then you might have too many dynamic shadows updating at once. See [clustered troubleshooting page](/lighting/clustered/troubleshooting) for more information related to the issue.

### "My volumetrics are broken and corrupt!"

* Certain AMD GPU models are known to have trouble running the clustered renderer, and since volumetrics are shadow dependant, this issue relates to them as well. **If you experience this, let us know what GPU brand/model, operating system and other hardware specs you're using.** Clustered lights may also act weird when running the game on Linux under DXVK, however the circumstances in which they break should not be possible in production.

## If you have any issues that are not addressed in this article, make sure to report it to us on the [Strata issue tracker.](https://github.com/StrataSource/Engine/issues)
