
from django.db import models


# Create your models here.


class Patient(models.Model):
    patient_first_name = models.CharField(max_length=50)
    patient_last_name = models.CharField(max_length=50)
    patient_age = models.IntegerField()
    patient_country = models.CharField(max_length=50)
    patient_consultation = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.patient_first_name}"
