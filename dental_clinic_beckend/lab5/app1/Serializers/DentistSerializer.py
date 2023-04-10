from rest_framework import serializers

from ..Models.DentistModels import Dentist


class DentistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dentist
        fields = "__all__"


class DentistIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dentist
        fields = ['id']