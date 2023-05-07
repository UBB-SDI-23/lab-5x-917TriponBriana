
from django.db import models

from ..Models.PatientModels import Patient
from rest_framework.exceptions import ValidationError


class Consultation(models.Model):
    def clean(self):
        if self.consultation_price < 0:
            raise ValidationError(
                'The consultation price cannot be a negative number!')

    consultation_type = models.CharField(max_length=50)
    consultation_price = models.IntegerField()
    consultation_duration = models.IntegerField()
    consultation_date = models.CharField(max_length=10)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.consultation_type}"

    class Meta:
        ordering = ['id']
        indexes = [models.Index(fields=["patient"])]
