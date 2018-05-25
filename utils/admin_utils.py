from django.contrib import admin
from django.contrib.gis.db import models
from functools import reduce


class RawIdAdminModel(admin.ModelAdmin):
    def __init__(self, model, admin_site, *args, **kwargs):
        self.raw_id_fields = [field.name for field in model._meta.concrete_fields if self.is_fk_or_m2m(field)]
        super(RawIdAdminModel, self).__init__(model, admin_site, *args, **kwargs)

    @staticmethod
    def is_fk_or_m2m(field):
        return reduce((lambda x, y: x or isinstance(field, y)), [
            models.ForeignKey, models.OneToOneField, models.ManyToManyField], False)