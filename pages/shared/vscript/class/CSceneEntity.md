---
title: CSceneEntity
---

# CSceneEntity

|Signature|Description|
|---|---|
| `void CSceneEntity::AddBroadcastTeamTarget(int)` | Adds a team (by index) to the broadcast list | 
| `float CSceneEntity::EstimateLength()` | Returns length of this scene in seconds. | 
| `handle CSceneEntity::FindNamedEntity(string)` | given an entity reference, such as !target, get actual entity from scene object | 
| `bool CSceneEntity::IsPaused()` | If this scene is currently paused. | 
| `bool CSceneEntity::IsPlayingBack()` | If this scene is currently playing. | 
| `bool CSceneEntity::LoadSceneFromString(string, string)` | given a dummy scene name and a vcd string, load the scene | 
| `void CSceneEntity::RemoveBroadcastTeamTarget(int)` | Removes a team (by index) from the broadcast list | 
