from django.shortcuts import render
from django.http import JsonResponse
from main.logic.tracks import get_individuals, get_data_from_individual


def render_map(request):
  data = get_individuals()
  return render(request, 'map.html', data)

def get_individual_data(request):
  if request.method == 'GET':
    individual = request.GET.get('individual')
    data = get_data_from_individual(individual)
    return JsonResponse(data)
  else:
    return
