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
cur.execute('TRUNCATE TABLE medication_dentist RESTART IDENTITY CASCADE;')

# generate new records to insert
batch_size = 1000
num_batches = 10000
total_records = batch_size * num_batches

for i in range(num_batches):
    print(f'Generating batch {i+1}/{num_batches}')
    med_id = fake.random_int(min=1, max=(i+1)*100)

    values = []
    for j in range(batch_size):
        dentist_id = fake.random_int(min=j*1000 + 1, max=(j+1)*1000)
        prescription_date = fake.random_element(elements=('13.03.2022', '21.06.2023', '29.10.2022', '05.01.2024', '30.12.2024', '07.05.2023'))
        diagnostic = fake.random_element(elements=('Albire', 'Detartraj', 'Plombare', 'Implant', 'Fatete'))

        values.append(
            sql.SQL("({}, {}, {}, {})").format(
                sql.Literal(med_id),
                sql.Literal(dentist_id),
                sql.Literal(prescription_date),
                sql.Literal(diagnostic)
            )
        )

    sql_statement = sql.SQL("INSERT INTO medication_dentist (med_id, dentist_id, prescription_date, diagnostic) VALUES {}").format(
        sql.SQL(", ").join(values)
    )

    # execute the SQL statement
    cur.execute(sql_statement)

# commit the changes and close the cursor and connection
conn.commit()
cur.close()
conn.close()

