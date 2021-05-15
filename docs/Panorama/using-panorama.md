---
layout: default
title: Using Panorama
parent: Panorama
nav_order: 1
---

# Using Panorama

As of Momentum Mod 0.8.8 and Portal 2: Community Edition 0.5.6, both games ship with Panorama installed. 

To use Panorama, you must launch the game *without* the `-legacyui` option. Both P2CE and Momentum have launch options specifically for Panorama,
so steam should ask you when you're trying to launch the game. 

## Tinkering with Panorama

To modify Panorama UI files, you must first extract `<game>/panorama/code.pbin` into `<game>/panorama`. 
`code.pbin` is just a signed zip file, so you should be able to open it with a utility such as WinRAR or Ark. 
For Panorama to load the extracted files off the disk instead of from `code.pbin`, the game needs to be 
run with `-dev`. 

Keep in mind that `code.pbin` is signed and must exist for the game to start with Panorama.


### Reloading Your Changes

Layouts and scripts can be reloaded by pressing `F8` while on a panel.

Panels that use the global v8 context need special care taken when writing scripts.
Defining named types, such as classes or functions, should be completely avoided since in global contexts,
scripts aren't reloaded, but rather re-executed in the same environment. The main menu's script is a 
good example of a "global context safe" script.

## Panorama Debugger

The panorama debugger can be enabled by entering `panorama_debugger_toggle` in console. The debugger is only 
supported on Windows, and a Linux port is unlikely for now. 