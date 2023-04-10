
from django.db import models


class Dentist(models.Model):
    dentist_first_name = models.CharField(max_length=50)
    dentist_last_name = models.CharField(max_length=50)
    dentist_age = models.IntegerField()
    dentist_country = models.CharField(max_length=50)
    dentist_salary = models.IntegerField()
    med = models.ManyToManyField('Medication', through='MedicationDentist')

    def __str__(self):
        return f"{self.dentist_first_name}"