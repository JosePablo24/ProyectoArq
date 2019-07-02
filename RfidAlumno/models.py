from django.db import models
from django.utils import timezone

# Create your models here.
class Asistencia(models.Model):
    id_alumno= models.IntegerField(null=False)
    id_rfid= models.IntegerField(null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)
    
    def _str_(self):
        return self.name

    class Meta:
        db_table = 'Rfid_Alumno'