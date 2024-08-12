---
title: CGameTrace
---

# CGameTrace

|Signature|Description|
|---|---|
| `bool CGameTrace::DidHit()` | Returns true if the trace hit anything | 
| `bool CGameTrace::DidHitNonWorldEntity()` | Returns true if the trace hit non-world entity | 
| `bool CGameTrace::DidHitWorld()` | Returns true if trace hit world | 
| `int CGameTrace::GetContents()` | Returns the contents flags of the hit entity or surface | 
| `Vector CGameTrace::GetEndPos()` | Returns the end position of the trace | 
| `handle CGameTrace::GetEntity()` | Returns a handle to the entity this trace hit | 
| `int CGameTrace::GetEntityIndex()` | Returns the index of the entity hit, or -1 if it did not hit an entity | 
| `float CGameTrace::GetFraction()` | Time completed, 1.0 means no hit | 
| `Vector CGameTrace::GetImpactNormal()` | Returns the normal of the plane where the trace hit | 
| `Vector CGameTrace::GetStartPos()` | Returns the start position of the trace | 
