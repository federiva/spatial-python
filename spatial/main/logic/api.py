import requests

def get_flights_from_bound(lat_min, lon_min, lat_max, lon_max) -> list:
  url = f'https://opensky-network.org/api/states/all?lamin={lon_min}&lomin={lat_min}&lamax={lon_max}&lomax={lat_max}'
  response = requests.get(url)
  points_lon_lat = None
  response_json = response.json()
  states = response_json.get('states')
  if (states):
    # Remove planes in the ground
    states = list(filter(lambda x: x[8] is False, states))
    points_lon_lat = [[(x[6], x[5])] for x in states]
  return points_lon_lat
