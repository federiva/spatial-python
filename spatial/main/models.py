from django.db import models

class Animal(models.Model):
  """Model for tracking animals"""
  event_id = models.BigIntegerField(null=False)
  timestamp = models.DateTimeField(max_length=200)
  location_long = models.CharField(max_length=200)
  location_lat = models.CharField(max_length=200)
  individual_taxon_canonical_name = models.CharField(max_length=200)
  tag_local_identifier = models.CharField(max_length=200)
  individual_local_identifier = models.CharField(max_length=200)
