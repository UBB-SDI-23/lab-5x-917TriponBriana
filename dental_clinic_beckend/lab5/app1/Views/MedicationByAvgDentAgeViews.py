from django.db.models import Avg, Count, OuterRef
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ..Models.ConsultationModels import Consultation
from ..Models.DentistModels import Dentist
from ..Models.MedicationDentistModels import MedicationDentist
from ..Models.MedicationModels import Medication
from ..Models.PatientModels import Patient
from ..Serializers.MedicationSerializer import MedicationSerializer
from rest_framework import generics


class MedicationByAvgDentistAge(generics.ListAPIView):
    serializer_class = MedicationSerializer

    def get_queryset(self):
        query = Medication.objects.annotate(avg_age=Avg('medicationdentist__dentist__dentist_age')).order_by('avg_age')
        print(query.query)

        return query
