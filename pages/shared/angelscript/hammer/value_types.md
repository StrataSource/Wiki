---
title: Value Types
---

# Value Types

This page outlines the various Strata Hammer AngelScript value types.

## `CMapFace`

```as
class CMapFace
{
  CMapFace();
  ~CMapFace();
  void CreateFace(Vector[]@ points, int numPoints);
}
```

## `Color`

```as
class Color
{
  Color();
  Color(uint8 r, uint8 g, uint8 b);
  Color(uint8 r, uint8 g, uint8 b, uint8 a);
  void SetColor(uint8 r, uint8 g, uint8 b, uint8 a);
  void GetColor(uint8&out r, uint8&out g, uint8&out b, uint8&out a) const;
  uint8& operator[](int idx);
  uint8& operator[](int idx) const;
  uint8 r;
  uint8 g;
  uint8 b;
  uint8 a;
  uint raw;
}
```

## `GUIData`

```as
class GUIData
{
  GUIData(GuiElement type, const string&in label, int64 defVal);
  GUIData(GuiElement type, const string&in label, double defVal);
  GUIData(GuiElement type, const string&in text);
  GUIData(GuiElement type);
}
```

## `MeshBuilder`

```as
class MeshBuilder
{
  MeshBuilder();
  ~MeshBuilder();
  void Position(const Vector&in pos);
  void Normal(const Vector&in normal);
  void Color(uint8 r, uint8 g, uint8 b, uint8 a);
  void TexCoord(int i, float u, float v);
  void TexCoord(int i, const Vector2D&in uv);
  void AdvanceVertex();
  void Index(uint16 index);
  void FastIndex2(uint16 index1, uint16 index2);
  void AdvanceIndex();
  void Start(const string&in material, PrimitiveType type, int primitiveCount);
  void Start(const string&in material, PrimitiveType, int vertexCount, int indexCount);
  void Draw();
}
```

## `QAngle`

```as
class QAngle
{
  QAngle();
  QAngle(float x, float y, float z);
  void Init(float x, float y, float z);
  void Random(float minVal, float maxVal);
  bool IsValid() const;
  void Invalidate();
  float Length() const;
  float LengthSqr() const;
  float operator[](int idx) const;
  float& operator[](int idx);
  bool operator==(const QAngle&in other) const;
  QAngle& operator=(const QAngle&in other);
  QAngle& operator+=(const QAngle&in other);
  QAngle& operator-=(const QAngle&in other);
  QAngle& operator*=(float fl);
  QAngle& operator/=(float fl);
  QAngle operator-() const;
  QAngle operator+(const QAngle&in other) const;
  QAngle operator-(const QAngle&in other) const;
  QAngle operator*(float fl) const;
  QAngle operator/(float fl) const;
  float x;
  float y;
  float z;
}
```

## `VMatrix`

```as
class VMatrix
{
  VMatrix();
  VMatrix(float m00, float m01, float m02, float m03, float m10, float m11, float m12, float m13, float m20, float m21, float m22, float m23, float m30, float m31, float m32, float m33);
  VMatrix(const Vector&in forward, const Vector&in left, const Vector&in up);
  void Init(float m00, float m01, float m02, float m03, float m10, float m11, float m12, float m13, float m20, float m21, float m22, float m23, float m30, float m31, float m32, float m33);
  float& operator[](uint x, uint y);
  const float& operator[](uint x, uint y) const;
  void SetLeft(const Vector&in left);
  void SetUp(const Vector&in up);
  void SetForward(const Vector&in forward);
  void GetBasisVectors(Vector&out forward, Vector&out left, Vector&out up) const;
  void SetBasisVectors(const Vector&in forward, const Vector&in left, const Vector&in up);
  void SetTranslation(const Vector&in trans);
  void PreTranslate(const Vector&in trans);
  void PostTranslate(const Vector&in trans);
  Vector GetLeft() const;
  Vector GetUp() const;
  Vector GetForward() const;
  Vector GetTranslation() const;
  Vector ApplyRotation(const Vector&in vec) const;
  Vector VMul3x3(const Vector&in vec) const;
  Vector VMul3x3Transpose(const Vector&in vec) const;
  Vector VMul4x3(const Vector&in vec) const;
  Vector VMul4x3Transpose(const Vector&in vec) const;
  void MatrixMul(const VMatrix&in vm, VMatrix&out out) const;
  void Identity();
  bool IsIdentity() const;
  void SetupMatrixOrgAngles(const Vector&in origin, const QAngle&in angles);
  bool InverseGeneral(VMatrix&out inverse) const;
  VMatrix InverseTR() const;
  bool IsRotationMatrix() const;
  Vector GetScale() const;
  VMatrix Scale(const Vector&in scale);
  VMatrix NormalizeBasisVectors() const;
  VMatrix Transpose() const;
  VMatrix Transpose3x3() const;
}
```

## `Vector`

```as
class Vector
{
  Vector();
  Vector(float x, float y, float z);
  float operator[](int idx) const;
  float& operator[](int idx);
  void Init(float x, float y, float z);
  bool IsValid() const;
  void Invalidate();
  void Random(float minVal, float maxVal);
  void Zero();
  float NormalizeInPlace();
  Vector Normalized() const;
  void Negate();
  float Length() const;
  float Length2D() const;
  float Length2DSqr() const;
  float LengthSqr() const;
  bool IsZero(float tolerance) const;
  bool IsLengthGreaterThan(float val) const;
  bool IsLengthLessThan(float val) const;
  bool WithinAABox(const Vector&in mins, const Vector&in maxs);
  float DistTo(const Vector&in other) const;
  float DistToSqr(const Vector&in other) const;
  void MulAdd(const Vector&in a, const Vector&in b, float scalar);
  float Dot(const Vector&in other) const;
  Vector Cross(const Vector&in other) const;
  Vector Min(const Vector&in other) const;
  Vector Max(const Vector&in other) const;
  const Vector2D& AsVector2D() const;
  Vector2D& AsVector2D();
  bool operator==(const Vector&in other) const;
  Vector& operator+=(const Vector&in other);
  Vector& operator+=(float fl);
  Vector& operator-=(const Vector&in other);
  Vector& operator-=(float fl);
  Vector& operator*=(const Vector&in other);
  Vector& operator*=(float fl);
  Vector& operator/=(const Vector&in other);
  Vector& operator/=(float fl);
  Vector& operator=(const Vector&in other);
  Vector operator-() const;
  Vector operator+(const Vector&in other) const;
  Vector operator-(const Vector&in other) const;
  Vector operator*(const Vector&in other) const;
  Vector operator/(const Vector&in other) const;
  Vector operator*(float fl) const;
  Vector operator/(float fl) const;
  float x;
  float y;
  float z;
}
```

## `Vector2D`

```as
class Vector2D
{
  Vector2D();
  Vector2D(float x, float y);
  Vector2D(const Vector2D&in other);
  float operator[](int idx) const;
  float& operator[](int idx);
  void Init(float x, float y);
  bool IsValid() const;
  void Random(float minVal, float maxVal);
  void Negate();
  float Length() const;
  float LengthSqr() const;
  bool IsZero(float tolerance) const;
  float NormalizeInPlace();
  bool IsLengthGreaterThan(float val) const;
  bool IsLengthLessThan(float val) const;
  float DistTo(const Vector2D&in other) const;
  float DistToSqr(const Vector2D&in other) const;
  void MulAdd(const Vector2D&in a, const Vector2D&in b, float scalar);
  float Dot(const Vector2D&in other) const;
  Vector2D Min(const Vector2D&in other) const;
  Vector2D Max(const Vector2D&in other) const;
  bool operator==(const Vector2D&in other) const;
  Vector2D& operator+=(const Vector2D&in other);
  Vector2D& operator-=(const Vector2D&in other);
  Vector2D& operator*=(const Vector2D&in other);
  Vector2D& operator*=(float fl);
  Vector2D& operator/=(const Vector2D&in other);
  Vector2D& operator/=(float fl);
  Vector2D& operator=(const Vector2D&in other);
  Vector2D operator-() const;
  Vector2D operator+(const Vector2D&in other) const;
  Vector2D operator-(const Vector2D&in other) const;
  Vector2D operator*(const Vector2D&in other) const;
  Vector2D operator/(const Vector2D&in other) const;
  Vector2D operator*(float fl) const;
  Vector2D operator/(float fl) const;
  float x;
  float y;
}
```

## `Vector4D`

```as
class Vector4D
{
  Vector4D();
  Vector4D(float x, float y, float z, float w);
  Vector4D(const Vector4D&in other);
  void Init(float x, float y, float z, float w);
  void Init(const Vector&in vec, float w);
  bool IsValid() const;
  void Negate();
  float Length() const;
  float LengthSqr() const;
  bool IsZero(float) const;
  float DistTo(const Vector4D&in other) const;
  float DistToSqr(const Vector4D&in other) const;
  void MulAdd(const Vector4D&in a, const Vector4D&in b, float scalar);
  float Dot(const Vector4D&in other) const;
  float operator[](int idx) const;
  float& operator[](int idx);
  const Vector& AsVector3D() const;
  Vector& AsVector3D();
  const Vector2D& AsVector2D() const;
  Vector2D& AsVector2D();
  void Random(float minVal, float maxVal);
  bool operator==(const Vector4D&in other) const;
  Vector4D& operator+=(const Vector4D&in other);
  Vector4D& operator-=(const Vector4D&in other);
  Vector4D& operator*=(const Vector4D&in other);
  Vector4D& operator*=(float fl);
  Vector4D& operator/=(const Vector4D&in other);
  Vector4D& operator/=(float fl);
  float x;
  float y;
  float z;
  float w;
}
```

## `dictionaryValue`

```as
class dictionaryValue
{
  dictionaryValue();
  ~dictionaryValue();
  dictionaryValue& operator=(const dictionaryValue&in);
  dictionaryValue& operator@=(const ?&in);
  dictionaryValue& operator@=(const dictionaryValue&in);
  dictionaryValue& operator=(const ?&in);
  dictionaryValue& operator=(double);
  dictionaryValue& operator=(int64);
  void opCast(?&out);
  void opConv(?&out);
  int64 opConv();
  double opConv();
}
```

## `string`

```as
{
  string();
  string(const string&in other);
  string(bool num);
  string(int num);
  string(uint num);
  string(int64 num);
  string(uint64 num);
  string(float num);
  string(double num);
  ~string();
  string& operator=(const string&in str);
  string& operator=(int64 num);
  string& operator=(uint64 num);
  string& operator=(double num);
  string& operator=(float num);
  uint8& operator[](uint idx);
  const uint8& operator[](uint idx) const;
  string& operator+=(const string&in);
  string& operator+=(int64);
  string& operator+=(uint64);
  string& operator+=(double);
  string& operator+=(float);
  string operator+(const string&in) const;
  string operator+(int64) const;
  string operator+(uint64) const;
  string opAdd_r(int64) const;
  string opAdd_r(uint64) const;
  string operator+(double) const;
  string opAdd_r(double) const;
  string operator+(float) const;
  string opAdd_r(float) const;
  bool operator==(const string&in) const;
  uint len() const;
  uint length() const;
  uint resize() const;
  bool empty() const;
  string tolower() const;
  string toupper() const;
  string trim() const;
  int64 toInt() const;
  float toFloat() const;
  uint locate(const string&in, const uint = 0) const;
  string substr(const int start, const int length) const;
  string subString(const int start, const int length) const;
  string substr(const int start) const;
  string subString(const int start) const;
  string replace(const string&in search, const string&in replace) const;
  bool isAlpha() const;
  bool isNumerical() const;
  bool isNumeric() const;
  bool isAlphaNumerical() const;
  string[]@ split(const string&in) const;
}
```
