---
title: "Troubleshooting and Known Issues"
features:
    - USE_CLUSTERED
---
# Troubleshooting and Known Issues

This is a list of currently known issues and some troubleshooting tips for any issues with clustered lighting.

**"Everything is completely broken/corrupted"**

* Certain GPU models may have trouble running the clustered renderer. **If you experience this, let us know what GPU brand/model, operating system and other hardware specs you're using.** Usually this issue has been observed when running the game on Linux under DXVK on AMD platforms. However, the circumstances in which this has been observed should not be possible in production.

**"My lights don't have shadows" / "My lights are shining through walls"**

* For cheap static shadows, make sure you are using baked direct lighting for static shadows, (Light mode "specular" or "static.") With this option, specular lighting will still travel through walls. If that's an issue for your map, you may need to use dynamic shadows or turn off specular.
* For dynamic shadows, make sure the "Shadowed" spawn flag is set on the light that should be casting shadows.

**"I set the Shadowed spawn flag, but there are still no shadows/light leaks through walls"**

* You may have too many dynamic shadows updating at once. This is a known issue without a current workaround. Let us know if you find one!

**"My dynamic shadows are blurry"**

* Set the "Initial Shadow Size" key on your light to something around 7, or higher if you really need it.

**"My dynamic shadows are 'frozen' or don't update" / "Some entities like rockets don't cast shadows"**

* Shadows are updated when entities move near the light source. Some entities aren't hooked up properly, this is a known issue. Most entities should be fixed (prop_dynamic, prop_physics), but if you find any entity that does not update shadows, make sure to let us know on the [Strata issue tracker](https://github.com/StrataSource/Engine/issues).

**"Shadows glitch or flicker when a light is moving"**

* This is a known issue without a current workaround. Let us know if you find one!

**"I see light coming from light sources that aren't in the current PVS"**

* This is a known issue without a current workaround. Let us know if you find one!

If you have any issues that are not addressed in this article, make sure to report it to us on the [Strata issue tracker](https://github.com/StrataSource/Engine/issues).
