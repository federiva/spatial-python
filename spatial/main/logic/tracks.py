from main.models import Animal
from django.core.serializers import serialize
from main.logic.maps import get_buffered_polygon_from_points

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
  serialized_data = serialize('json', query)
  return {
    'data': serialized_data,
    'location': location,
    'polygon': polygon
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
