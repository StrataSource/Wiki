---
title: Creating an Addon 
---

# Creating an Addon 
## Overview
Portal 2: Community Edition's workshop functions different to Portal 2's; where Portal 2 only allows for singular maps, Portal 2: Community Edition's workshop works very similarly to Left 4 Dead's workshop, where you can upload entire `.vpk`s. These `.vpk`s can contain materials, models, vscripts, sounds, captions, and maps. This also eliminates the need to pack files into maps, as you can now include the assets in their original file paths.
## Organizing your files
The first step to creating an addon is getting your files organized. Addon folders can be located anywhere, but the best location is your base Portal 2: Community Edition folder. Your addon folder should be structured like a normal game folder (eg: `steamapps\common\Portal 2 Community Edition\addon_folder_name`, then your `materials`, `models`, etc. folders get put in `addon_folder_name`). Next, put all the files you want to include in the addon in their correct folders. 
## Uploading to the workshop
Now, you will upload your addon to the workshop. The process for this is somewhat similar to Portal 2, however some more steps are involved. To upload to the workshop, there are currently two tools: workshopcli and workshopgui. Addons use a special file named [`addon.kv3`](reference/workshop/addon_kv3) to manage all the information relating to the addon. You can imagine this file as the "`gameinfo.txt`" of your addon. This file is automatically created by the workshop uploader when you first upload the addon.

### Using workshopgui
In the `bin\win64` folder of the root install, towards the bottom of the lists you will find both workshop uploaders. Open the one labeled `workshopgui.exe`. After a short wait, a small window with a large button should appear in the center of your screen. Click on this button, and a file explorer window should appear. Navigate to your addon folder, select it, and click the "Select Folder" button. After a short wait, a notice saying that `addon.kv3` is missing, and that it will automatically create one for you; click ok to do this. The program will then freeze for about a minute, then open up your newly uploaded addon on your browser of choice. Don't worry, it's hidden, so nobody can see it!

### Using workshopcli 
Open a Command Prompt/Powershell session and `cd` to `path\to\steamapps\common\Portal 2 Community Edition`. Input the following command: 
```
.\bin\win64\workshopcli.exe -game p2ce mymod
``` 
`mymod` is the name of your addon folder, and is relative to your current `cd` location. If your mod folder is in the base `Portal 2 Community Edition` folder, then when running `workshopcli` from the root folder you would have to specify just the name of your addon folder. If you were running `workshopcli` from `Portal 2 Community Edition\bin\win64`, then you would instead specify `-game ..\..\p2ce ..\..\mymod`. You should get a message talking about a missing `addon.kv3`, let the program create one.

## Finalizing your Addon 
Now, edit your description and upload any screenshots you want. Now, copy your description and open up your addon folder. You should find a newly created `addon.kv3` file; open it and find the description parameter. Paste your description over the "Sample description" text to prevent having to retype your description after each update.

After this, subscribe to your addon and test it yourself on your machine (remember to move your original content you copied your assets from, so you are testing a base install of your addon. Any content in your custom folder will override your addon). After you find your addon satisfactory, go to your addon page and change the visibility to public. Congratulations! You have uploaded your first addon!

## Updating an Addon 
The process of updating an addon is very similar to uploading one. First, make changes or move the files you want to update into your addon folder. Then, before going any further, doublecheck the "id" and "description" parameters in your addon.kv3 file matches the ID in the URL of your addon and its description. If you upload an addon to the wrong ID, it will override the addon at that id with your addon. After making sure the IDs match, open your preferred workshop upload tool and open your addon folder. After a short delay, it should ask you what to put for the patch notes description; type what changes you made if you want — it's not required — and click ok. After a short wait, your workshop page should appear and your changes uploaded. Your addon is now updated!
