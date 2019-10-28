from api.models import Measure
from api.serializers import MeasureSerializer
from django.http import Http404
from rest_framework .views import APIView
from rest_framework.response import Response
from rest_framework import status

class MeasureList(APIView):
    def get(self, request, format = None):
        measures = Measure.objects.all()
        serializer = MeasureSerializer(measures, many=True)
        return Response(serializer.data)

class MeasureSave(APIView):
    def post(self, request, format = None):
        serializer = MeasureSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class MeasureById(APIView):

    def get_object(self, pk):
        try:
            return Measure.objects.get(pk=pk)
        except Measure.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        measure = self.get_object(pk)
        serializer = MeasureSerializer(measure)
        return Response(serializer.data)

class MeasureUpdate(APIView):

    def get_object(self, pk):
        try:
            return Measure.objects.get(pk=pk)
        except Measure.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        measure = self.get_object(pk)
        serializer = MeasureSerializer(measure, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MeasureDelete(APIView):

    def get_object(self, pk):
        try:
            return Measure.objects.get(pk=pk)
        except Measure.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        measure = self.get_object(pk)
        measure.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MeasuresBySensor(APIView):

    def get_object(self, fk):
        try:
            return Measure.objects.filter(sensor=fk)
        except Measure.DoesNotExist:
            raise Http404

    def get(self, request, fk, format=None):
        measures = self.get_object(fk)
        serializer = MeasureSerializer(measures, many=True)
        return Response(serializer.data)