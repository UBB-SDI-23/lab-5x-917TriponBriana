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


class MedicationByNumberOfOtherDentistsPrescribed(generics.ListAPIView):
    serializer_class = MedicationSerializer

    def get_queryset(self):
        query = Medication.objects.annotate(
            number_other_dentists=Count(
                Dentist.med.through.objects.filter(
                    medication_id=OuterRef('pk')
                ).exclude(
                    dentist_id=OuterRef('dentist__id')
                ).values('dentist_id').distinct(),
                distinct=True
            )
        ).order_by('-number_other_dentists')[:3]

        print(query.query)

        return query
