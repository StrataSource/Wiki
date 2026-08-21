---
title: Core Event Types
weight: 20
---

# Core Event Types

This script demonstrates/tests various core event types. These are invoked during the game init process.

```as
[LevelInitPreEntity]
void OnLevelInitPreEntity()
{
    Msg("level init pre-entity\n");
}

[LevelInitPostEntity]
void OnLevelInitPostEntity()
{
    Msg("level init post-entity\n");
}

[LevelShutdownPreEntity]
void OnLevelShutdownPreEntity()
{
    Msg("Level shutdown pre-entity\n");
}

[LevelShutdownPostEntity]
void OnLevelShutdownPostEntity()
{
    Msg("Level shutdown post-entity\n");
}
```

[Link to Original `sample-content` Example File](https://github.com/StrataSource/sample-content/blob/main/code/shared/init_events.as)
