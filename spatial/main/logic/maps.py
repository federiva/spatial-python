from geopandas.geoseries import GeoSeries
from shapely.geometry import Polygon

def get_polygon(points: list) -> GeoSeries:
  """Gets a polygon

  Args:
      points (list): A list of lon-lat points

  Returns:
      GeoSeries: A polygon
  """
  return GeoSeries(Polygon([(float(x[0]), float(x[1])) for x in points]))

def get_buffered_polygon(polygon: GeoSeries, buffer: float = 1) -> GeoSeries:
  """Gets a buffered polygon

  Args:
      polygon (GeoSeries): Input polygon
      buffer (float, optional): How much the buffer should be. Defaults to 1.

  Returns:
      Geoseries: A buffered polygon
  """
  assert(buffer > 0)
  buffered_polygon = polygon.buffer(buffer)
  while buffered_polygon.geom_type[0] == "MultiPolygon":
    buffer = buffer + 0.5
    buffered_polygon = polygon.buffer(buffer)
  return buffered_polygon


def get_polygon_coordinates(polygon: GeoSeries) -> list:
  return list(polygon.exterior[0].coords)

def get_buffered_polygon_from_points(points: list) -> list:
  polygon = get_polygon(points)
  buffered_polygon = get_buffered_polygon(polygon)
  return get_polygon_coordinates(buffered_polygon)

def get_bounding_box(points: list) -> list:
  lon = [float(x[0]) for x in points]
  lat = [float(x[1]) for x in points]
  lon_min, lon_max = min(lon), max(lon)
  lat_min, lat_max = min(lat), max(lat)
  bound = [[lon_max, lat_max], [lon_min, lat_min]]
  return lat_min, lon_min, lat_max, lon_max, bound
