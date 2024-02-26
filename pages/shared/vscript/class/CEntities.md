---
title: CEntities
---

# CEntities

|Signature|Description|
|---|---|
| `handle CEntities::CreateByClassname(string)` | Creates an entity by classname | 
| `handle CEntities::FindByClassname(handle, string)` | Find entities by class name. Pass 'null' to start an iteration, or reference to a previously found entity to continue a search | 
| `handle CEntities::FindByClassnameNearest(string, Vector, float)` | Find entities by class name nearest to a point. | 
| `handle CEntities::FindByClassnameWithin(handle, string, Vector, float)` | Find entities by class name within a radius. Pass 'null' to start an iteration, or reference to a previously found entity to continue a search | 
| `handle CEntities::FindByModel(handle, string)` | Find entities by model name. Pass 'null' to start an iteration, or reference to a previously found entity to continue a search | 
| `handle CEntities::FindByName(handle, string)` | Find entities by name. Pass 'null' to start an iteration, or reference to a previously found entity to continue a search | 
| `handle CEntities::FindByNameNearest(string, Vector, float)` | Find entities by name nearest to a point. | 
| `handle CEntities::FindByNameWithin(handle, string, Vector, float)` | Find entities by name within a radius. Pass 'null' to start an iteration, or reference to a previously found entity to continue a search | 
| `handle CEntities::FindByTarget(handle, string)` | Find entities by targetname. Pass 'null' to start an iteration, or reference to a previously found entity to continue a search | 
| `handle CEntities::FindInSphere(handle, Vector, float)` | Find entities within a radius. Pass 'null' to start an iteration, or reference to a previously found entity to continue a search | 
| `handle CEntities::First()` | Begin an iteration over the list of entities | 
| `handle CEntities::GetByIndex(int)` | Get an entity via its entity index. |
| `handle CEntities::Next(handle)` | Continue an iteration over the list of entities, providing reference to a previously found entity | 
