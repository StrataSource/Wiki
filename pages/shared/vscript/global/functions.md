---
title: Functions
---

# Global Functions

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
