---
title: addon.kv3
---
# addon.kv3
Addons use a special file called `addon.kv3`, which defines various parts of the addon. The [workshop tools](p2ce/reference/workshop/addoncreation#uploading-to-the-workshop) automatically generate this but it can be manually edited after initial creation.

*(NOTE: As workshop support gets updated and expanded, all these parameters should become functional. As of now, many parameters may be broken or non-functional. If you have any suggestions or feature requests, please create an issue on [the P2CE repo](https://github.com/StrataSource/Portal-2-Community-Edition/issues).)*
## Parameters

| Parameter name | Parameter description | Detault | Example |
| --- | --- | --- | --- |
| mod | Name of the addon | N/A | "Cool Name Mappack" |
| description | Description to put on the workshop page | "Sample Description" | "This is a really cool mappack with a really cool name!" |
| type | Type of addon this is | map | "mappack" |
| id | Workshop item ID. This is automatically generated on the creation of the file. This can be found by examining the URL of your addon | N/A | "3092835977" |
| authors | List of authors. Steam automatically adds the creator, so do not add your username. | [ ] | [ "Strata Source" ] |
| instance_paths | Paths to instances, default includes the root.| [ ] | [ "${root}/sdk_content/instances" ]
| dependencies | Dependencies, either games or workshop items | [ ] | [ "workshop:123456", "game:440" ] |
| gamedata | Same as GameData in `gameinfo.txt`, but as an array. | [ ] | [ "${game:440}/bin/tf.fgd" ] |
| tags | Workshop tags | [ ] | [ "realism", "graphics" ] |
| ignore | Files or folders to ignore | [ ] | [ ".gitignore" ]
| metadata | "Arbitrary info that may be attached to this addon. Can be read via API" | [ ] | N/A |
