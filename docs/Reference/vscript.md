---
layout: default
title: VScript API Reference
parent: Reference
---

# VScript API Reference

This page contains a summary of the VScript API available in Chaos-based games that include
VScript. 

Currently the only Chaos game that ships VScript is Portal 2: Community Edition.

## Global Functions

|Signature|Description|
|---|---|
| void AddBranchLevelName(int, string)|Adds a level to the specified branche's list.|
| void AddCoopCreditsName(string)|Adds a name to the coop credit's list.|
| handle CreateProp(string, Vector, string, int)|Create a physics prop|
| handle CreateSceneEntity(string)|Create a scene entity to play the specified scene.|
| void DebugDrawBox(Vector, Vector, Vector, int, int, int, int, float)|Draw a debug overlay box|
| void DebugDrawEntityText(int, int, string, float, int, int, int, int)|Draw debug overlay entity text|
| void DebugDrawEntityTextAtPosition(Vector, int, string, float, int, int, int, int)|Draw a debug overlay entity text at position|
| void DebugDrawGrid(Vector)|Draw debug overlay grid|
| void DebugDrawLine(Vector, Vector, int, int, int, bool, float)|Draw a debug overlay box|
| void DebugDrawScreenText(float, float, string, int, int, int, int, float)|Draw debug overlay screen text|
| void DebugDrawText(Vector, string, bool, float)|Draw debug overlay text|
| void DebugDrawTri(Vector, Vector, Vector, int, int, int, int, bool, float)|Draw a debug overlay triangle|
| void DispatchParticleEffect(string, Vector, Vector)|Dispatches a one-off particle system|
| bool DoIncludeScript(string, handle)|Execute a script (internal)|
| function EntFire(target, action, value, delay, activator)|Generate and entity i/o event|
| void EntFireByHandle(handle, string, string, float, handle, handle)|Generate and entity i/o event. First parameter is an entity instance.|
| float FrameTime()|Get the time spent on the server in the last frame|
| int GetBluePlayerIndex()|Player index of the blue player.|
| int GetCoopBranchLevelIndex(int)|Given the 'branch' argument, returns the current chosen level.|
| int GetCoopSectionIndex()|Section that the coop players have selected to load.|
| int GetDeveloperLevel()|Gets the level of 'developer'|
| int GetHighestActiveBranch()|Returns which branches should be available in the hub.|
| int GetMapIndexInPlayOrder()|Determines which index (by order played) this map is. Returns -1 if entry is not found. -2 if this is not a known community map.|
| string GetMapName()|Get the name of the map.|
| int GetNumMapsPlayed()|Returns how many maps the player has played through.|
| int GetOrangePlayerIndex()|Player index of the orange player.|
| handle GetPlayer()|Returns the player (SP Only).|
| float GetPlayerSilenceDuration(int)|Time that the specified player has been silent on the mic.|
| void GivePlayerPortalgun()|Give player the portalgun.|
| bool IsLevelComplete(int, int)|Returns true if the level in the specified branch is completed by either player.|
| bool IsMultiplayer()|Is this a multiplayer game?|
| bool IsPlayerLevelComplete(int, int, int)|Returns true if the level in the specified branch is completed by a specific player.|
| bool LoopSinglePlayerMaps()|Run the single player maps in a continuous loop.|
| void MarkMapComplete(string)|Marks a maps a complete for both players.|
| void PrecacheMovie(string)|Precaches a named movie. Only valid to call within the entity's 'Precache' function called on mapspawn.|
| float RandomFloat(float, float)|Generate a random floating point number within a range, inclusive|
| int RandomInt(int, int)|Generate a random integer within a range, inclusive|
| void RecordAchievementEvent(string, int)|Records achievement event or progress|
| void RequestMapRating()|Pops up the map rating dialog for user input|
| void ScriptShowHudMessageAll(string, float)|Show center print text message.|
| bool ScriptSteamShowURL(string)|Bring up the steam overlay and shows the specified URL.  (Full address with protocol type is required, e.g. http://www.steamgames.com/)|
| void SendToConsole(string)|Send a string to the console as a command|
| void SendToConsoleServer(string)|Send a string that gets executed on the server as a ServerCommand|
| void SendToPanorama(string, string)|Send an event to Panorama|
| void SetDucking(string, string, float)|Set the level of an audio ducking channel|
| int SetMapAsPlayed()|Adds the current map to the play order and returns the new index therein. Returns -2 if this is not a known community map.|
| void ShowMessage(string)|Print a hud message on all clients|
| float Time()|Get the current server time|
| handle TraceHull(Vector, Vector, Vector, Vector, int, handle, int)|Sweeps a hull along the specified line. Returns a CGameTrace with the trace result|
| float TraceLine(Vector, Vector, handle)|given 2 points & ent to ignore, return fraction along line that hits world or models|
| handle TraceLineEx(Vector, Vector, int, handle, int)|Given 2 points, ent to ignore, collision group and trace mask, returns a CGameTrace with the result|
| handle TracePortalLine(Vector, Vector, int, handle, int, bool)|Same as TraceLineEx, but will transform the trace based on any portals it passes through. Additional boolean determines if the end position should be transformed or left unchanged.|
| bool TryDLC1InstalledOrCatch()|Tests if the DLC1 is installed for Try/Catch blocks.|
| function UniqueString(string)|Generate a string guaranteed to be unique across the life of the script VM, with an optional root string. Useful for adding data to tables when not sure what keys are already in use in that table.|
| void UpgradePlayerPortalgun()|Give player the portalgun.|
| void UpgradePlayerPotatogun()|Give player the portalgun.|

## CLinkedPortalDoor

|Signature|Description|
|---|---|
| handle CLinkedPortalDoor::GetPartnerInstance() | Get the instance handle of the door's linked partner | 
| string CLinkedPortalDoor::GetPartnername() | Returns the partnername of the door. | 

## CBaseFilter

|Signature|Description|
|---|---|
| bool CBaseFilter::PassesDamageFilter(handle, handle) | Check if the given caller and damage info pass the damage filter, with the second parameter being a CTakeDamageInfo instance. The caller is the one who requests the filter result; For example, the entity being damaged when using this as a damage filter. | 
| bool CBaseFilter::PassesFilter(handle, handle) | Check if the given caller and entity pass the filter. The caller is the one who requests the filter result; For example, the entity being damaged when using this as a damage filter. | 

## CEntities

|Signature|Description|
|---|---|
| handle CEntities::CreateByClassname(string) | Creates an entity by classname | 
| handle CEntities::FindByClassname(handle, string) | Find entities by class name. Pass 'null' to start an iteration, or reference to a previously found entity to continue a search | 
| handle CEntities::FindByClassnameNearest(string, Vector, float) | Find entities by class name nearest to a point. | 
| handle CEntities::FindByClassnameWithin(handle, string, Vector, float) | Find entities by class name within a radius. Pass 'null' to start an iteration, or reference to a previously found entity to continue a search | 
| handle CEntities::FindByModel(handle, string) | Find entities by model name. Pass 'null' to start an iteration, or reference to a previously found entity to continue a search | 
| handle CEntities::FindByName(handle, string) | Find entities by name. Pass 'null' to start an iteration, or reference to a previously found entity to continue a search | 
| handle CEntities::FindByNameNearest(string, Vector, float) | Find entities by name nearest to a point. | 
| handle CEntities::FindByNameWithin(handle, string, Vector, float) | Find entities by name within a radius. Pass 'null' to start an iteration, or reference to a previously found entity to continue a search | 
| handle CEntities::FindByTarget(handle, string) | Find entities by targetname. Pass 'null' to start an iteration, or reference to a previously found entity to continue a search | 
| handle CEntities::FindInSphere(handle, Vector, float) | Find entities within a radius. Pass 'null' to start an iteration, or reference to a previously found entity to continue a search | 
| handle CEntities::First() | Begin an iteration over the list of entities | 
| handle CEntities::Next(handle) | Continue an iteration over the list of entities, providing reference to a previously found entity | 

## CBaseFlex

|Signature|Description|
|---|---|
| handle CBaseFlex::GetCurrentScene() | Returns the instance of the oldest active scene entity (if any). | 
| handle CBaseFlex::GetSceneByIndex(int) | Returns the instance of the scene entity at the specified index. | 

## CBasePlayer

|Signature|Description|
|---|---|
| bool CBasePlayer::IsNoclipping() | Returns true if the player is in noclip mode. | 

## CEnvEntityMaker

|Signature|Description|
|---|---|
| void CEnvEntityMaker::SpawnEntity() | Create an entity at the location of the maker | 
| void CEnvEntityMaker::SpawnEntityAtEntityOrigin(handle) | Create an entity at the location of a specified entity instance | 
| void CEnvEntityMaker::SpawnEntityAtLocation(Vector, Vector) | Create an entity at a specified location and orientaton, orientation is Euler angle in degrees (pitch, yaw, roll) | 
| void CEnvEntityMaker::SpawnEntityAtNamedEntityOrigin(string) | Create an entity at the location of a named entity | 

## CFuncTrackTrain

|Signature|Description|
|---|---|
| Vector CFuncTrackTrain::GetFuturePosition(float, float) | Get a position on the track x seconds in the future | 

## CBaseAnimating

|Signature|Description|
|---|---|
| Vector CBaseAnimating::GetAttachmentAngles(int) | Get the attachement id's angles as a p,y,r vector | 
| Vector CBaseAnimating::GetAttachmentOrigin(int) | Get the attachement id's origin vector | 
| int CBaseAnimating::GetObjectScaleLevel() | The scale size of the entity | 
| bool CBaseAnimating::IsSequenceFinished() | Ask whether the main sequence is done playing | 
| int CBaseAnimating::LookupAttachment(string) | Get the named attachement id | 
| void CBaseAnimating::SetBodygroup(int, int) | Sets a bodygroup | 

## CPropLinkedPortalDoor [Portal 2: Community Edition Only]

|Signature|Description|
|---|---|
| handle CPropLinkedPortalDoor::GetPartnerInstance() | Get the instance handle of the door's linked partner | 
| string CPropLinkedPortalDoor::GetPartnername() | Returns the partnername of the door. | 

## CPropWeightedCube [Portal 2: Community Edition Only]

|Signature|Description|
|---|---|
| handle CPropWeightedCube::GetPartner() | Get the instance handle of the schrodinger's partner | 

## CSceneEntity

|Signature|Description|
|---|---|
| void CSceneEntity::AddBroadcastTeamTarget(int) | Adds a team (by index) to the broadcast list | 
| float CSceneEntity::EstimateLength() | Returns length of this scene in seconds. | 
| handle CSceneEntity::FindNamedEntity(string) | given an entity reference, such as !target, get actual entity from scene object | 
| bool CSceneEntity::IsPaused() | If this scene is currently paused. | 
| bool CSceneEntity::IsPlayingBack() | If this scene is currently playing. | 
| bool CSceneEntity::LoadSceneFromString(string, string) | given a dummy scene name and a vcd string, load the scene | 
| void CSceneEntity::RemoveBroadcastTeamTarget(int) | Removes a team (by index) from the broadcast list | 

## CScriptKeyValues

|Signature|Description|
|---|---|
| void CScriptKeyValues::Clear() | Clears this KeyValues object. | 
| handle CScriptKeyValues::FindKey(string, bool) | Given a KeyValues object and a key name, find a KeyValues object associated with the key name | 
| handle CScriptKeyValues::GetFirstSubKey() | Given a KeyValues object, return the first sub key object | 
| bool CScriptKeyValues::GetKeyBool(string) | Given a KeyValues object and a key name, return associated bool value | 
| float CScriptKeyValues::GetKeyFloat(string) | Given a KeyValues object and a key name, return associated float value | 
| int CScriptKeyValues::GetKeyInt(string) | Given a KeyValues object and a key name, return associated integer value | 
| string CScriptKeyValues::GetKeyString(string) | Given a KeyValues object and a key name, return associated string value | 
| handle CScriptKeyValues::GetNextKey() | Given a KeyValues object, return the next key object in a sub key group | 
| bool CScriptKeyValues::IsKeyEmpty(string) | Given a KeyValues object and a key name, return true if key name has no value | 
| void CScriptKeyValues::ReleaseKeyValues() | Given a root KeyValues object, release its contents | 
| void CScriptKeyValues::SetKeyBool(string, bool) | Given a KeyValues object and a key name, sets the associated bool value | 
| void CScriptKeyValues::SetKeyFloat(string, float) | Given a KeyValues object and a key name, sets the associated float value | 
| void CScriptKeyValues::SetKeyInt(string, int) | Given a KeyValues object and a key name, sets the associated integer value | 
| void CScriptKeyValues::SetKeyString(string, string) | Given a KeyValues object and a key name, sets the associated string value | 

## CTakeDamageInfo

|Signature|Description|
|---|---|
| void CTakeDamageInfo::AddDamage(float) | Adds to the damage. | 
| void CTakeDamageInfo::AddDamageType(int) | Adds to the damage type. | 
| bool CTakeDamageInfo::BaseDamageIsValid() | Checks if the base damage is valid. | 
| string CTakeDamageInfo::GetAmmoName() | Gets the ammo type name. | 
| int CTakeDamageInfo::GetAmmoType() | Gets the ammo type. | 
| handle CTakeDamageInfo::GetAttacker() | Gets the attacker. | 
| float CTakeDamageInfo::GetBaseDamage() | Gets the base damage. | 
| float CTakeDamageInfo::GetDamage() | Gets the damage. | 
| int CTakeDamageInfo::GetDamageCustom() | Gets the damage custom. | 
| Vector CTakeDamageInfo::GetDamageForce() | Gets the damage force. | 
| Vector CTakeDamageInfo::GetDamagePosition() | Gets the damage position. | 
| int CTakeDamageInfo::GetDamageStats() | Gets the damage stats. | 
| int CTakeDamageInfo::GetDamageType() | Gets the damage type. | 
| int CTakeDamageInfo::GetDamagedOtherPlayers() | Gets whether other players have been damaged. | 
| handle CTakeDamageInfo::GetInflictor() | Gets the inflictor. | 
| float CTakeDamageInfo::GetMaxDamage() | Gets the max damage. | 
| Vector CTakeDamageInfo::GetReportedPosition() | Gets the reported damage position. | 
| handle CTakeDamageInfo::GetWeapon() | Gets the weapon. | 
| void CTakeDamageInfo::ScaleDamage(float) | Scales the damage. | 
| void CTakeDamageInfo::ScaleDamageForce(float) | Scales the damage force. | 
| void CTakeDamageInfo::SetAmmoType(int) | Sets the ammo type. | 
| void CTakeDamageInfo::SetAttacker(handle) | Sets the attacker. | 
| void CTakeDamageInfo::SetDamage(float) | Sets the damage. | 
| void CTakeDamageInfo::SetDamageCustom(int) | Sets the damage custom. | 
| void CTakeDamageInfo::SetDamageForce(Vector) | Sets the damage force. | 
| void CTakeDamageInfo::SetDamagePosition(Vector) | Sets the damage position. | 
| void CTakeDamageInfo::SetDamageStats(int) | Sets the damage stats. | 
| void CTakeDamageInfo::SetDamageType(int) | Sets the damage type. | 
| void CTakeDamageInfo::SetDamagedOtherPlayers(int) | Sets whether other players have been damaged. | 
| void CTakeDamageInfo::SetInflictor(handle) | Sets the inflictor. | 
| void CTakeDamageInfo::SetMaxDamage(float) | Sets the max damage. | 
| void CTakeDamageInfo::SetReportedPosition(Vector) | Sets the reported damage position. | 
| void CTakeDamageInfo::SetWeapon(handle) | Sets the weapon. | 
| void CTakeDamageInfo::SubtractDamage(float) | Removes from the damage. | 

## CPlayerVoiceListener

|Signature|Description|
|---|---|
| float CPlayerVoiceListener::GetPlayerSpeechDuration(int) | Returns the number of seconds the player has been continuously speaking. | 
| bool CPlayerVoiceListener::IsPlayerSpeaking(int) | Returns whether the player specified is speaking. | 

## CBaseEntity

|Signature|Description|
|---|---|
| void CBaseEntity::ConnectOutput(string, string) | Adds an I/O connection that will call the named function when the specified output fires | 
| void CBaseEntity::Destroy() |  | 
| void CBaseEntity::DisconnectOutput(string, string) | Removes a connected script function from an I/O event. | 
| void CBaseEntity::EmitSound(string) | Plays a sound from this entity. | 
| Vector CBaseEntity::EyeAngles() | Get eye pitch, yaw, roll as a vector | 
| Vector CBaseEntity::EyeLocalAngles() | Get eye local pitch, yaw, roll as a vector | 
| Vector CBaseEntity::EyePosition() | Get vector to eye position - absolute coords | 
| handle CBaseEntity::FirstMoveChild() |  | 
| Vector CBaseEntity::GetAngles() | Get entity pitch, yaw, roll as a vector | 
| Vector CBaseEntity::GetAngularVelocity() | Get the local angular velocity - returns a vector of pitch,yaw,roll | 
| Vector CBaseEntity::GetBoundingMaxs() | Get a vector containing max bounds, centered on object | 
| Vector CBaseEntity::GetBoundingMins() | Get a vector containing min bounds, centered on object | 
| Vector CBaseEntity::GetCenter() | Get vector to center of object - absolute coords | 
| string CBaseEntity::GetClassname() |  | 
| Vector CBaseEntity::GetForwardVector() | Get the forward vector of the entity | 
| float CBaseEntity::GetFriction() |  | 
| float CBaseEntity::GetGravity() |  | 
| int CBaseEntity::GetHealth() |  | 
| Vector CBaseEntity::GetLeftVector() | Get the left vector of the entity | 
| int CBaseEntity::GetMaxHealth() |  | 
| handle CBaseEntity::GetModelKeyValues() | Get a KeyValue class instance on this entity's model | 
| string CBaseEntity::GetModelName() | Returns the name of the model | 
| handle CBaseEntity::GetMoveParent() | If in hierarchy, retrieves the entity's parent | 
| string CBaseEntity::GetName() |  | 
| Vector CBaseEntity::GetOrigin() |  | 
| handle CBaseEntity::GetOwner() | Gets this entity's owner | 
| string CBaseEntity::GetPreTemplateName() | Get the entity name stripped of template unique decoration | 
| handle CBaseEntity::GetRootMoveParent() | If in hierarchy, walks up the hierarchy to find the root parent | 
| string CBaseEntity::GetScriptId() | Retrieve the unique identifier used to refer to the entity within the scripting system | 
| handle CBaseEntity::GetScriptScope() | Retrieve the script-side data associated with an entity | 
| float CBaseEntity::GetSoundDuration(string, string) | Returns float duration of the sound. Takes soundname and optional actormodelname. | 
| int CBaseEntity::GetTeam() |  | 
| Vector CBaseEntity::GetUpVector() | Get the up vector of the entity | 
| Vector CBaseEntity::GetVelocity() |  | 
| handle CBaseEntity::NextMovePeer() |  | 
| void CBaseEntity::PrecacheModel(string) |  | 
| void CBaseEntity::PrecacheScriptSound(string) |  | 
| void CBaseEntity::PrecacheSoundScript(string) | Precache a sound for later playing. | 
| void CBaseEntity::SetAbsOrigin(Vector) | SetAbsOrigin | 
| void CBaseEntity::SetAngles(float, float, float) | Set entity pitch, yaw, roll | 
| void CBaseEntity::SetAngularVelocity(float, float, float) | Set the local angular velocity - takes float pitch,yaw,roll velocities | 
| void CBaseEntity::SetForwardVector(Vector) | Set the orientation of the entity to have this forward vector | 
| void CBaseEntity::SetFriction(float) |  | 
| void CBaseEntity::SetGravity(float) | Sets gravity on this entity. Only affects gravity along Z axis | 
| void CBaseEntity::SetHealth(int) |  | 
| void CBaseEntity::SetMaxHealth(int) |  | 
| void CBaseEntity::SetModel(string) |  | 
| void CBaseEntity::SetOrigin(Vector) |  | 
| void CBaseEntity::SetOwner(handle) | Sets this entity's owner | 
| void CBaseEntity::SetSize(Vector, Vector) |  | 
| void CBaseEntity::SetTeam(int) |  | 
| void CBaseEntity::SetVelocity(Vector) |  | 
| void CBaseEntity::StopSound(string) | Stops a sound on this entity. | 
| bool CBaseEntity::ValidateScriptScope() | Ensure that an entity's script scope has been created | 
| int CBaseEntity::entindex() |  | 

## CGameTrace

|Signature|Description|
|---|---|
| bool CGameTrace::DidHit() | Returns true if the trace hit anything | 
| bool CGameTrace::DidHitNonWorldEntity() | Returns true if the trace hit non-world entity | 
| bool CGameTrace::DidHitWorld() | Returns true if trace hit world | 
| int CGameTrace::GetContents() | Returns the contents flags of the hit entity or surface | 
| Vector CGameTrace::GetEndPos() | Returns the end position of the trace | 
| handle CGameTrace::GetEntity() | Returns a handle to the entity this trace hit | 
| int CGameTrace::GetEntityIndex() | Returns the index of the entity hit, or -1 if it did not hit an entity | 
| float CGameTrace::GetFraction() | Time completed, 1.0 means no hit | 
| Vector CGameTrace::GetImpactNormal() | Returns the normal of the plane where the trace hit | 
| Vector CGameTrace::GetStartPos() | Returns the start position of the trace | 

## CPointViewControl

|Signature|Description|
|---|---|
| int CPointViewControl::GetFov() | get camera's current fov setting as integer | 
| void CPointViewControl::SetFov(int, float) | set camera's current fov in integer degrees and fov change rate as float | 

## CPortal\_Player [Portal 2: Community Edition Only]

|Signature|Description|
|---|---|
| int CPortal_Player::GetWheatleyMonitorDestructionCount() | Get number of wheatley monitors destroyed by the player. | 
| void CPortal_Player::IncWheatleyMonitorDestructionCount() | Set number of wheatley monitors destroyed by the player. | 
| void CPortal_Player::TurnOffPotatos() | Turns Off the Potatos material light | 
| void CPortal_Player::TurnOnPotatos() | Turns On the Potatos material light | 

## Script Constants


|Name|Value|
|---|---|
| `BOUNCE_POWER` | `0` | 
| `COLLISION_GROUP_BREAKABLE_GLASS` | `6` | 
| `COLLISION_GROUP_CAMERA_SOLID` | `21` | 
| `COLLISION_GROUP_DEBRIS` | `1` | 
| `COLLISION_GROUP_DEBRIS_BLOCK_PROJECTILE` | `25` | 
| `COLLISION_GROUP_DEBRIS_TRIGGER` | `2` | 
| `COLLISION_GROUP_DISSOLVING` | `16` | 
| `COLLISION_GROUP_DOOR_BLOCKER` | `14` | 
| `COLLISION_GROUP_INTERACTIVE` | `4` | 
| `COLLISION_GROUP_INTERACTIVE_DEBRIS` | `3` | 
| `COLLISION_GROUP_IN_VEHICLE` | `10` | 
| `COLLISION_GROUP_NONE` | `0` | 
| `COLLISION_GROUP_NPC` | `9` | 
| `COLLISION_GROUP_NPC_ACTOR` | `18` | 
| `COLLISION_GROUP_NPC_SCRIPTED` | `19` | 
| `COLLISION_GROUP_PASSABLE_DOOR` | `15` | 
| `COLLISION_GROUP_PLACEMENT_SOLID` | `22` | 
| `COLLISION_GROUP_PLAYER` | `5` | 
| `COLLISION_GROUP_PLAYER_HELD` | `23` | 
| `COLLISION_GROUP_PLAYER_MOVEMENT` | `8` | 
| `COLLISION_GROUP_PROJECTILE` | `13` | 
| `COLLISION_GROUP_PUSHAWAY` | `17` | 
| `COLLISION_GROUP_PZ_CLIP` | `20` | 
| `COLLISION_GROUP_VEHICLE` | `7` | 
| `COLLISION_GROUP_VEHICLE_CLIP` | `12` | 
| `COLLISION_GROUP_WEAPON` | `11` | 
| `COLLISION_GROUP_WEIGHTED_CUBE` | `24` | 
| `MASK_ALL` | `-1` | 
| `MASK_BLOCKLOS` | `16449` | 
| `MASK_BLOCKLOS_AND_NPCS` | `33570881` | 
| `MASK_DEADSOLID` | `65547` | 
| `MASK_FLOORTRACE` | `67125251` | 
| `MASK_NPCFLUID` | `33701891` | 
| `MASK_NPCSOLID` | `33701899` | 
| `MASK_NPCSOLID_BRUSHONLY` | `147467` | 
| `MASK_NPCWORLDSTATIC` | `131083` | 
| `MASK_NPCWORLDSTATIC_FLUID` | `131075` | 
| `MASK_OPAQUE` | `16513` | 
| `MASK_OPAQUE_AND_NPCS` | `33570945` | 
| `MASK_PLAYERSOLID` | `33636363` | 
| `MASK_PLAYERSOLID_BRUSHONLY` | `81931` | 
| `MASK_SHOT` | `1174421507` | 
| `MASK_SHOT_BRUSHONLY` | `67125251` | 
| `MASK_SHOT_HULL` | `100679691` | 
| `MASK_SHOT_PORTAL` | `33570819` | 
| `MASK_SOLID` | `33570827` | 
| `MASK_SOLID_BRUSHONLY` | `16395` | 
| `MASK_SPLITAREAPORTAL` | `48` | 
| `MASK_VISIBLE` | `24705` | 
| `MASK_VISIBLE_AND_NPCS` | `33579137` | 
| `MASK_WATER` | `16432` | 
| `MASK_WEAPONCLIPPING` | `100679683` | 
| `NO_POWER` | `4` | 
| `PI` | `3.14159` | 
| `PORTAL_POWER` | `3` | 
| `RAND_MAX` | `2147483647` | 
| `REFLECT_POWER` | `1` | 
| `SPEED_POWER` | `2` | 
| `STICK_POWER` | `5` | 
| `_charsize_` | `1` | 
| `_floatsize_` | `8` | 
| `_intsize_` | `8` |
