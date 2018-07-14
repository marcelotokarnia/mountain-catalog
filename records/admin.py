from django.contrib import admin
from records.models import TextRecord, ImageRecord, VideoRecord, TrailRecord, TrackPoint, WayPoint
from utils.admin_utils import RawIdAdminModel


admin.site.register(TextRecord, RawIdAdminModel)
admin.site.register(ImageRecord, RawIdAdminModel)
admin.site.register(VideoRecord, RawIdAdminModel)
admin.site.register(TrailRecord, RawIdAdminModel)
admin.site.register(TrackPoint, RawIdAdminModel)
admin.site.register(WayPoint, RawIdAdminModel)
