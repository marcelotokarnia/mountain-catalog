from django.contrib.gis.db import models
from utils.models_utils import BaseModel


class Mountain(BaseModel):
  id = models.AutoField(primary_key=True)
  spot = models.PointField()
  curiosities = models.TextField(blank=True, null=True)
  province = models.CharField(max_length=128, blank=True, null=True)
  difficulty = models.CharField(max_length=128, blank=True, null=True)
  elevation = models.IntegerField(blank=True, null=True)
  name = models.CharField(max_length=128)
  country = models.CharField(max_length=128, blank=True, null=True)
  state = models.CharField(max_length=128, blank=True, null=True)
  region = models.CharField(max_length=128, blank=True, null=True)

  def __str__(self):
    return "%s: %s(%sm)-%s (%s, %s)" % (self.pk, self.name, self.elevation, self.country, self.spot.x, self.spot.y)