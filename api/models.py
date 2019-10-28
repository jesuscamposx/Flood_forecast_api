from django.db import models

class Sensor(models.Model):
    idSensor = models.AutoField(primary_key=True)
    activated = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    altitude = models.DecimalField(max_digits=9, decimal_places=6)
    class Meta:
        ordering = ['created']

class Measure(models.Model):
    idMeasure = models.AutoField(primary_key=True)
    sensor = models.ForeignKey('Sensor', on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    water_level = models.DecimalField(max_digits=6, decimal_places=3)
    class Meta: 
        ordering = ['created']

