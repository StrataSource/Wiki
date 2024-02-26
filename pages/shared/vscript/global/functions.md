---
title: Functions
---

# Global Functions

|Signature|Description|
|---|---|
| `void AddBranchLevelName(int branch, string level)`|Adds a level to the specified branche's list.|
| `void AddCoopCreditsName(string name)`|Adds a name to the coop credit's list.|
| `handle CreateProp(string entityName, Vector origin, string modelName, int animIndex)`|Create a physics prop|
| `handle CreateSceneEntity(string scene)`|Create a scene entity to play the specified scene.|
| `void DebugDrawBox(Vector origin, Vector mins, Vector maxs, int r, int g, int b, int a, float duration)`|Draw a debug overlay box|
| `void DebugDrawBoxAngles(Vector origin, Vector mins, Vector maxs, Vector angles, int r, int g, int b, int a, float duration)`|Draw a debug overlay box with specific angles|
| `void DebugDrawEntityText(int entIndex, int text_offset, string text, float duration, int r, int g, int b, int a)`|Draw debug overlay entity text|
| `void DebugDrawEntityTextAtPosition(Vector pos, int text_offset, string text, float duration, int r, int g, int b, int a)`|Draw a debug overlay entity text at position|
| `void DebugDrawGrid(Vector origin)`|Draw debug overlay grid|
| `void DebugDrawLine(Vector origin, Vector target, int r, int b, int b, bool noDepthTest, float duration)`|Draw a debug overlay box|
| `void DebugDrawScreenText(float xpos, float ypos, string text, int r, int g, int b, int a, float duration)`|Draw debug overlay screen text|
| `void DebugDrawText(Vector origin, string text, bool viewCheck, float duration)`|Draw debug overlay text|
| `void DebugDrawTri(Vector p1, Vector p2, Vector p3, int r, int g, int b, int a, bool noDepthTest, float duration)`|Draw a debug overlay triangle|
| `void DispatchParticleEffect(string particleName, Vector origin, Vector angles)`|Dispatches a one-off particle system|
| `bool DoIncludeScript(string, handle)`|Execute a script (internal, do not use)|
| `function EntFire(handle target, string action, string value, float delay, handle activator)`|Generate and entity i/o event|
| `void EntFireByHandle(handle target, string action, string value, float delay, handle activator, handle caller)`|Generate and entity i/o event. First parameter is an entity instance.|
| `float FrameTime()`|Get the time spent on the server in the last frame|
| `int GetBluePlayerIndex()`|Player index of the blue player.|
| `int GetCoopBranchLevelIndex(int branch)`|Given the 'branch' argument, returns the current chosen level.|
| `int GetCoopSectionIndex()`|Section that the coop players have selected to load.|
| `int GetDeveloperLevel()`|Gets the level of 'developer'|
| `int GetHighestActiveBranch()`|Returns which branches should be available in the hub.|
| `int GetMapIndexInPlayOrder()`|Determines which index (by order played) this map is. Returns -1 if entry is not found. -2 if this is not a known community map.|
| `string GetMapName()`|Get the name of the map.|
| `int GetNumMapsPlayed()`|Returns how many maps the player has played through.|
| `int GetOrangePlayerIndex()`|Player index of the orange player.|
| `handle GetPlayer()`|Returns the player (SP Only).|
| `float GetPlayerSilenceDuration(int playerIndex)`|Time that the specified player has been silent on the mic.|
| `void GivePlayerPortalgun()`|Give player the portalgun.|
| `bool IsLevelComplete(int branch, int level)`|Returns true if the level in the specified branch is completed by either player.|
| `bool IsMultiplayer()`|Is this a multiplayer game?|
| `bool IsPlayerLevelComplete(int playerIndex, int branch, int level)`|Returns true if the level in the specified branch is completed by a specific player.|
| `bool LoopSinglePlayerMaps()`|Run the single player maps in a continuous loop.|
| `void MarkMapComplete(string mapName)`|Marks a maps a complete for both players.|
| `void PrecacheMovie(string movieName)`|Precaches a named movie. Only valid to call within the entity's 'Precache' function called on mapspawn.|
| `float RandomFloat(float min, float max)`|Generate a random floating point number within a range, inclusive|
| `int RandomInt(int min, int max)`|Generate a random integer within a range, inclusive|
| `void RecordAchievementEvent(string achName, int playerIndex)`|Records achievement event or progress|
| `void RequestMapRating()`|Pops up the map rating dialog for user input|
| `void ScriptShowHudMessageAll(string msg, float duration)`|Show center print text message.|
| `bool ScriptSteamShowURL(string url)`|Bring up the steam overlay and shows the specified URL.  (Full address with protocol type is required, e.g. http://www.steamgames.com/)|
| `void SendToConsole(string cmd)`|Send a string to the console as a command|
| `void SendToConsoleServer(string cmd)`|Send a string that gets executed on the server as a ServerCommand|
| `void SendToPanorama(string eventName, string playload)`|Send an event to Panorama|
| `void SetDucking(string layerName, string mixGroupName, float factor)`|Set the level of an audio ducking channel|
| `int SetMapAsPlayed()`|Adds the current map to the play order and returns the new index therein. Returns -2 if this is not a known community map.|
| `void ShowMessage(string message)`|Print a hud message on all clients|
| `float Time()`|Get the current server time|
| `handle TraceHull(Vector start, Vector end, Vector hullMin, Vector hullMax, int entityMask, handle entIgnore, int collisionGroup)`|Sweeps a hull along the specified line. Returns a CGameTrace with the trace result|
| `float TraceLine(Vector start, Vector end, handle entIgnore)`|given 2 points & ent to ignore, return fraction along line that hits world or models|
| `handle TraceLineEx(Vector start, Vector end, int entityMask, handle entToIgnore, int collisionGroup)`|Given 2 points, ent to ignore, collision group and trace mask, returns a CGameTrace with the result|
| `handle TracePortalLine(Vector start, Vector end, int entityMask, handle entToIgnore, int collisionGroup, bool transformTrace)`|Same as TraceLineEx, but will transform the trace based on any portals it passes through. Additional boolean determines if the end position should be transformed or left unchanged.|
| `bool TryDLC1InstalledOrCatch()`|Tests if the DLC1 is installed for Try/Catch blocks.|
| `function UniqueString(string templateStr)`|Generate a string guaranteed to be unique across the life of the script VM, with an optional root string. Useful for adding data to tables when not sure what keys are already in use in that table.|
| `void UpgradePlayerPortalgun()`|Give player the portalgun.|
| `void UpgradePlayerPotatogun()`|Give player the portalgun.|
