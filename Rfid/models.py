from django.db import models
from django.utils import timezone

class Rfid(models.Model):
    identificador = models.IntegerField(null=False, default=0)
    delete = models.BooleanField(default=False)    
    create = models.DateTimeField(default=timezone.now)
    def _str_(self):
        return self.name

    class Meta:
        db_table = 'Rfid'