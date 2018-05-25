from django.contrib import admin
from mountains.models import Mountain
from utils.admin_utils import RawIdAdminModel


admin.site.register(Mountain, RawIdAdminModel)
