from main.models import Animal
from django.core.serializers import serialize
from main.logic.maps import get_buffered_polygon_from_points, get_bounding_box
from main.logic.api import get_flights_from_bound

def get_individuals():
  query = list(
    set(
      Animal.objects.values_list('individual_local_identifier', flat=True)
    )
  )
  return {'individuals': query}

def get_data_from_individual(individual: str) -> dict:
  query = Animal.objects.filter(individual_local_identifier = individual)
  location = __get_location_from_data(query.values())
  polygon = __get_buffered_polygon(query)
  lat_min, lon_min, lat_max, lon_max, bounding_box = get_bounding_box([[x.location_lat, x.location_long] for x in query])
  flights = get_flights_from_bound(lat_min, lon_min, lat_max, lon_max)
  print(flights)
  serialized_data = serialize('json', query)
  return {
    'data': serialized_data,
    'location': location,
    'bounding_box': bounding_box,
    'flights': flights
  }

def __get_location_from_data(data: list) -> dict:
  long = [x.get('location_long') for x in data]
  lat = [x.get('location_lat') for x in data]
  return {
    'min_lat': min(lat),
    'max_lat': max(lat),
    'min_lon': min(long),
    'max_lon': max(long),
  }

def __get_buffered_polygon(query):
  points = [[x.location_lat, x.location_long] for x in query]
  buffered_polygon_coords = get_buffered_polygon_from_points(points)
  return buffered_polygon_coords
