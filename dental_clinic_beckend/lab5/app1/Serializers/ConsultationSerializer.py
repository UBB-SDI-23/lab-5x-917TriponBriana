from rest_framework import serializers

from ..Models.ConsultationModels import Consultation
from ..Serializers.PatientSerializer import PatientSerializer


class ConsultationSerializer(serializers.ModelSerializer):
    patients = PatientSerializer(many=True, read_only=True)

    class Meta:
        model = Consultation
        fields = ('id', 'consultation_type', 'consultation_price', 'consultation_duration', 'consultation_date', 'patient', 'patients')
        # fields = "__all__"
