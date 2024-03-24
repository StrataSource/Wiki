---
title: CBaseFilter
---

# CBaseFilter

*Inherits [CBaseEntity](CBaseEntity)*

|Signature|Description|
|---|---|
| `bool CBaseFilter::PassesDamageFilter(handle, handle)` | Check if the given caller and damage info pass the damage filter, with the second parameter being a CTakeDamageInfo instance. The caller is the one who requests the filter result; For example, the entity being damaged when using this as a damage filter. | 
| `bool CBaseFilter::PassesFilter(handle, handle)` | Check if the given caller and entity pass the filter. The caller is the one who requests the filter result; For example, the entity being damaged when using this as a damage filter. | 
