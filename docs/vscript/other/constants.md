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
| `COLLISION_GROUP_BREAKABLE_GLASS`         | 6     |
| `COLLISION_GROUP_CAMERA_SOLID`            | 21    |
| `COLLISION_GROUP_DEBRIS`                  | 1     |
| `COLLISION_GROUP_DEBRIS_BLOCK_PROJECTILE` | 25    |
| `COLLISION_GROUP_DEBRIS_TRIGGER`          | 2     |
| `COLLISION_GROUP_DISSOLVING`              | 16    |
| `COLLISION_GROUP_DOOR_BLOCKER`            | 14    |
| `COLLISION_GROUP_INTERACTIVE`             | 4     |
| `COLLISION_GROUP_INTERACTIVE_DEBRIS`      | 3     |
| `COLLISION_GROUP_IN_VEHICLE`              | 10    |
| `COLLISION_GROUP_NONE`                    | 0     |
| `COLLISION_GROUP_NPC`                     | 9     |
| `COLLISION_GROUP_NPC_ACTOR`               | 18    |
| `COLLISION_GROUP_NPC_SCRIPTED`            | 19    |
| `COLLISION_GROUP_PASSABLE_DOOR`           | 15    |
| `COLLISION_GROUP_PLACEMENT_SOLID`         | 22    |
| `COLLISION_GROUP_PLAYER`                  | 5     |
| `COLLISION_GROUP_PLAYER_HELD`             | 23    |
| `COLLISION_GROUP_PLAYER_MOVEMENT`         | 8     |
| `COLLISION_GROUP_PROJECTILE`              | 13    |
| `COLLISION_GROUP_PUSHAWAY`                | 17    |
| `COLLISION_GROUP_PZ_CLIP`                 | 20    |
| `COLLISION_GROUP_VEHICLE`                 | 7     |
| `COLLISION_GROUP_VEHICLE_CLIP`            | 12    |
| `COLLISION_GROUP_WEAPON`                  | 11    |
| `COLLISION_GROUP_WEIGHTED_CUBE`           | 24    |

## Trace Masks

Trace masks are used with the extended trace API to filter entities by category.

| Name                         | Value      |
| ---------------------------- | ---------- |
| `MASK_ALL`                   | -1         |
| `MASK_BLOCKLOS`              | 16449      |
| `MASK_BLOCKLOS_AND_NPCS`     | 33570881   |
| `MASK_DEADSOLID`             | 65547      |
| `MASK_FLOORTRACE`            | 67125251   |
| `MASK_NPCFLUID`              | 33701891   |
| `MASK_NPCSOLID`              | 33701899   |
| `MASK_NPCSOLID_BRUSHONLY`    | 147467     |
| `MASK_NPCWORLDSTATIC`        | 131083     |
| `MASK_NPCWORLDSTATIC_FLUID`  | 131075     |
| `MASK_OPAQUE`                | 16513      |
| `MASK_OPAQUE_AND_NPCS`       | 33570945   |
| `MASK_PLAYERSOLID`           | 33636363   |
| `MASK_PLAYERSOLID_BRUSHONLY` | 81931      |
| `MASK_SHOT`                  | 1174421507 |
| `MASK_SHOT_BRUSHONLY`        | 67125251   |
| `MASK_SHOT_HULL`             | 100679691  |
| `MASK_SHOT_PORTAL`           | 33570819   |
| `MASK_SOLID`                 | 33570827   |
| `MASK_SOLID_BRUSHONLY`       | 16395      |
| `MASK_SPLITAREAPORTAL`       | 48         |
| `MASK_VISIBLE`               | 24705      |
| `MASK_VISIBLE_AND_NPCS`      | 33579137   |
| `MASK_WATER`                 | 16432      |
| `MASK_WEAPONCLIPPING`        | 100679683  |

## Button Flags

| Name             | Value      |
| ---------------- | ---------- |
| `IN_ATTACK`      | 0x1        |
| `IN_JUMP`        | 0x2        |
| `IN_DUCK`        | 0x4        |
| `IN_FORWARD`     | 0x8        |
| `IN_BACK`        | 0x10       |
| `IN_USE`         | 0x20       |
| `IN_CANCEL`      | 0x40       |
| `IN_LEFT`        | 0x80       |
| `IN_RIGHT`       | 0x100      |
| `IN_MOVELEFT`    | 0x200      |
| `IN_MOVERIGHT`   | 0x400      |
| `IN_ATTACK2`     | 0x800      |
| `IN_RUN`         | 0x1000     |
| `IN_RELOAD`      | 0x2000     |
| `IN_ALT1`        | 0x4000     |
| `IN_ALT2`        | 0x8000     |
| `IN_SCORE`       | 0x10000    |
| `IN_SPEED`       | 0x20000    |
| `IN_WALK`        | 0x40000    |
| `IN_ZOOM`        | 0x80000    |
| `IN_WEAPON1`     | 0x100000   |
| `IN_WEAPON2`     | 0x200000   |
| `IN_GRENADE1`    | 0x800000   |
| `IN_GRENADE2`    | 0x1000000  |
| `IN_LOOKSPIN`    | 0x2000000  |
| `IN_USEORRELOAD` | 0x4000000  |
| `IN_COOP_PING`   | 0x8000000  |
| `IN_REMOTE_VIEW` | 0x10000000 |

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

## Cube Types

| Name               | Value |
| ------------------ | ----- |
| `CUBE_STANDARD`    | 0     |
| `CUBE_COMPANION`   | 1     |
| `CUBE_REFLECTIVE`  | 2     |
| `CUBE_SPHERE`      | 3     |
| `CUBE_ANTIQUE`     | 4     |
| `CUBE_SCHRODINGER` | 5     |

## Misc. Constants

| Name          | Value      |
| ------------- | ---------- |
| `RAND_MAX`    | 2147483647 |
| `PI`          | 3.14159    |
| `_charsize_`  | 1          |
| `_floatsize_` | 8          |
| `_intsize_`   | 8          |
