# Using Panorama

As of Momentum Mod 0.8.8 and Portal 2: Community Edition 0.5.6, both games ship with Panorama installed. 

To use Panorama, you must launch the game *without* the `-legacyui` option. Both P2CE and Momentum have launch options specifically for Panorama,
so steam should ask you when you're trying to launch the game. 

## Tinkering with Panorama

To modify Panorama UI files, you must first extract the `<game>/panorama/code.pbin` file into `<game/panorama/`, but make sure to 
*not* remove code.pbin, as panorama will not load without it. `code.pbin` itself is just a signed ZIP file, so you can just open it 
with a program like WinRAR or use a command line utility, such as `unzip`, to extract it.

By default, Panorama will not load loose files on the filesystem unless it's launched with `-dev`, so if you're trying to modify
Panorama files, make sure to launch with `-dev`. 

Panorama layouts are just XML files and they're combined with Javascript and CSS scripts. 
Currently we support ES6 Javascript in panorama.

### Reloading the UI 

Layouts and scripts can be reloaded by pressing `F8`
