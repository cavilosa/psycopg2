import psycopg2


conn = psycopg2.connect('dbname=example user=postgres password=cavilosa1')


cursor = conn.cursor()

cursor.execute('drop table if exists table4;')

cursor.execute('''
    create table table4 (
        id integer primary key,
        completed boolean not null default false
    );
''')

cursor.execute('insert into table4 values (1, false), (%s, %s);', (2, True))

#tamplate with sql
SQL = 'insert into table4 values (%(id)s, %(completed)s);'

data = {
    "id": 3,
    "completed": False
}

cursor.execute(SQL, data)

conn.commit()
conn.close()
cursor.close()
