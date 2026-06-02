---
title: Constants
features:
    - USE_VSCRIPT
---

# Script Constants

## Collision Groups

These constants are used with the extended trace API to filter entities by their collision group.

| Name                                      | Value |
| ----------------------------------------- | ----- |
| `COLLISION_GROUP_NONE`                    | 0     |
| `COLLISION_GROUP_DEBRIS`                  | 1     |
| `COLLISION_GROUP_DEBRIS_TRIGGER`          | 2     |
| `COLLISION_GROUP_INTERACTIVE_DEBRIS`      | 3     |
| `COLLISION_GROUP_INTERACTIVE`             | 4     |
| `COLLISION_GROUP_PLAYER`                  | 5     |
| `COLLISION_GROUP_BREAKABLE_GLASS`         | 6     |
| `COLLISION_GROUP_VEHICLE`                 | 7     |
| `COLLISION_GROUP_PLAYER_MOVEMENT`         | 8     |
| `COLLISION_GROUP_NPC`                     | 9     |
| `COLLISION_GROUP_IN_VEHICLE`              | 10    |
| `COLLISION_GROUP_WEAPON`                  | 11    |
| `COLLISION_GROUP_VEHICLE_CLIP`            | 12    |
| `COLLISION_GROUP_PROJECTILE`              | 13    |
| `COLLISION_GROUP_DOOR_BLOCKER`            | 14    |
| `COLLISION_GROUP_PASSABLE_DOOR`           | 15    |
| `COLLISION_GROUP_DISSOLVING`              | 16    |
| `COLLISION_GROUP_PUSHAWAY`                | 17    |
| `COLLISION_GROUP_NPC_ACTOR`               | 18    |
| `COLLISION_GROUP_NPC_SCRIPTED`            | 19    |
| `COLLISION_GROUP_PZ_CLIP`                 | 20    |
| `COLLISION_GROUP_CAMERA_SOLID`            | 21    |
| `COLLISION_GROUP_PLACEMENT_SOLID`         | 22    |
| `COLLISION_GROUP_PLAYER_HELD`             | 23    |
| `COLLISION_GROUP_WEIGHTED_CUBE`           | 24    |
| `COLLISION_GROUP_DEBRIS_BLOCK_PROJECTILE` | 25    |

## Contents Flags

| Name                            | Value      | Definition                                           |
| ------------------------------- | ---------- | ---------------------------------------------------- |
| `CONTENTS_EMPTY`                | 0          | 0                                                    |
| `CONTENTS_SOLID`                | 1          | 0x1                                                  |
| `CONTENTS_WINDOW`               | 2          | 0x2                                                  |
| `CONTENTS_AUX`                  | 4          | 0x4                                                  |
| `CONTENTS_GRATE`                | 8          | 0x8                                                  |
| `CONTENTS_SLIME`                | 16         | 0x10                                                 |
| `CONTENTS_WATER`                | 32         | 0x20                                                 |
| `CONTENTS_BLOCKLOS`             | 64         | 0x40                                                 |
| `CONTENTS_OPAQUE`               | 128        | 0x80                                                 |
| `LAST_VISIBLE_CONTENTS`         | 128        | CONTENTS_OPAQUE                                      |
| `ALL_VISIBLE_CONTENTS`          | 255        | (LAST_VISIBLE_CONTENTS \| (LAST_VISIBLE_CONTENTS-1)) |
| `CONTENTS_TESTFOGVOLUME`        | 256        | 0x100                                                |
| `CONTENTS_SLIDE`                | 512        | 0x200                                                |
| `CONTENTS_BLOCKLIGHT`           | 1024       | 0x400                                                |
| `CONTENTS_TEAM1`                | 2048       | 0x800                                                |
| `CONTENTS_TEAM2`                | 4096       | 0x1000                                               |
| `CONTENTS_IGNORE_NODRAW_OPAQUE` | 8192       | 0x2000                                               |
| `CONTENTS_MOVEABLE`             | 16384      | 0x4000                                               |
| `CONTENTS_AREAPORTAL`           | 32768      | 0x8000                                               |
| `CONTENTS_PLAYERCLIP`           | 65536      | 0x10000                                              |
| `CONTENTS_MONSTERCLIP`          | 131072     | 0x20000                                              |
| `CONTENTS_BRUSH_PAINT`          | 262144     | 0x40000                                              |
| `CONTENTS_GRENADECLIP`          | 524288     | 0x80000                                              |
| `CONTENTS_DRONECLIP`            | 1048576    | 0x100000                                             |
| `CONTENTS_UNUSED3`              | 2097152    | 0x200000                                             |
| `CONTENTS_UNUSED4`              | 4194304    | 0x400000                                             |
| `CONTENTS_UNUSED5`              | 8388608    | 0x800000                                             |
| `CONTENTS_ORIGIN`               | 16777216   | 0x1000000                                            |
| `CONTENTS_MONSTER`              | 33554432   | 0x2000000                                            |
| `CONTENTS_DEBRIS`               | 67108864   | 0x4000000                                            |
| `CONTENTS_DETAIL`               | 134217728  | 0x8000000                                            |
| `CONTENTS_TRANSLUCENT`          | 268435456  | 0x10000000                                           |
| `CONTENTS_LADDER`               | 536870912  | 0x20000000                                           |
| `CONTENTS_HITBOX`               | 1073741824 | 0x40000000                                           |

## Trace Masks

Trace masks are used with the extended trace API to filter entities by category.

| Name                         | Value      | Definition                                                                                                             |
| ---------------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------- |
| `MASK_ALL`                   | -1         | 0xFFFFFFFF                                                                                                             |
| `MASK_SOLID`                 | 33570827   | (CONTENTS_SOLID \| CONTENTS_MOVEABLE \| CONTENTS_WINDOW \| CONTENTS_MONSTER \| CONTENTS_GRATE)                         |
| `MASK_PLAYERSOLID`           | 33636363   | (CONTENTS_SOLID \| CONTENTS_MOVEABLE \| CONTENTS_PLAYERCLIP \| CONTENTS_WINDOW \| CONTENTS_MONSTER \| CONTENTS_GRATE)  |
| `MASK_NPCSOLID`              | 33701899   | (CONTENTS_SOLID \| CONTENTS_MOVEABLE \| CONTENTS_MONSTERCLIP \| CONTENTS_WINDOW \| CONTENTS_MONSTER \| CONTENTS_GRATE) |
| `MASK_NPCFLUID`              | 33701891   | (CONTENTS_SOLID \| CONTENTS_MOVEABLE \| CONTENTS_MONSTERCLIP \| CONTENTS_WINDOW \| CONTENTS_MONSTER)                   |
| `MASK_WATER`                 | 16432      | (CONTENTS_WATER \| CONTENTS_MOVEABLE \| CONTENTS_SLIME)                                                                |
| `MASK_OPAQUE`                | 16513      | (CONTENTS_SOLID \| CONTENTS_MOVEABLE \| CONTENTS_OPAQUE)                                                               |
| `MASK_OPAQUE_AND_NPCS`       | 33570945   | (MASK_OPAQUE \| CONTENTS_MONSTER)                                                                                      |
| `MASK_BLOCKLOS`              | 16449      | (CONTENTS_SOLID \| CONTENTS_MOVEABLE \| CONTENTS_BLOCKLOS)                                                             |
| `MASK_BLOCKLOS_AND_NPCS`     | 33570881   | (MASK_BLOCKLOS \| CONTENTS_MONSTER)                                                                                    |
| `MASK_VISIBLE`               | 24705      | (MASK_OPAQUE \| CONTENTS_IGNORE_NODRAW_OPAQUE)                                                                         |
| `MASK_VISIBLE_AND_NPCS`      | 33579137   | (MASK_OPAQUE_AND_NPCS \| CONTENTS_IGNORE_NODRAW_OPAQUE)                                                                |
| `MASK_SHOT`                  | 1174421507 | (CONTENTS_SOLID \| CONTENTS_MOVEABLE \| CONTENTS_MONSTER \| CONTENTS_WINDOW \| CONTENTS_DEBRIS \| CONTENTS_HITBOX)     |
| `MASK_FLOORTRACE`            | 67125251   | (CONTENTS_SOLID \| CONTENTS_MOVEABLE \| CONTENTS_WINDOW \| CONTENTS_DEBRIS)                                            |
| `MASK_WEAPONCLIPPING`        | 100679683  | (CONTENTS_SOLID \| CONTENTS_MOVEABLE \| CONTENTS_MONSTER \| CONTENTS_WINDOW \| CONTENTS_DEBRIS)                        |
| `MASK_SHOT_BRUSHONLY`        | 67125251   | (CONTENTS_SOLID \| CONTENTS_MOVEABLE \| CONTENTS_WINDOW \| CONTENTS_DEBRIS)                                            |
| `MASK_SHOT_HULL`             | 100679691  | (CONTENTS_SOLID \| CONTENTS_MOVEABLE \| CONTENTS_MONSTER \| CONTENTS_WINDOW \| CONTENTS_DEBRIS \| CONTENTS_GRATE)      |
| `MASK_SHOT_PORTAL`           | 33570819   | (CONTENTS_SOLID \| CONTENTS_MOVEABLE \| CONTENTS_WINDOW \| CONTENTS_MONSTER)                                           |
| `MASK_SOLID_BRUSHONLY`       | 16395      | (CONTENTS_SOLID \| CONTENTS_MOVEABLE \| CONTENTS_WINDOW \| CONTENTS_GRATE)                                             |
| `MASK_PLAYERSOLID_BRUSHONLY` | 81931      | (CONTENTS_SOLID \| CONTENTS_MOVEABLE \| CONTENTS_WINDOW \| CONTENTS_PLAYERCLIP \| CONTENTS_GRATE)                      |
| `MASK_NPCSOLID_BRUSHONLY`    | 147467     | (CONTENTS_SOLID \| CONTENTS_MOVEABLE \| CONTENTS_WINDOW \| CONTENTS_MONSTERCLIP \| CONTENTS_GRATE)                     |
| `MASK_NPCWORLDSTATIC`        | 131083     | (CONTENTS_SOLID \| CONTENTS_WINDOW \| CONTENTS_MONSTERCLIP \| CONTENTS_GRATE)                                          |
| `MASK_NPCWORLDSTATIC_FLUID`  | 131075     | (CONTENTS_SOLID \| CONTENTS_WINDOW \| CONTENTS_MONSTERCLIP)                                                            |
| `MASK_SPLITAREAPORTAL`       | 48         | (CONTENTS_WATER \| CONTENTS_SLIME)                                                                                     |
| `MASK_DEADSOLID`             | 65547      | (CONTENTS_SOLID \| CONTENTS_PLAYERCLIP \| CONTENTS_WINDOW \| CONTENTS_GRATE)                                           |

## Button Flags

| Name             | Value     | Definition |
| ---------------- | --------- | ---------- |
| `IN_ATTACK`      | 1         | 0x1        |
| `IN_JUMP`        | 2         | 0x2        |
| `IN_DUCK`        | 4         | 0x4        |
| `IN_FORWARD`     | 8         | 0x8        |
| `IN_BACK`        | 16        | 0x10       |
| `IN_USE`         | 32        | 0x20       |
| `IN_CANCEL`      | 64        | 0x40       |
| `IN_LEFT`        | 128       | 0x80       |
| `IN_RIGHT`       | 256       | 0x100      |
| `IN_MOVELEFT`    | 512       | 0x200      |
| `IN_MOVERIGHT`   | 1024      | 0x400      |
| `IN_ATTACK2`     | 2048      | 0x800      |
| `IN_RUN`         | 4096      | 0x1000     |
| `IN_RELOAD`      | 8192      | 0x2000     |
| `IN_ALT1`        | 16384     | 0x4000     |
| `IN_ALT2`        | 32768     | 0x8000     |
| `IN_SCORE`       | 65536     | 0x10000    |
| `IN_SPEED`       | 131072    | 0x20000    |
| `IN_WALK`        | 262144    | 0x40000    |
| `IN_ZOOM`        | 524288    | 0x80000    |
| `IN_WEAPON1`     | 1048576   | 0x100000   |
| `IN_WEAPON2`     | 2097152   | 0x200000   |
| `IN_GRENADE1`    | 8388608   | 0x800000   |
| `IN_GRENADE2`    | 16777216  | 0x1000000  |
| `IN_LOOKSPIN`    | 33554432  | 0x2000000  |
| `IN_USEORRELOAD` | 67108864  | 0x4000000  |
| `IN_COOP_PING`   | 134217728 | 0x8000000  |
| `IN_REMOTE_VIEW` | 268435456 | 0x10000000 |

## MoveType

| Name                  | Value |
| --------------------- | ----- |
| `MOVETYPE_NONE`       | 0     |
| `MOVETYPE_ISOMETRIC`  | 1     |
| `MOVETYPE_WALK`       | 2     |
| `MOVETYPE_STEP`       | 3     |
| `MOVETYPE_FLY`        | 4     |
| `MOVETYPE_FLYGRAVITY` | 5     |
| `MOVETYPE_VPHYSICS`   | 6     |
| `MOVETYPE_PUSH`       | 7     |
| `MOVETYPE_NOCLIP`     | 8     |
| `MOVETYPE_LADDER`     | 9     |
| `MOVETYPE_OBSERVER`   | 10    |
| `MOVETYPE_CUSTOM`     | 11    |

## MoveCollide

| Name                     | Value |
| ------------------------ | ----- |
| `MOVECOLLIDE_DEFAULT`    | 0     |
| `MOVECOLLIDE_FLY_BOUNCE` | 1     |
| `MOVECOLLIDE_FLY_CUSTOM` | 2     |
| `MOVECOLLIDE_FLY_SLIDE`  | 3     |


## Paint Types

| Name            | Value |
| --------------- | ----- |
| `BOUNCE_POWER`  | 0     |
| `REFLECT_POWER` | 1     |
| `SPEED_POWER`   | 2     |
| `PORTAL_POWER`  | 3     |
| `NO_POWER`      | 4     |
| `STICK_POWER`   | 5     |

## Cube Shape

Cube shape is used by the Shape/Behavior system for weighted cubes. A cube's shape indicates which buttons it can press. Note that other values are permitted for custom cubes.

| Name                   | Value |
| ---------------------- | ----- |
| `CUBE_SHAPE_CUBIC`     | 1     |
| `CUBE_SHAPE_SPHERICAL` | 2     |

## Cube Behavior

Cube behavior is used by the Shape/Behavior system for weighted cubes. A cube's behavior indicates the functionality of the cube.

| Name                        | Value |
| --------------------------- | ----- |
| `CUBE_BEHAVIOR_REGULAR`     | 1     |
| `CUBE_BEHAVIOR_REFLECTIVE`  | 2     |
| `CUBE_BEHAVIOR_SCHRODINGER` | 3     |

## Surface Type Flags

| Name                | Value  | Definition    |
| ------------------- | -------| ------------- |
| `SURF_LIGHT`        | 1      | 0x1           |
| `SURF_SKY2D`        | 2      | 0x2           |
| `SURF_SKY`          | 4      | 0x4           |
| `SURF_WARP`         | 8      | 0x8           |
| `SURF_TRANS`        | 16     | 0x10          |
| `SURF_NOPORTAL`     | 32     | 0x20          |
| `SURF_TRIGGER`      | 64     | 0x40          |
| `SURF_NODRAW`       | 128    | 0x80          |
| `SURF_HINT`         | 256    | 0x100         |
| `SURF_SKIP`         | 512    | 0x200         |
| `SURF_NOLIGHT`      | 1024   | 0x400         |
| `SURF_BUMPLIGHT`    | 2048   | 0x800         |
| `SURF_NOSHADOWS`    | 4096   | 0x1000        |
| `SURF_NODECALS`     | 8192   | 0x2000        |
| `SURF_NOPAINT`      | 8192   | SURF_NODECALS |
| `SURF_NOCHOP`       | 16384  | 0x4000        |
| `SURF_HITBOX`       | 32768  | 0x8000        |
| `SURF_SKYNOEMIT`    | 65536  | 0x10000       |
| `SURF_SKYOCCLUSION` | 131072 | 0x20000       |
| `SURF_SLICK`        | 262144 | 0x40000       |

## Misc. Constants

| Name          | Value      |
| ------------- | ---------- |
| `RAND_MAX`    | 2147483647 |
| `PI`          | 3.14159    |
| `_charsize_`  | 1          |
| `_floatsize_` | 8          |
| `_intsize_`   | 8          |
