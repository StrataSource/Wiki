---
title: Technical Notes
features:
    - USE_CAMPAIGNMANAGER
---

# Technical Notes

> [!NOTE]
> This article includes technical notes, relevant to users developing sourcemods, with the intent of rolling their own UI script code.

# Reusing P2:CE's UI

P2:CE's UI code was designed to be initially reused by sourcemods in the event that you cannot or do not want to roll your own UI script code. If the `campaign_default` convar is specified in `cfg/cvar_defaults.cfg`, the game will enter the campaign menu and use it as the base menu, meaning that the player cannot exit to the P2:CE's default menu. It will work with the campaign system and you can focus your efforts elsewhere until you decide to write your own menus.

# Campaign Progression

Campaigns have their progression information saved inside `SAVE/campaign_save_data.kv3`. This file can be erased using the `campaign_savedata_reset` command. Campaign progression is currently tracked by chapter & map number.

# Meta Keys

The meta block found in the campaign script is a generic block internally. The engine does not define the fields that this Wiki documents. Instead, these keys are required by P2:CE's Panorama UI code.

In TypeScript, the meta block is represented as a `Map<string, string>`, and keys are retrieved using `meta.get('key')`. If you roll your own UI code with no intention of reusing P2:CE's scripts, **none** of the meta keys (and subsequently the art asset specifications) documented by the Wiki will apply to your code. You **MUST** reimplement these keys and use them where you see fit. However, this also means that if you have other use cases for your Sourcemod, you can add keys yourself!

> [!WARNING]
> Meta blocks cannot have blocks nested inside. Do not attempt to do so if you are implementing a custom menu script.

# Campaign Value Fixup

> [!NOTE]
> **This applies to all campaign script values, but predominantly the meta values.**

When requesting a value from the campaign system, be it a chapter title, map name, or meta value (e.g. author, chapter display mode), it will return *exactly* what is specified by the script. There is no fixup for any value by the engine internally (excluding sanitization).

For example, take the following campaign script snippet:
```
{
	campaigns = {
		"portal2_sp" = {
			title = "#MainMenu_Campaigns_portal2"
			meta = {
				author = "#MainMenu_Campaigns_Valve_Author"
				desc = "#MainMenu_Campaigns_portal2_Description"
				box_art = "{campaign_art}/portal2/boxart.png"
			}
		}
	}
}
```

The reference guide postulates that the `title` key will be localized if the value is a valid localization token. While this is true for P2:CE proper, **this is not the case for custom UI code.** P2:CE's UI code localizes the `title` value by itself, which is frontend functionality **and is not provided by the engine.** This means that if you were to write your own UI code and retrieve the `title` key, you would get `#MainMenu_Campaigns_portal2` returned to you, **not** the localized string. For any value that needs fixup, that functionality must be reimplemented by your sourcemod's UI code.

**This is especially important for any value that provides an image asset path.**

To reduce friction of creating campaign scripts, P2:CE's UI code will build asset paths for campaign authors. The UI code builds a path for an addon like this: `file://[addon path]/.assets/[asset value in script]` (except for movie assets). Like the example prior, if you write your own UI code, you will have to reimplement this functionality yourself to what you expect, or write paths in the campaign script values themselves.

Campaigns bundled with the game itself (and **not** as a local addon) will refer to asset paths using `{named_paths}`. The above snippet uses this for `box_art`. This is a shorthand for asset paths in Panorama and these named paths are defined in `panorama/panorama.cfg`.

# API Documentation

Full documentation of the Campaigns API and interfacing it with Panorama can be found in the Panorama Types repository, located [here](https://github.com/StrataSource/pano-typed).

# Campaign Bucketing

Internally, campaigns are organized via buckets, where a bucket denotes the source of the campaign. This helps avoid ID string conflicts. The `campaign_list` console command will display campaigns and their respective buckets.

The following buckets are used:

- `base`: This bucket represents campaigns found within the game's `script/campaigns.kv3` file, the folder in which `gameinfo.txt` resides.
- `addon:[ADDON_FOLDER]`: This bucket represents campaigns found within a local addon. A separate bucket is created for each local addon.
- `workshop:[WORKSHOP_ID]`: This bucket represents campaigns found within an addon from the Steam Workshop. A separate bucket is created for each Workshop addon.

When you reference an addon through an API, the ideal method is to make a full reference, created as: `[BUCKET_ID]/[CAMPAIGN_ID]`.

For example, for the Portal 1 campaign, which is a locally shipped addon: `addon:portal1_sp/portal1_sp`.

For a campaign shipped in the base game's files: `base/my_cool_campaign` *(This is probably what you will use a lot if you need to interface with the Campaigns API and you are rolling your own UI)*
