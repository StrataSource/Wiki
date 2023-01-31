---
layout: default
title: BSP v25 Format
parent: Reference
---

# BSP Version 25

Bsp v25 is Chaos Engine's modified BSP format that raises many of the baked-in limits that BSP traditionally has.
Version 25 was selected to avoid collisions with other projects that are also modifying the BSP map format.

This document goes over the significant changes to the format so non-Chaos devs can parse and analyze our maps.

BSP v25 is extremely new right now and is subject to change. Until these changes are finalized and merged into our
primary development branch, this format may change **without** a BSP or lump version increase.

## Map Bounds

`MAX_COORD_INTEGER` was changed to `65536` (from 16k), making the world a max of `131072` units on any axis, spanning from -65k to 65k.

## Limit Summary

| Limit Name | Value |
|---|---|
| `MAX_BRUSH_LIGHTMAP_DIM_INCLUDING_BORDER` |	131 |
| `MAX_BRUSH_LIGHTMAP_DIM_WITHOUT_BORDER` | `( MAX_BRUSH_LIGHTMAP_DIM_INCLUDING_BORDER - 3 )` |
| `MAX_DISP_LIGHTMAP_DIM_INCLUDING_BORDER` |	512 |
| `MAX_DISP_LIGHTMAP_DIM_WITHOUT_BORDER` | `( MAX_DISP_LIGHTMAP_DIM_INCLUDING_BORDER - 3 )` |
| `MAX_LIGHTMAP_DIM_WITHOUT_BORDER` |		MAX_DISP_LIGHTMAP_DIM_WITHOUT_BORDER |
| `MAX_LIGHTMAP_DIM_INCLUDING_BORDER` |	MAX_DISP_LIGHTMAP_DIM_INCLUDING_BORDER |
| `MAX_LIGHTSTYLES` |	64 |
| `MIN_MAP_DISP_POWER` |		2 |
| `MAX_MAP_DISP_POWER` |		4 |
| `MAX_DISP_CORNER_NEIGHBORS` |	4 |
| `MAX_MAP_MODELS` |					65536 |
| `MAX_MAP_BRUSHES` |					131072 |
| `MAX_MAP_ENTITIES` |				20480 (bumped from 16384) |
| `MAX_MAP_TEXDATA` |					16384 (bumped from 2048) |
| `MAX_MAP_DISPINFO` |				262144 |
| `MAX_MAP_DISP_VERTS` |				`( MAX_MAP_DISPINFO * ((1<<MAX_MAP_DISP_POWER)+1) * ((1<<MAX_MAP_DISP_POWER)+1) )` |
| `MAX_MAP_DISP_TRIS` |				`( (1 << MAX_MAP_DISP_POWER) * (1 << MAX_MAP_DISP_POWER) * 2 )` |
| `MAX_DISPVERTS` |					`NUM_DISP_POWER_VERTS( MAX_MAP_DISP_POWER )` |
| `MAX_DISPTRIS` |					`NUM_DISP_POWER_TRIS( MAX_MAP_DISP_POWER )` |
| `MAX_MAP_AREAS` |					65536 |
| `MAX_MAP_AREA_BYTES` |				`(MAX_MAP_AREAS/8)` |
| `MAX_MAP_AREAPORTALS` |				65536 |
| `MAX_MAP_PLANES` |					1048576 |
| `MAX_MAP_NODES` |					1048576 |
| `MAX_MAP_BRUSHSIDES` |				`(MAX_MAP_BRUSHES * 10)` (used to be fixed at 65536) |
| `MAX_MAP_LEAFS` |					1048576 |
| `MAX_MAP_VERTS` |					1048576 |
| `MAX_MAP_VERTNORMALS` |				1048576 |
| `MAX_MAP_VERTNORMALINDICES` |		1048576 |
| `MAX_MAP_FACES` |					1048576 |
| `MAX_MAP_LEAFFACES` |				1048576 |
| `MAX_MAP_LEAFBRUSHES` | 			1048576 |
| `MAX_MAP_PORTALS` |					1048576 |
| `MAX_MAP_CLUSTERS` |				1048576 |
| `MAX_MAP_LEAFWATERDATA` |			32768 |
| `MAX_MAP_PORTALVERTS` |				128000 |
| `MAX_MAP_EDGES` |					4096000 |
| `MAX_MAP_SURFEDGES` |				8192000 |
| `MAX_MAP_LIGHTING` |				`0x1000000` |
| `MAX_MAP_VISIBILITY` |				`0x1000000` |
| `MAX_MAP_TEXTURES` |				16384 |
| `MAX_MAP_CUBEMAPSAMPLES` |			16384 |
| `MAX_MAP_OVERLAYS` |				16384 |
| `MAX_MAP_WATEROVERLAYS` |			16384 |
| `MAX_MAP_TEXDATA_STRING_DATA` |		256000 |
| `MAX_MAP_TEXDATA_STRING_TABLE` |	1048576 |
| `MAX_MAP_PRIMITIVES` |				1048576 |
| `MAX_MAP_PRIMVERTS` |				1048576 |
| `MAX_MAP_PRIMINDICES` |				1048576 |

## New Lump Versions

The following table lists current lump versions for all lumps that are versioned in Chaos:

| Lump Name | Version |
|---|---|
| `LUMP_PHYSDISP_VERSION` | 2 |
| `LUMP_NODES_VERSION` | 1 |
| `LUMP_DISPINFO_VERSION` | 1 |
| `LUMP_EDGES_VERSION` | 1 |
| `LUMP_PRIMITIVES_VERSION` | 1 |
| `LUMP_FACES_VERSION` | 2 |
| `LUMP_FACEBRUSHES_VERSION` | 1 |
| `LUMP_FACEBRUSHLIST_VERSION` | 1 |
| `LUMP_LEAF_AMBIENT_INDEX_VERSION` | 1 |
| `LUMP_LEAFS_VERSION` | 2 |
| `LUMP_BRUSHSIDES_VERSION` | 1 |
| `LUMP_AREAPORTALS_VERSION` | 1 |
| `LUMP_LEAFFACES_VERSION` | 1 |
| `LUMP_LEAFBRUSHES_VERSION` | 1 |
| `LUMP_PRIMINDICES_VERSION` | 1 |
| `LUMP_VERTNORMALINDICES_VERSION` | 1 |
| `LUMP_OVERLAYS_VERSION` | 1 |
| `LUMP_WATEROVERLAYS_VERSION` | 1 |
| `LUMP_LEAFWATERDATA_VERSION` | 1  |

## Structures

In the BSP v25 update, all lumps listed in the lump version table have been modified. 
This section lists the new structure format for each of those lumps.

```cpp
struct dphysdisp_t
{
	unsigned int numDisplacements;
	//unsigned int dataSize[numDisplacements]; // Note that the array that follows this is using unsigned int
};

struct dnode_t
{
	int				planenum;
	int				children[2];
	float			mins[3];
	float			maxs[3];
	unsigned int	firstface;
	unsigned int	numfaces;
	short			area;
};

struct DispSubNeighbor_t
{
	unsigned int neighbor;
	unsigned char neighborOrient;
	unsigned char span;
	unsigned char neighborSpan;
};

struct DispNeighbor_t
{
	DispSubNeighbor_t neighbors[2];
};

struct DispCornerNeighbors_t
{
	unsigned int neighbors[4];
	unsigned char neighborCount;
};

class ddispinfo_t
{
	Vector		startPosition;
	int			m_iDispVertStart;
	int			m_iDispTriStart;
    int         power;
    int         minTess;
    float       smoothingAngle;
    int         contents;
	unsigned int	m_iMapFace;
	int			m_iLightmapAlphaStart;
	int			m_iLightmapSamplePositionStart;
	
	DispNeighbor_t			m_EdgeNeighbors[4];
	DispCornerNeighbors_t	m_CornerNeighbors[4];

	enum unnamed { ALLOWEDVERTS_SIZE = 10 };
	unsigned int	m_AllowedVerts[ALLOWEDVERTS_SIZE];
};

struct dedge_t
{
	unsigned int	v[2];
};

struct dprimitive_t
{
	unsigned char	type;
	unsigned int	firstIndex;
	unsigned int	indexCount;
	unsigned int	firstVert;
	unsigned int	vertCount;
};

struct dface_t
{
	unsigned int	planenum;
	byte		side;
	byte		onNode;
	int			firstedge;
	int			numedges;
	int			texinfo;
	int		dispinfo;
	int		surfaceFogVolumeID;
	byte		styles[MAXLIGHTMAPS];
	int			lightofs;
    float       area;
	int			m_LightmapTextureMinsInLuxels[2];
	int			m_LightmapTextureSizeInLuxels[2];
	int origFace;
	unsigned int m_EnableShadows : 1;
	unsigned int m_NumPrims : 31;
	unsigned int	firstPrimID;
	unsigned int	smoothingGroups;
};

struct dfaceid_t
{
	unsigned int	hammerfaceid;
};

struct dfacebrushlist_t
{
	unsigned int	m_nFaceBrushCount;
	unsigned int	m_nFaceBrushStart;
};

struct dleaf_t
{
	int				contents;
	int				cluster;
	BEGIN_BITFIELD( bf );
	int				area:17;
	int				flags:15;
	END_BITFIELD();
	float			mins[3];
	float			maxs[3];
	unsigned int	firstleafface;
	unsigned int	numleaffaces;
	unsigned int	firstleafbrush;
	unsigned int	numleafbrushes;
	int				leafWaterDataID;
};

struct dleafambientindex_t
{
	unsigned int ambientSampleCount;
	unsigned int firstAmbientSample;
};

struct dbrushside_t
{
	unsigned int	planenum;
	int				texinfo;
	int				dispinfo;
	byte			bevel;
	byte			thin;
};

struct dareaportal_t
{
	unsigned int	m_PortalKey;
	unsigned int	otherarea;
	unsigned int	m_FirstClipPortalVert;
	unsigned int	m_nClipPortalVerts;
	int				planenum;
};

struct dleafwaterdata_t
{
	float	surfaceZ;
	float	minZ;
	int		surfaceTexInfoID;
};

#define OVERLAY_BSP_FACE_COUNT	64
struct doverlay_t
{
	int			nId;
	int			nTexInfo;
	unsigned short	m_nFaceCountAndRenderOrder;
	int			aFaces[OVERLAY_BSP_FACE_COUNT];
	float		flU[2];
	float		flV[2];
	Vector		vecUVPoints[4];
	Vector		vecOrigin;
	Vector		vecBasisNormal;
};

#define WATEROVERLAY_BSP_FACE_COUNT				256
struct dwateroverlay_t
{
	int				nId;
	int				nTexInfo;
	unsigned short	m_nFaceCountAndRenderOrder;
	int				aFaces[WATEROVERLAY_BSP_FACE_COUNT];
	float			flU[2];
	float			flV[2];
	Vector			vecUVPoints[4];
	Vector			vecOrigin;
	Vector			vecBasisNormal;
};
```
