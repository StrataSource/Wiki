---
title: CScriptKeyValues
---

# CScriptKeyValues

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
