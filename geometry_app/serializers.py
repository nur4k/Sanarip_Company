from rest_framework import serializers

from geometry_app.models import Region, District, Canton, Contour


class RegionSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'title', 'geometry')


class DistrictSerialzier(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('id', 'title', 'geometry', 'region')


class CantonSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Canton
        fields = ('id', 'title', 'geometry', 'dictrit')


class ContourSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Contour
        fields = ('id', 'geometry', 'canton')
