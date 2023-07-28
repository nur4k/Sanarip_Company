from rest_framework import generics

from geometry_app.models import Region, District, Canton, Contour
from geometry_app.serializers import RegionSerialzier, DistrictSerialzier, CantonSerialzier, ContourSerialzier


class RegionView(generics.ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerialzier


class DistrictView(generics.ListCreateAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerialzier


class CantonView(generics.ListCreateAPIView):
    queryset = Canton.objects.all()
    serializer_class = CantonSerialzier


class ContourView(generics.ListCreateAPIView):
    queryset = Contour.objects.all()
    serializer_class = ContourSerialzier
