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
cur.execute('TRUNCATE TABLE consultations RESTART IDENTITY CASCADE;')

# generate new records to insert
batch_size = 1000
num_batches = 1000
total_records = batch_size * num_batches

for i in range(num_batches):
    print(f'Generating batch {i+1}/{num_batches}')

    values = []
    for j in range(batch_size):
        consultation_type = fake.random_element(elements=('Albire', 'Detartraj', 'Plombare', 'Implant', 'Fatete'))
        consultation_price = fake.random_int(min=50, max=1000)
        consultation_duration = fake.random_element(elements=('13.03.2022', '21.06.2023', '29.10.2022', '05.01.2024', '30.12.2024', '07.05.2023'))
        consultation_date = fake.country()
        patient_id = fake.random_int(min=1, max=1000000)

        values.append(
            sql.SQL("({}, {}, {}, {}, {})").format(
                sql.Literal(consultation_type),
                sql.Literal(consultation_price),
                sql.Literal(consultation_duration),
                sql.Literal(consultation_date),
                sql.Literal(patient_id)
            )
        )

    sql_statement = sql.SQL("INSERT INTO consultations (consultation_type, consultation_price, consultation_duration, consultation_date, patient_id) VALUES {}").format(
        sql.SQL(", ").join(values)
    )

    # execute the SQL statement
    cur.execute(sql_statement)

# commit the changes and close the cursor and connection
conn.commit()
cur.close()
conn.close()

