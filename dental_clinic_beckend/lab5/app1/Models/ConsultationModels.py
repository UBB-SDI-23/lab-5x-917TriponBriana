
from django.db import models

from ..Models.PatientModels import Patient


class Consultation(models.Model):
    consultation_type = models.CharField(max_length=50)
    consultation_price = models.IntegerField()
    consultation_duration = models.IntegerField()
    consultation_date = models.CharField(max_length=10)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.consultation_type}"
