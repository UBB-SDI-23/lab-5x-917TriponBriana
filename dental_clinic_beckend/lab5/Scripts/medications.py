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
cur.execute('TRUNCATE TABLE medications RESTART IDENTITY CASCADE;')

# generate new records to insert
batch_size = 1000
num_batches = 1000
total_records = batch_size * num_batches

for i in range(num_batches):
    print(f'Generating batch {i+1}/{num_batches}')

    values = []
    for j in range(batch_size):
        med_name = fake.random_element(elements=('Advil', 'Algocalmin', 'Augmentin', 'Cuminol', 'Fluorel', 'Eficef'))
        med_active_subst = fake.random_element(elements=('ibuprofen', 'antibiotic', 'paracetamol'))
        med_price = fake.random_int(min=15, max=300)
        med_expiration_date = fake.random_element(elements=('13.03.2022', '21.06.2023', '29.10.2022', '05.01.2024', '30.12.2024', '07.05.2023'))
        med_usage = fake.random_element(elements=('Administrare orala cu apa', 'In intervale egate de timp'))
        # dent_id = fake.random_int(min=1, max=1000000)

        values.append(
            sql.SQL("({}, {}, {}, {}, {})").format(
                sql.Literal(med_name),
                sql.Literal(med_active_subst),
                sql.Literal(med_price),
                sql.Literal(med_expiration_date),
                sql.Literal(med_usage),
                # sql.Literal(dent_id)
            )
        )

    sql_statement = sql.SQL("INSERT INTO medications (med_name, med_active_subst, med_price, med_expiration_date, med_usage) VALUES {}").format(
        sql.SQL(", ").join(values)
    )

    # execute the SQL statement
    cur.execute(sql_statement)

# commit the changes and close the cursor and connection
conn.commit()
cur.close()
conn.close()

