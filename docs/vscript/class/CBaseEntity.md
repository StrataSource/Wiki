---
title: CBaseEntity
---

# CBaseEntity

|Signature|Description|
|---|---|
| `void CBaseEntity::ConnectOutput(string, string)` | Adds an I/O connection that will call the named function when the specified output fires | 
| `void CBaseEntity::Destroy()` |  | 
| `void CBaseEntity::DisconnectOutput(string, string)` | Removes a connected script function from an I/O event. | 
| `void CBaseEntity::EmitSound(string)` | Plays a sound from this entity. | 
| `Vector CBaseEntity::EyeAngles()` | Get eye pitch, yaw, roll as a vector | 
| `Vector CBaseEntity::EyeLocalAngles()` | Get eye local pitch, yaw, roll as a vector | 
| `Vector CBaseEntity::EyePosition()` | Get vector to eye position - absolute coords | 
| `handle CBaseEntity::FirstMoveChild()` |  | 
| `Vector CBaseEntity::GetAngles()` | Get entity pitch, yaw, roll as a vector | 
| `Vector CBaseEntity::GetAngularVelocity()` | Get the local angular velocity - returns a vector of pitch,yaw,roll | 
| `Vector CBaseEntity::GetBoundingMaxs()` | Get a vector containing max bounds, centered on object | 
| `Vector CBaseEntity::GetBoundingMins()` | Get a vector containing min bounds, centered on object | 
| `Vector CBaseEntity::GetCenter()` | Get vector to center of object - absolute coords | 
| `string CBaseEntity::GetClassname()` |  | 
| `Vector CBaseEntity::GetForwardVector()` | Get the forward vector of the entity | 
| `float CBaseEntity::GetFriction()` |  | 
| `float CBaseEntity::GetGravity()` |  | 
| `int CBaseEntity::GetHealth()` |  | 
| `Vector CBaseEntity::GetLeftVector()` | Get the left vector of the entity | 
| `int CBaseEntity::GetMaxHealth()` |  | 
| `handle CBaseEntity::GetModelKeyValues()` | Get a KeyValue class instance on this entity's model | 
| `string CBaseEntity::GetModelName()` | Returns the name of the model | 
| `handle CBaseEntity::GetMoveParent()` | If in hierarchy, retrieves the entity's parent | 
| `string CBaseEntity::GetName()` |  | 
| `Vector CBaseEntity::GetOrigin()` |  | 
| `handle CBaseEntity::GetOwner()` | Gets this entity's owner | 
| `string CBaseEntity::GetPreTemplateName()` | Get the entity name stripped of template unique decoration | 
| `handle CBaseEntity::GetRootMoveParent()` | If in hierarchy, walks up the hierarchy to find the root parent | 
| `string CBaseEntity::GetScriptId()` | Retrieve the unique identifier used to refer to the entity within the scripting system | 
| `handle CBaseEntity::GetScriptScope()` | Retrieve the script-side data associated with an entity |
| `int CBaseEntity::GetMoveType()` | Returns the current move type |
| `int CBaseEntity::GetMoveCollide()` | Returns the current move collide type |
| `int CBaseEntity::GetCollisionGroup()` | Returns the collision group |
| `float CBaseEntity::GetSoundDuration(string, string)` | Returns float duration of the sound. Takes soundname and optional actormodelname. | 
| `int CBaseEntity::GetTeam()` |  | 
| `Vector CBaseEntity::GetUpVector()` | Get the up vector of the entity | 
| `Vector CBaseEntity::GetVelocity()` |  | 
| `handle CBaseEntity::NextMovePeer()` |  | 
| `void CBaseEntity::PrecacheModel(string)` |  | 
| `void CBaseEntity::PrecacheScriptSound(string)` |  | 
| `void CBaseEntity::PrecacheSoundScript(string)` | Precache a sound for later playing. | 
| `void CBaseEntity::SetAbsOrigin(Vector)` | SetAbsOrigin | 
| `void CBaseEntity::SetParent(HSCRIPT hParent)` | Sets the parent entity |
| `void CBaseEntity::SetParentWithAttachment(HSCRIPT hParent, int iAttachment)` | Sets the parent entity, and assuming the location of the specified attachment |
| `void CBaseEntity::SetMoveType(int moveType)` | Sets the move type |
| `void CBaseEntity::SetMoveCollide(int moveCollide)` | Sets the move collide mode |
| `void CBaseEntity::SetCollisionGroup(int group)` | Sets the collision group |
| `void CBaseEntity::SetAngles(float, float, float)` | Set entity pitch, yaw, roll | 
| `void CBaseEntity::SetAngularVelocity(float, float, float)` | Set the local angular velocity - takes float pitch,yaw,roll velocities | 
| `void CBaseEntity::SetForwardVector(Vector)` | Set the orientation of the entity to have this forward vector | 
| `void CBaseEntity::SetFriction(float)` |  | 
| `void CBaseEntity::SetGravity(float)` | Sets gravity on this entity. Only affects gravity along Z axis | 
| `void CBaseEntity::SetHealth(int)` |  | 
| `void CBaseEntity::SetMaxHealth(int)` |  | 
| `void CBaseEntity::SetModel(string)` |  | 
| `void CBaseEntity::SetOrigin(Vector)` |  | 
| `void CBaseEntity::SetOwner(handle)` | Sets this entity's owner | 
| `void CBaseEntity::SetSize(Vector, Vector)` |  | 
| `void CBaseEntity::SetTeam(int)` |  | 
| `void CBaseEntity::SetVelocity(Vector)` |  | 
| `void CBaseEntity::Spawn()` | Calls the entity's Spawn function. This properly initializes the entity and allows it to begin simulating.| 
| `void CBaseEntity::StopSound(string)` | Stops a sound on this entity. | 
| `bool CBaseEntity::ValidateScriptScope()` | Ensure that an entity's script scope has been created | 
| `int CBaseEntity::entindex()` |  | 
