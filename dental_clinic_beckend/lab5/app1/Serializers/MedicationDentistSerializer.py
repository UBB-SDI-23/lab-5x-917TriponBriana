from rest_framework import serializers

from ..Models.DentistModels import Dentist
from ..Models.MedicationModels import Medication
from ..Models.MedicationDentistModels import MedicationDentist


class MedicationDentistSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationDentist
        fields = "__all__"

    def validate_medication_id(self, value):
        filter = Medication.objects.filter(id=value)
        if not filter.exists():
            raise serializers.ValidationError("Medication does not exist!")
        return value

    def validate_dentist_id(self, value):
        filter = Dentist.objects.filter(id=value)
        if not filter.exists():
            raise serializers.ValidationError("Dentist does not exist!")
        return value

