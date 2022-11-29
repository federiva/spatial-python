import requests

def get_flights_from_bound(lat_min, lon_min, lat_max, lon_max) -> list:
  url = f'https://opensky-network.org/api/states/all?lamin={lat_min}&lomin={lon_min}&lamax={lat_max}&lomax={lon_max}'
  response = requests.get(url)
  print(url)
  points_lon_lat = None
  response_json = response.json()
  states = response_json.get('states')
  if (states):
    print(len(states))
    points_lon_lat = [[(x[5], x[6])] for x in states]
  return points_lon_lat
