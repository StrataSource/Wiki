---
title: Classes
---

# Classes

This page outlines the various Strata Hammer AngelScript classes.

## `BoundBox`

```as
class BoundBox
{
  void GetBoundsCenter(Vector&out center) const;
  bool ContainsPoint(const Vector&in point) const;
  void GetBoundsSize(Vector&out size) const;
  const Vector maxs;
  const Vector mins;
}
```

## `CMapClass`

```as
class CMapClass
{
}
```

## `CMapGroup`

```as
class CMapGroup
{
  CMapGroup@ CMapGroup();
  void AddChild(CMapClass@ child);
  void CalcBounds(bool full);
  void GetBoundsSize(Vector&out size);
  void TransMove(const Vector&in delta);
  void TransRotate(const Vector&in refPoint, const QAngle&in angle);
  void TransScale(const Vector&in refPoint, const Vector&in scale);
  CMapClass@ opImplCast();
}
```

## `CMapSolid`

```as
class CMapSolid
{
  CMapSolid@ CMapSolid();
  void AddFace(const CMapFace&in face);
  void InitializeTextureAxes(TextureAlignment align, uint initTexFlags);
  void CalcBounds(bool full);
  void GetBoundsSize(Vector&out size);
  void TransMove(const Vector&in delta);
  void TransRotate(const Vector&in refPoint, const QAngle&in angle);
  void TransScale(const Vector&in refPoint, const Vector&in scale);
  CMapClass@ opImplCast();
}
```

## `Material`

```as
class Material
{
}
```

## `Render`

```as
class Render
{
  void BeginLocalTransfrom(const VMatrix&in, bool transform);
  void EndLocalTransfrom();
  void SetTextColor(uint8 r, uint8 g, uint8 b, uint8 a);
  void SetDrawColor(uint8 r, uint8 g, uint8 b);
  void SetDrawColor(const Color&in color);
  void GetDrawColor(Color&out color);
  void BindMaterial(Material@ material);
  void PushRenderMode(RenderMode mode);
  void PopRenderMode();
  void DrawLine(const Vector&in start, const Vector&in end);
  void DrawBoxExt(const Vector&in center, float extend, bool fill);
  void DrawPlane(const Vector&in p0, const Vector&in p1, const Vector&in p2, const Vector&in p3, bool fill);
  void RenderWireframeBox(const Vector&in mins, const Vector&in maxs, uint8 r, uint8 g, uint8 b);
  void RenderBox(const Vector&in mins, const Vector&in maxs, uint8 r, uint8 g, uint8 b);
  void RenderArrow(const Vector&in start, const Vector&in end, uint8 r, uint8 g, uint8 b);
  void RenderCone(const Vector&in base, const Vector&in tip, float radius, int slices, uint8 r, uint8 g, uint8 b);
  void RenderSphere(const Vector&in center, float radius, int theta, int phi, uint8 r, uint8 g, uint8 b);
  void RenderWireframeSphere(const Vector&in center, float radius, int theta, int phi, uint8 r, uint8 g, uint8 b);
  const bool lightingPreview;
  const float gridDistance;
  const float gridSize;
  const bool inLocalTransformMode;
}
```

## `ScriptSolid`

```as
interface ScriptSolid
{
  GUIData[]@ GetGuiData() const;
  void GuiUpdated(const dictionary@ dict);
  CMapClass@ CreateMapSolid(const BoundBox@ box, TextureAlignment align);
  void DrawPreview(Render@ render, const BoundBox@ box);
}
```

## `array<class T>`

```as
class array<class T>
{
  T[]@ array(int&in);
  T[]@ array(int&in, uint length);
  T[]@ array(int&in, uint length, const T&in value);
  T[]@ $list(int&in type, int&in list) { repeat T };
  T& operator[](uint index);
  const T& operator[](uint index) const;
  T[]& operator=(const T[]&in);
  void insertAt(uint index, const T&in value);
  void insertAt(uint index, const T[]&inout arr);
  void insertLast(const T&in value);
  void removeAt(uint index);
  void removeLast();
  void removeRange(uint start, uint count);
  uint length() const;
  void reserve(uint length);
  void resize(uint length);
  void sortAsc();
  void sortAsc(uint startAt, uint count);
  void sortDesc();
  void sortDesc(uint startAt, uint count);
  void reverse();
  int find(const T&in value) const;
  int find(uint startAt, const T&in value) const;
  int findByRef(const T&in value) const;
  int findByRef(uint startAt, const T&in value) const;
  bool operator==(const T[]&in) const;
  bool isEmpty() const;
  void sort(array::less&in, uint startAt = 0, uint count = uint ( - 1 ));
  callback bool less(const T&in a, const T&in b);
}
```

## `dictionary`

```as
class dictionary
{
  dictionary@ dictionary();
  dictionary@ $list(int&in) { repeat { string, ? } };
  dictionary& operator=(const dictionary&in);
  void set(const string&in, const ?&in);
  bool get(const string&in, ?&out) const;
  void set(const string&in, const int64&in);
  bool get(const string&in, int64&out) const;
  void set(const string&in, const double&in);
  bool get(const string&in, double&out) const;
  bool exists(const string&in) const;
  bool isEmpty() const;
  uint getSize() const;
  bool delete(const string&in);
  void deleteAll();
  string[]@ getKeys() const;
  dictionaryValue& operator[](const string&in);
  const dictionaryValue& operator[](const string&in) const;
}
```

## `grid<class T>`

```as
class grid<class T>
{
  grid<T>@ grid(int&in);
  grid<T>@ grid(int&in, uint, uint);
  grid<T>@ grid(int&in, uint, uint, const T&in);
  grid<T>@ $list(int&in type, int&in list) { repeat { repeat_same T } };
  T& operator[](uint, uint);
  const T& operator[](uint, uint) const;
  void resize(uint width, uint height);
  uint width() const;
  uint height() const;
}
```
