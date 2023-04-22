
from django.db import models

from ..Models.DentistModels import Dentist
from ..Models.MedicationModels import Medication


class MedicationDentist(models.Model):
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    dentist = models.ForeignKey(Dentist, on_delete=models.CASCADE)
    prescription_date = models.CharField(max_length=10)
    diagnostic = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.medication}--{self.dentist}"
