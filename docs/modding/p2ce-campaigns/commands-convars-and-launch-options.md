---
title: Useful Commands, Convars, and Launch Options
features:
    - USE_CAMPAIGNMANAGER
---

# Useful Commands

## `campaign_reload`

Reloads the campaign list. New & change campaign scripts should appear in the UI. If you are on the campaign selection screen, re-enter that screen to see the new/update campaign.

## `campaign_info`

Spews information about the current campaign into the console.

## `campaign_list`

Lists all campaigns detected by P2:CE to the console.

## `campaign_clear`

Clears the currently active campaign.

## `campaign_continue`

Continue a campaign from the latest save. Usage: `campaign_continue [campaign_id]`.

## `campaign_level_next`

Changes the map to the next level in the campaign, if it exists.

## `campaign_level_prev`

Changes the map to the previous level in the campaign, if it exists.

## `campaign_savedata_reset`

Wipes all save data relating to campaign progression. Does not delete saved game files.

## `campaign_savedata_show`

Display save data relating to campaign progression.

## `campaign_set_active`

Set a specified campaign as active. Usage: `campaign_set_active [campaign_id]`

## `campaign_start`

Starts a specified campaign at a certain chapter. Usage: `campaign_start [campaign_id] [chapter_index]`

## `startupmenu`

Enters the appropriate background map as detailed by the campaign script.

# Useful Cvars

## `campaign_debug`

If value is 1, prints additional debugging information to the console in relation to the campaign system.

## `campaign_default`

Sets the default campaign to boot into on startup. The background map will be entered automatically without intervention by a script.

# Useful Launch Options

## `-unlockchapters`

Treats all campaigns as completely unlocked for testing. This does not make any changes to the progression save. Must be used in conjunction with the `-dev` launch option.

## `-nochapterprogress`

Treats all campaigns as completely locked for testing. This does not make any changes to the progression save. Must be used in conjunction with the `-dev` launch option.