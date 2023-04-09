from django.db.models import Avg, Count, OuterRef
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ..models import Patient, Dentist, Consultation, Medication, MedicationDentist
from ..serializer import PatientSerializer, DentistSerializer, ConsultationSerializer, MedicationSerializer, \
    MedicationDentistSerializer, PatientIdSerializer
from rest_framework import generics


class MedicationDetail(generics.ListAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer

    def get(self, request):
        obj = Medication.objects.all()
        serializer = MedicationSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MedicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class MedicationInfo(generics.ListAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer

    def get(self, request, id):
        try:
            obj = Medication.objects.get(id=id)
        except Medication.DoesNotExist:
            msg = {"msg": "Not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = MedicationSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        try:
            obj = Medication.objects.get(id=id)
        except Medication.DoesNotExist:
            msg = {"msg": "Not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = MedicationSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        try:
            obj = Medication.objects.get(id=id)
        except Medication.DoesNotExist:
            msg = {"msg": "Not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = MedicationSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            obj = Medication.objects.get(id=id)
        except Medication.DoesNotExist:
            msg = {"msg": "Not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response({"msg" : "Deleted"}, status=status.HTTP_204_NO_CONTENT)


class MedicationByAvgDentistAge(generics.ListAPIView):
    serializer_class = MedicationSerializer

    def get_queryset(self):
        query = Medication.objects.annotate(avg_age=Avg('medicationdentist__dentist__dentist_age')).order_by('avg_age')
        print(query.query)

        return query


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