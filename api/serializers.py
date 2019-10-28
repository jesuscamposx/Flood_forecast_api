from rest_framework import serializers
from api.models import Sensor, Measure

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['idSensor', 'activated', 'created', 'latitude','altitude']

class MeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measure
        fields = ['idMeasure', 'sensor', 'created', 'water_level']