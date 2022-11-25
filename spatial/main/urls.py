"""API endpoints for main app"""
from django.urls import path, include
from . import views

# It contains the url belonging to the dummy api view
app_name = 'main'

urlpatterns = [
    path('', views.render_map, name='map'),
]
