# import psycopg2
# from faker import Faker
# from psycopg2 import sql
#
# fake = Faker()
#
# conn = psycopg2.connect(
#     # host="ec2-16-170-167-143.eu-north-1.compute.amazonaws.com",
#     database="db_clinic",
#     user="db_user",
#     password="db_pass",
#     host="127.0.0.1",
#     port="5432",
# )
# cur = conn.cursor()
#
# # delete all the existing records
# cur.execute('TRUNCATE TABLE app1_patient RESTART IDENTITY CASCADE;')
#
# # generate new records to insert
# batch_size = 1000
# num_batches = 100
# total_records = batch_size * num_batches
#
# for i in range(num_batches):
#     print(f'Generating batch {i+1}/{num_batches}')
#
#     values = []
#     for j in range(batch_size):
#         # generate fake data for patient fields
#         patient_first_name = fake.patient_first_name()[:100]
#         patient_last_name = fake.patient_last_name()[:100]
#         patient_age = fake.random_int(min=2, max=100)
#         patient_country = fake.patient_country()
#         patient_consultation = fake.word()
#
#         # escape any special characters ot quotes in data
#         values.append(
#             sql.SQL("({}, {}, {}, {}, {})").format(
#                 sql.Literal(patient_first_name),
#                 sql.Literal(patient_last_name),
#                 sql.Literal(patient_age),
#                 sql.Literal(patient_country),
#                 sql.Literal(patient_consultation)
#             )
#         )
#
#     # join the values and generate the SQL statement
#     sql_statement = sql.SQL("INSERT INTO app1_patient (patient_first_name, patient_last_name, patient_age, patient_country, patient_consultation) VALUES {}").format(
#         sql.SQL(", ").join(values)
#     )
#
#     # execute the SQL statement
#     cur.execute(sql_statement)
#
# # commit the changes and close the cursor and connection
# conn.commit()
# cur.close()
# conn.close()

#
# import random
# import sys
# from faker import Faker
#
#
# # if __name__ == '__main__':
# #     fake = Faker()
# #     step = 1000
# #     consultations = ['albire', 'detartraj', 'implant', 'extractie molari de minte', 'plombare', 'punere de fatete', 'ortodontie', 'control', 'fast and fixed']
# #     header = "insert into app1_patient (patient_first_name, patient_last_name, \"patient_age\", patient_countrty, patient_consultation) VALUES "
# #     file_preffix = "patient_"
# #     file_suffix = ".sql"
# #
# #     original_stdout = sys.stdout
# #
# #     for i in range(step):
# #         with open(f"{file_preffix}{i}{file_suffix}", "w") as file:
# #             sys.stdout = file
# #             print(header)
# #             for j in range(step):
# #                 print(f"('{fake.name()}','{fake.name()}','{random.randint(2, 90)}','{fake.country()}','{fake.word()}", end='')
# #
# #                 if j != step - 1:
# #                     print(',')
# #
# #         sys.stdout = original_stdout
# #         print(f"{i+1}/1000")
