---
title: Example Wedge
weight: 10
---

# Example Wedge (`script_wedge.as`)

```as
[Solid("script_wedge")]
class ExampleWedge : ScriptSolid
{
  GUIData[]@ GetGuiData() const
  {
    return {};
  }

  void GuiUpdated(const dictionary@ dict)
  {
  }

  CMapClass@ CreateMapSolid( const BoundBox@ box, TextureAlignment align )
  {
    float width = (box.maxs[0] - box.mins[0]) / 2;
    float depth = (box.maxs[1] - box.mins[1]) / 2;
    float height = (box.maxs[2] - box.mins[2]) / 2;

    Vector origin;
    box.GetBoundsCenter(origin);

    CMapFace face;
    CMapSolid@ solid = CMapSolid();
    Vector[] points;
    points.resize(4);

    points[0][0] = origin[0] + width;
    points[0][1] = origin[1] + depth;
    points[0][2] = origin[2] + height;

    points[1][0] = origin[0] + width;
    points[1][1] = origin[1] - depth;
    points[1][2] = origin[2] + height;

    points[2][0] = origin[0] - width;
    points[2][1] = origin[1] - depth;
    points[2][2] = origin[2] + height;

    face.CreateFace(points, 3);
    solid.AddFace(face);

    for (int i = 0; i < 3; i++)
    {
      points[i][2] = origin[2] - height;
    }

    face.CreateFace(points, -3);
    solid.AddFace(face);

    points[0][0] = origin[0] + width;
    points[0][1] = origin[1] + depth;
    points[0][2] = origin[2] - height;

    points[1][0] = origin[0] + width;
    points[1][1] = origin[1] + depth;
    points[1][2] = origin[2] + height;

    points[2][0] = origin[0] - width;
    points[2][1] = origin[1] - depth;
    points[2][2] = origin[2] + height;

    points[3][0] = origin[0] - width;
    points[3][1] = origin[1] - depth;
    points[3][2] = origin[2] - height;

    face.CreateFace(points, 4);
    solid.AddFace(face);

    points[0][0] = origin[0] + width;
    points[0][1] = origin[1] - depth;
    points[0][2] = origin[2] + height;

    points[1][0] = origin[0] + width;
    points[1][1] = origin[1] - depth;
    points[1][2] = origin[2] - height;

    points[2][0] = origin[0] - width;
    points[2][1] = origin[1] - depth;
    points[2][2] = origin[2] - height;

    points[3][0] = origin[0] - width;
    points[3][1] = origin[1] - depth;
    points[3][2] = origin[2] + height;

    face.CreateFace(points, 4);
    solid.AddFace(face);

    points[0][0] = origin[0] + width;
    points[0][1] = origin[1] + depth;
    points[0][2] = origin[2] + height;

    points[1][0] = origin[0] + width;
    points[1][1] = origin[1] + depth;
    points[1][2] = origin[2] - height;

    points[2][0] = origin[0] + width;
    points[2][1] = origin[1] - depth;
    points[2][2] = origin[2] - height;

    points[3][0] = origin[0] + width;
    points[3][1] = origin[1] - depth;
    points[3][2] = origin[2] + height;

    face.CreateFace(points, 4);
    solid.AddFace(face);

    solid.CalcBounds(false);
    solid.InitializeTextureAxes(align, INIT_TEXTURE_ALL | INIT_TEXTURE_FORCE);

    return solid;
  }

  void DrawPreview( Render@ render, const BoundBox@ box )
  {
    float width = (box.maxs[0] - box.mins[0]) / 2;
    float depth = (box.maxs[1] - box.mins[1]) / 2;
    float height = (box.maxs[2] - box.mins[2]) / 2;
    Vector origin;
    box.GetBoundsCenter(origin);

    MeshBuilder builder;
    builder.Start(GetDefaultTextureName(), MATERIAL_QUADS, 3);

    Vector2D tc1(0, 0);
    Vector2D tc2(0, 1);
    Vector2D tc3(1, 1);
    Vector2D tc4(1, 0);

    Vector pos;

    pos.x = origin[0] + width;
    pos.y = origin[1] + depth;
    pos.z = origin[2] - height;
    builder.Position( pos );
    builder.Normal( vec3_origin );
    builder.TexCoord( 0, tc1 );
    builder.AdvanceVertex();

    pos.x = origin[0] + width;
    pos.y = origin[1] + depth;
    pos.z = origin[2] + height;
    builder.Position( pos );
    builder.Normal( vec3_origin );
    builder.TexCoord( 0, tc2 );
    builder.AdvanceVertex();

    pos.x = origin[0] - width;
    pos.y = origin[1] - depth;
    pos.z = origin[2] + height;
    builder.Position( pos );
    builder.Normal( vec3_origin );
    builder.TexCoord( 0, tc3 );
    builder.AdvanceVertex();

    pos.x = origin[0] - width;
    pos.y = origin[1] - depth;
    pos.z = origin[2] - height;
    builder.Position( pos );
    builder.Normal( vec3_origin );
    builder.TexCoord( 0, tc4 );
    builder.AdvanceVertex();

    pos.x = origin[0] + width;
    pos.y = origin[1] - depth;
    pos.z = origin[2] + height;
    builder.Position( pos );
    builder.Normal( vec3_origin );
    builder.TexCoord( 0, tc1 );
    builder.AdvanceVertex();

    pos.x = origin[0] + width;
    pos.y = origin[1] - depth;
    pos.z = origin[2] - height;
    builder.Position( pos );
    builder.Normal( vec3_origin );
    builder.TexCoord( 0, tc2 );
    builder.AdvanceVertex();

    pos.x = origin[0] - width;
    pos.y = origin[1] - depth;
    pos.z = origin[2] - height;
    builder.Position( pos );
    builder.Normal( vec3_origin );
    builder.TexCoord( 0, tc3 );
    builder.AdvanceVertex();

    pos.x = origin[0] - width;
    pos.y = origin[1] - depth;
    pos.z = origin[2] + height;
    builder.Position( pos );
    builder.Normal( vec3_origin );
    builder.TexCoord( 0, tc4 );
    builder.AdvanceVertex();

    pos.x = origin[0] + width;
    pos.y = origin[1] + depth;
    pos.z = origin[2] + height;
    builder.Position( pos );
    builder.Normal( vec3_origin );
    builder.TexCoord( 0, tc1 );
    builder.AdvanceVertex();

    pos.x = origin[0] + width;
    pos.y = origin[1] + depth;
    pos.z = origin[2] - height;
    builder.Position( pos );
    builder.Normal( vec3_origin );
    builder.TexCoord( 0, tc2 );
    builder.AdvanceVertex();

    pos.x = origin[0] + width;
    pos.y = origin[1] - depth;
    pos.z = origin[2] - height;
    builder.Position( pos );
    builder.Normal( vec3_origin );
    builder.TexCoord( 0, tc3 );
    builder.AdvanceVertex();

    pos.x = origin[0] + width;
    pos.y = origin[1] - depth;
    pos.z = origin[2] + height;
    builder.Position( pos );
    builder.Normal( vec3_origin );
    builder.TexCoord( 0, tc4 );
    builder.AdvanceVertex();

    builder.Draw();

    builder.Start(GetDefaultTextureName(), MATERIAL_TRIANGLES, 2);

    pos.x = origin[0] + width;
    pos.y = origin[1] + depth;
    pos.z = origin[2] + height;
    builder.Position( pos );
    builder.Normal( vec3_origin );
    builder.TexCoord( 0, tc1 );
    builder.AdvanceVertex();

    pos.x = origin[0] + width;
    pos.y = origin[1] - depth;
    pos.z = origin[2] + height;
    builder.Position( pos );
    builder.Normal( vec3_origin );
    builder.TexCoord( 0, tc2 );
    builder.AdvanceVertex();

    pos.x = origin[0] - width;
    pos.y = origin[1] - depth;
    pos.z = origin[2] + height;
    builder.Position( pos );
    builder.Normal( vec3_origin );
    builder.TexCoord( 0, tc3 );
    builder.AdvanceVertex();

    pos.x = origin[0] + width;
    pos.y = origin[1] + depth;
    pos.z = origin[2] - height;
    builder.Position( pos );
    builder.Normal( vec3_origin );
    builder.TexCoord( 0, tc1 );
    builder.AdvanceVertex();

    pos.x = origin[0] - width;
    pos.y = origin[1] - depth;
    pos.z = origin[2] - height;
    builder.Position( pos );
    builder.Normal( vec3_origin );
    builder.TexCoord( 0, tc3 );
    builder.AdvanceVertex();

    pos.x = origin[0] + width;
    pos.y = origin[1] - depth;
    pos.z = origin[2] - height;
    builder.Position( pos );
    builder.Normal( vec3_origin );
    builder.TexCoord( 0, tc4 );
    builder.AdvanceVertex();

    builder.Draw();
  }
};
```
