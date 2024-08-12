---
title: CBaseAnimating
---

# CBaseAnimating

*Inherits [CBaseEntity](CBaseEntity)*

|Signature|Description|
|---|---|
| `Vector CBaseAnimating::GetAttachmentAngles(int)` | Get the attachement id's angles as a p,y,r vector | 
| `Vector CBaseAnimating::GetAttachmentOrigin(int) `| Get the attachement id's origin vector | 
| `int CBaseAnimating::GetObjectScaleLevel()` | The scale size of the entity | 
| `bool CBaseAnimating::IsSequenceFinished()` | Ask whether the main sequence is done playing | 
| `int CBaseAnimating::LookupAttachment(string)` | Get the named attachement id | 
| `void CBaseAnimating::SetBodygroup(int, int)` | Sets a bodygroup | 
| `int CBaseAnimating::GetBodygroup(int group)` | Gets a bodygroup |
| `int CBaseAnimating::GetBodygroupCount(int group)` | Gets the number of bodygroups in a group |
| `int CBaseAnimating::GetNumBodyGroups()` | Returns the number of bodygroup groups |
| `string CBaseAnimating::GetBodygroupName(int group)` | Returns the name of the bodygroup |
| `string CBaseAnimating::GetBodygroupPartName(int group, int part)` | Returns the bodygroup part name |
| `int CBaseAnimating::GetBoneCount()` | Returns the number of bones |
| `Vector CBaseAnimating::GetBonePosition(int bone)` | Returns the world origin of the bone |
| `Vector CBaseAnimating::GetBoneRotation(int bone)` | Returns the rotation of the bone, in pitch, yaw, roll format |
| `int CBaseAnimating::LookupPoseParameter(string name)` | Lookup a pose parameter based on its name. Returns -1 if not found |
| `float CBaseAnimating::GetPoseParameter(int param)` | Returns pose parameter value based on index |
| `float CBaseAnimating::SetPoseParameter(int param, float value)` | Set pose parameter value based on index |
| `float CBaseAnimating::GetPoseParameterMax(int param)` | Returns the max value of the pose parameter |
| `float CBaseAnimating::GetPoseParameterMin(int param)` | Returns the min value of the pose parameter |
| `float CBaseAnimating::GetPlaybackRate()` | Returns the current playback rate |
| `void CBaseAnimating::SetPlaybackRate(float rate)` | Sets the current playback rate |
| `bool CBaseAnimating::IsValidSequence(int sequence)` | Checks if the specified sequence is valid |
| `int CBaseAnimating::GetSequence()` | Returns the current sequence |
| `void CBaseAnimating::SetSequence(int sequence)` | Sets the current sequence |
| `int CBaseAnimating::GetSequenceCount()` | Returns the number of available sequences |
| `string CBaseAnimating::GetSequenceName(int sequence)` | Returns the name of the sequence, if it's valid |
| `string CBaseAnimating::GetSequenceActivityName(int sequence)` | Returns the name of the sequence's activity |
| `int CBaseAnimating::LookupSequence(string name)` | Looks up a sequence based on name |
| `bool CBaseAnimating::LookupActivity(string name)` | Looks up an activity based on name |
| `bool CBaseAnimating::IsActivityFinished(int activity)` | Is the current activity finished? |
| `bool CBaseAnimating::IsSequenceFinished(int sequence)` | Is the current sequence finished? |
| `float CBaseAnimating::GetSequenceDuration(int sequence)` | Gets the sequence duration for the specified sequence |
| `float CBaseAnimating::GetSequenceCycleRate(int sequence)` | Gets the sequence cycle rate for the specified sequence |
| `bool CBaseAnimating::IsSequenceLooped(int sequence)` | Returns if the specified sequence is looped or not |