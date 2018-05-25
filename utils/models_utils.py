from django.contrib.gis.db import models
from utils.date_utils import date2milis


class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def to_dict_json(self):
        object_dicj = {}
        for field in self.__class__._meta.concrete_fields:
            isfk = isinstance(field, models.ForeignKey)
            propname = field.name + '_id' if isfk else field.name
            valor = getattr(self, propname)
            if valor is None:
                object_dicj[propname] = None
                continue
            if isinstance(field, models.DateTimeField):
                object_dicj[propname] = date2milis(valor) if valor else None
            elif isinstance(field, models.DateField):
                object_dicj[propname] = valor.strftime('%d/%m/%Y') if valor else None
            elif isinstance(field, models.ImageField):
                object_dicj[propname] = str(valor)
            else:
                object_dicj[propname] = valor
        return object_dicj