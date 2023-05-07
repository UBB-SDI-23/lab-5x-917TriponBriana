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
cur.execute('TRUNCATE TABLE dentists RESTART IDENTITY CASCADE;')

# generate new records to insert
batch_size = 1000
num_batches = 1000
total_records = batch_size * num_batches

for i in range(num_batches):
    print(f'Generating batch {i+1}/{num_batches}')

    values = []
    for j in range(batch_size):
        dentist_first_name = fake.first_name()[:50]
        dentist_last_name = fake.last_name()[:50]
        dentist_age = fake.random_int(min=2, max=99)
        dentist_country = fake.country()
        dentist_salary = fake.random_int(min=12000, max=30000)
        med_id = fake.random_int(min=1, max=1000000)

        values.append(
            sql.SQL("({}, {}, {}, {}, {}, {})").format(
                sql.Literal(dentist_first_name),
                sql.Literal(dentist_last_name),
                sql.Literal(dentist_age),
                sql.Literal(dentist_country),
                sql.Literal(dentist_salary),
                sql.Literal(med_id)
            )
        )

    sql_statement = sql.SQL("INSERT INTO dentists (dentist_first_name, dentist_last_name, dentist_age, dentist_country, dentist_salary, med_id) VALUES {}").format(
        sql.SQL(", ").join(values)
    )

    # execute the SQL statement
    cur.execute(sql_statement)

# commit the changes and close the cursor and connection
conn.commit()
cur.close()
conn.close()

