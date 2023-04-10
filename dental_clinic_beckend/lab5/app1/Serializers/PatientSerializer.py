from rest_framework import serializers

from ..Models.PatientModels import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"


class PatientIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ["id"]
