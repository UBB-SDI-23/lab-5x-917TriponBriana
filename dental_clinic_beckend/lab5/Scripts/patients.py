import psycopg2
from faker import Faker
from psycopg2 import sql

fake = Faker()

conn = psycopg2.connect(
    host="127.0.0.1",
    port="5432",
    database="dc_clinic",
    user="db_user",
    password="db_pass"
)
cur = conn.cursor()

# delete all the existing records
cur.execute('TRUNCATE TABLE patients RESTART IDENTITY CASCADE;')

# generate new records to insert
batch_size = 1000
num_batches = 1000
total_records = batch_size * num_batches

for i in range(num_batches):
    print(f'Generating batch {i+1}/{num_batches}')

    values = []
    for j in range(batch_size):
        patient_first_name = fake.first_name()[:40]
        patient_last_name = fake.last_name()[:40]
        patient_age = fake.random_int(min=2, max=99)
        patient_country = fake.country()
        patient_consultation = fake.random_element(elements=('Albire', 'Detartraj', 'Plombare', 'Implant', 'Fatete'))

        values.append(
            sql.SQL("({}, {}, {}, {}, {})").format(
                sql.Literal(patient_first_name),
                sql.Literal(patient_last_name),
                sql.Literal(patient_age),
                sql.Literal(patient_country),
                sql.Literal(patient_consultation)
            )
        )

    sql_statement = sql.SQL("INSERT INTO patients (patient_first_name, patient_last_name, patient_age, patient_country, patient_consultation) VALUES {}").format(
        sql.SQL(", ").join(values)
    )

    # execute the SQL statement
    cur.execute(sql_statement)

# commit the changes and close the cursor and connection
conn.commit()
cur.close()
conn.close()

