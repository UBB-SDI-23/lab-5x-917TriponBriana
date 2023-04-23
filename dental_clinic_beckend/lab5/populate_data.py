import os
import random

import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lab5.settings')
django.setup()

from app1.Models.PatientModels import Patient


# if __name__ == '__main__':
#     from faker import Faker
#
#     fake = Faker()
#     n = 10000
#     for _ in range(n):
#         Patient.objects.create(patient_first_name=fake.patient_first_name(), patient_last_name=fake.patient_last_name(), patient_age=fake.patient_age(), patient_country=fake.patient_country(), patient_consultation=fake.patient_consultation())

if __name__ == '__main__':
    from faker import Faker

    fake = Faker()
    n = 1000000
    with open('populate_patient.csv', 'w') as f:
        # f.write('INSERT INTO patient(patient_first_name, patient_last_name, patient_age, patient_country, patient_consultation) VALUES \n')
        for i in range(n):
            f.write("'" + fake.name() + "'," + fake.name() + "'," + random.randint(2, 100).__str__() + ",'" + fake.name() + ",'" + fake.name() + '\n')
            print(i, "/", n)