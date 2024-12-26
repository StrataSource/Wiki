---
title: Sound System
weight: 0
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
