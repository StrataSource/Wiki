---
title: Sound System
---

# Sound System

Strata Source's sound system supports the following file formats:

* Microsoft WAV format 8-bit unsigned PCM
* Microsoft WAV format 16-bit signed PCM
* Microsoft WAV format ADPCM
* MP3
* OGG (Opus, Vorbis, Speex & PCM supported)
* FLAC

Support for MP3, OGG and FLAC files is provided by [libsndfile](https://libsndfile.github.io/libsndfile/).

Additionally, the following sample rates are supported:

* 11 kHz
* 22 kHz
* 44.1 kHz

Sound files which do not conform to these requirements may not play correctly or at all.

# Sound Scripts

Sound scripts in Strata are nearly identical to those found in other Source games. These are found in the `scripts/` directory, often named
in the format `game_sounds_xxx.txt`. The names of sound scripts to be loaded are defined in the manifest: `scripts/game_sounds_manifest.txt`,
which contains a list of sound script files to precache.

> [!P2CE]
> The game will also load any sound scripts placed in the `scripts/sounds/` directory.
> 
> It's recommended to place custom sound scripts here.

## Manifest

As previously described, `game_sounds_manifest.txt` defines which sound scripts are to be precached. This file is loaded only from the `MOD` search path.

> [!P2CE]
>
> The manifest also supports wildcards. i.e. `"precache_file" "scripts/sounds/*"`

## Sound Script Format

Sound script files contain multiple keyvalues objects describing sound parameters. The name of the keyvalues object determines how the sound 
can be referenced in-game. For example, `MySound.Test` will be referenced as `MySound.Test` in `ambient_generic`.

A complete description of the sound script format is as follows:

```
"MySound.Test"
{
    "soundentry_version"    "2" // Always set to 2!

    "channel"   "CHAN_AUTO"
    "volume"    "1.0"
    "pitch"     "100"
    "wave"      "mysound.wav"
    "distvariant"   "240,1320"
    "rndwave"
    {
        "wave"      "mysound.wav"
        // ...
    }
    "attenuation"   "ATTN_NONE"
    "play_to_owner_only"    "0"
    "delay_msec"    "0"
}

```

### `channel` (string)

This determines how the engine will allocate a channel to mix this sound.

The following are valid values:

* CHAN_AUTO
* CHAN_WEAPON
* CHAN_VOICE
* CHAN_ITEM
* CHAN_BODY
* CHAN_STREAM
* CHAN_STATIC

### `volume` (float or string)

`volume` determines how loud the sound is. 
This is either a floating point number in the range 0 to 1, or the string `VOL_NORM` representing a normal volume level.

### `pitch` (interval or string)

`pitch` determines if and how the engine should pitch adjust this sound.

Pitch can be an interval representing the min and max pitch of the sound, or a string representing a predefined pitch
setting. A pitch of `100` is considered normal and the engine will not modify the sound.

Valid predefined pitches are:
* PITCH_NORM    (pitch of 100)
* PITCH_LOW     (pitch of 95)
* PITCH_HIGH    (pitch of 120)

#### Examples

Pitched between 65% and 90% of normal:
```
"pitch"     "65,90"
```

Pitched at exactly 50% of normal:
```
"pitch"     "50"
```

Pitched at 95% (using PITCH_LOW):
```
"pitch"     "PITCH_LOW"
```

### `wave` (string)

`wave` specifies a single sound file to associate with this sound. They may be prefixed with a sound char, which controls
how the sound is spatialized.

### `soundlevel` (string)

`soundlevel` determines how far the sound can be heard from.

Valid values for this key include:
* SNDLVL_NONE
* SNDLVL_20dB
* SNDLVL_25dB
* SNDLVL_30dB
* SNDLVL_35dB
* SNDLVL_40dB
* SNDLVL_45dB
* SNDLVL_50dB
* SNDLVL_55dB
* SNDLVL_IDLE
* SNDLVL_TALKING
* SNDLVL_60dB
* SNDLVL_65dB
* SNDLVL_STATIC
* SNDLVL_70dB
* SNDLVL_NORM
* SNDLVL_75dB
* SNDLVL_80dB
* SNDLVL_85dB
* SNDLVL_90dB
* SNDLVL_95dB
* SNDLVL_100dB
* SNDLVL_105dB
* SNDLVL_110dB
* SNDLVL_120dB
* SNDLVL_130dB
* SNDLVL_GUNFIRE
* SNDLVL_140dB
* SNDLVL_150dB
* SNDLVL_180dB

### `distvar` (interval)

`distvar` gives more control over distance variant sounds. When a stereo wave file is marked with `CHAR_DISTVARIANT`,
the left channel represents the "close" sound, and the right channel represents the "far" sound. These channels are 
blended together between the near and far distances.

By default, `distvar` sounds have a transition start and end controlled with the `snd_dvar_dist_min` and `snd_dvar_dist_max`
cvar. If desired, this key may be used to specify a distance instead of relying on those cvars.

The value of this key is an interval in the format `near, far`, where near and far are measured in engine units.

**Warning:** You must specify `soundentry_version 2` for this parameter to work!

#### Examples

A sound that should start blending with far at 512 units, and transition to the far sound at 1024 units:
```
"distvar"       "512,1024"
```

A sound that should abruptly switch to the far channel at 120 units:
```
"distvar"       "120,120"
```

### `rndwave` (block)

`rndwave` contains a list of sound files that the engine will pick randomly to play. This block may contain up to
63 sounds.

#### Examples

Plays either test1.wav test2.wav or test3.wav
```
"rndwave"
{
    "wave"  "tests/test1.wav"
    "wave"  "tests/test2.wav"
    "wave"  "tests/test3.wav"
}
```

### `attenuation` (interval or string)

Defines sound attenuation. This is either an interval, or a string representing one of the predefined
attenuation values.

Setting this key will override `soundlevel`, if any was specified.

Valid predefined attenuation types:

* ATTN_NONE
* ATTN_NORM
* ATTN_IDLE
* ATTN_STATIC
* ATTN_RICOCHET
* ATTN_GUNFIRE

### `play_to_owner_only` (bool)

Determines if the sound should only be played to the owner.

### `delay_msec` (int)

Number of milliseconds the sound should be delayed until it starts playing.

### `soundentry_version` (int)

Determines the sound entry version. This should almost always be set to 2 for custom scripts.
When set to 1 or below, certain features may not work.

### `operator_stacks` (block)

A keyvalues block of operator stacks for this sound entry. See `sound_operator_stacks.txt` for an idea of how
these work.

