from django.db import models

# Create your models here.

########url######

class freq(models.Model):
    ulink=models.URLField()

    class Meta:
        _db_table='url'