from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import sensorview, measureview

urlpatterns = [
    #----------------Sensor----------------------------------
    path('sensor/getSensors', sensorview.SensorList.as_view()),
    path('sensor/createSensor', sensorview.SensorSave.as_view()),
    path('sensor/getSensor/<int:pk>', sensorview.SensorById.as_view()),
    path('sensor/updateSensor/<int:pk>', sensorview.SensorUpdate.as_view()),
    path('sensor/deleteSensor/<int:pk>', sensorview.SensorDelete.as_view()),
    
    #----------------Measure----------------------------------
    path('measure/getMeasures', measureview.MeasureList.as_view()),
    path('measure/createMeasure', measureview.MeasureSave.as_view()),
    path('measure/getMeasure/<int:pk>', measureview.MeasureById.as_view()),
    path('measure/getMeasures/<int:fk>', measureview.MeasuresBySensor.as_view()),
    path('measure/updateMeasure/<int:pk>', measureview.MeasureUpdate.as_view()),
    path('measure/deleteMeasure/<int:pk>', measureview.MeasureDelete.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)