from utils.models_utils import BaseModel
from django.contrib.gis.db import models
from mountains.models import Mountain
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.auth.models import User


class TextRecord(BaseModel):
    title = models.CharField(max_length=1024)
    created_by = models.ForeignKey(User, related_name="texts", on_delete=models.CASCADE)
    record = models.TextField()
    votes = models.IntegerField(default=0)
    mountain = models.ForeignKey(Mountain, related_name="texts", on_delete=models.CASCADE)


class ImageRecord(BaseModel):
    created_by = models.ForeignKey(User, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="mountain_images/")
    votes = models.IntegerField(default=0)
    mountain = models.ForeignKey(Mountain, related_name="images", on_delete=models.CASCADE)


class VideoRecord(BaseModel):
    created_by = models.ForeignKey(User, related_name="videos", on_delete=models.CASCADE)
    provider = models.CharField(max_length=1024, default="youtube")
    link = models.CharField(max_length=2048)
    votes = models.IntegerField(default=0)
    mountain = models.ForeignKey(Mountain, related_name="videos", on_delete=models.CASCADE)


class TrailRecord(BaseModel):
    created_by = models.ForeignKey(User, related_name="trail_records", on_delete=models.CASCADE)
    title = models.CharField(max_length=1024)
    votes = models.IntegerField(default=0)
    accumulated_heights = models.IntegerField()
    accumulated_depths = models.IntegerField()
    simplified_track = models.MultiLineStringField()
    mountain = models.ForeignKey(Mountain, related_name="trail_records", on_delete=models.CASCADE)

    @property
    def simplified_length(self):
        geometry = GEOSGeometry(self.simplified_track)
        geometry.transform(3857)
        return geometry.length


class TrackPoint(models.Model):
    point = models.PointField()
    time = models.DateTimeField()
    ele = models.IntegerField()
    trail_record = models.ForeignKey(TrailRecord, related_name='trackpoints', on_delete=models.CASCADE)

    def to_gpx(self):
        return '<trkpt lat="%s" lon="%s"><ele>%s</ele><time>%s</time></trkpt>' % (
            self.point.y, self.point.x, self.ele, self.time.strftime('%Y-%m-%dT%H:%M:%SZ'))


class WayPoint(models.Model):
    point = models.PointField()
    ele = models.IntegerField()
    name = models.CharField(max_length=1024)
    trail_record = models.ForeignKey(TrailRecord, related_name='waypoints', on_delete=models.CASCADE)

    def to_gpx(self):
        return '<wpt lat="%s" lon="%s"><ele>%s</ele><name>%s</name></wpt>' % (
            self.point.y, self.point.x, self.ele, self.name
        )
