
from django.db import models

from ..Models.DentistModels import Dentist


class Medication(models.Model):
    med_name = models.CharField(max_length=50)
    med_active_subst = models.CharField(max_length=50)
    med_price = models.IntegerField()
    med_expiration_date = models.CharField(max_length=10)
    med_usage = models.CharField(max_length=50)
    dent = models.ManyToManyField(Dentist, through='MedicationDentist')

    def __str__(self):
        return f"{self.med_name}"
