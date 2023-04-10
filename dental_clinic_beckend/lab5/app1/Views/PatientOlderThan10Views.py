from django.db.models import Avg, Count, OuterRef
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ..Models.ConsultationModels import Consultation
from ..Models.DentistModels import Dentist
from ..Models.MedicationDentistModels import MedicationDentist
from ..Models.MedicationModels import Medication
from ..Models.PatientModels import Patient
from ..Serializers.PatientSerializer import PatientSerializer
from rest_framework import generics


class PatientOlderThan18(generics.ListAPIView):
    serializer_class = PatientSerializer

    def get_queryset(self):
        query = Patient.objects.filter(patient_age__gt=18)
        print(query.query)

        return query
