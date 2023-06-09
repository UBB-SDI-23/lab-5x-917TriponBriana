from django.db.models import Avg, Count, OuterRef
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ..Models.ConsultationModels import Consultation
from ..Models.DentistModels import Dentist
from ..Models.MedicationDentistModels import MedicationDentist
from ..Models.MedicationModels import Medication
from ..Models.PatientModels import Patient
from ..Serializers.PatientSerializer import PatientSerializer, PatientIdSerializer
from rest_framework import generics
from rest_framework import generics


class PatientIds(APIView):
    def get(self, request):
        obj = Patient.objects.all()
        serializer = PatientIdSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
