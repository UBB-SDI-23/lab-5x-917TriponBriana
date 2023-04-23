# import os
# import random
#
# import django
#
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lab5.settings')
# django.setup()
#
# from app1.Models.PatientModels import Patient
#
#
# if __name__ == '__main__':
#     from faker import Faker
#
#     fake = Faker()
#     n = 10000
#     for _ in range(n):
#         Patient.objects.create(patient_first_name=fake.patient_first_name(), patient_last_name=fake.patient_last_name(), patient_age=fake.patient_age(), patient_country=fake.patient_country(), patient_consultation=fake.patient_consultation())

# if __name__ == '__main__':
#     from faker import Faker
#
#     fake = Faker()
#     n = 1000000
#     with open('populate_patient.csv', 'w') as f:
#         # f.write('INSERT INTO patient(patient_first_name, patient_last_name, patient_age, patient_country, patient_consultation) VALUES \n')
#         for i in range(n):
#             f.write("'" + fake.name() + "'," + fake.name() + "'," + random.randint(2, 100).__str__() + ",'" + fake.name() + ",'" + fake.name() + '\n')
#             print(i, "/", n)

import os
import random
import django
from faker.providers import date_time
from psycopg2._psycopg import cursor
from psycopg2.extras import execute_values


if __name__ == '__main__':
    from faker import Faker

    fake = Faker()
    fake.add_provider(date_time)
    consultations = ['albire', 'detartraj', 'implant', 'extractie molari de minte', 'plombare', 'punere de fatete',
                    'ortodontie', 'control', 'fast and fixed']
    batch_size = 1000
    with open('patient.sql', 'w') as file:
        sql = f"TRUNCATE TABLE patients RESTART IDENTITY CASCADE;"
        file.write(sql + '\n')

        for i in range(0, 1000000, 1000):
            data = []
            for j in range(i, i + 1000):
                patient_first_name = fake.first_name()
                patient_last_name = fake.last_name()
                patient_age = random.randint(2, 90)
                patient_country = fake.country()
                patient_consultation = fake.word()
                data.append(f"('{patient_first_name}', '{patient_last_name}', '{patient_age}', '{patient_country}', '{patient_consultation}')")
            sql = f"INSERT INTO patients (patient_first_name, patient_last_name, patient_age, patient_country, patient_consultation) VALUES {','.join(data)};"
            file.write(sql + '\n')