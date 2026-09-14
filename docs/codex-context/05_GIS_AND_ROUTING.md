# GIS, Flood Mapping and Evacuation Routing

## Stack
- GeoPandas
- Rasterio
- Shapely
- PyProj
- OSMnx
- NetworkX
- PySheds or WhiteboxTools where useful

## DEM preprocessing
```text
DEM -> local metric CRS -> fill depressions -> flow direction
 -> flow accumulation -> stream extraction -> catchment/terrain features
```

Do this offline for a defined demo corridor. Do not perform heavy raster hydrology per request.

## Coordinate systems
Use WGS84/EPSG:4326 for API geometries where appropriate. Use a suitable projected CRS for distance/area calculations.

## Flood/risk layer MVP
A terrain/rainfall-derived risk grid or thresholded impact polygons are sufficient for the prototype. A full hydrodynamic simulation is out of scope.

## Routing
Represent roads/paths as a NetworkX graph. Each edge can contain:
- distance
- estimated travel time
- slope/elevation metadata
- flood status
- closure status
- hazard penalty

Normal routing minimizes travel cost. Emergency routing first excludes unsafe edges, then minimizes a safe cost function. Always provide a reason when a route is unavailable.

## Demo data
Use compact GeoJSON and graph fixtures. The exact corridor is configurable. Never claim the fixture is a live operational map.
