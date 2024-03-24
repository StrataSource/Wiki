---
title: CPropPortal
---

# CPropPortal

*Inherits [CBasePortal](CBasePortal)*

| Signature | Description |
|---|---|
| `void SetActivatedState(bool activated)` | Activates or deactivates a portal |
| `void Resize(float halfWidth, float halfHeight)` | Resizes the portal to the specified dimensions. Please note that these are 'half' dimensions |
| `void Fizzle()` | Fizzle this portal |
| `void NewLocation(Vector vecPos, Vector angles)` | Move this portal to a new location with the specified position and angles |
| `void SetLinkageGroupID(int id)` | Set this portal's linkage group ID |
| `int GetLinkageGroupID()` | Returns this portal's linkage group ID |
| `handle GetFiredByPlayer()` | Returns a handle to the player that fired the portal, or null if none |
