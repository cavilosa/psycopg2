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

cursor.execute('Select * from table4;')
lines = cursor.fetchall()
for line in lines:
    print (line)

cursor.execute('Select * from table4;')
lines = cursor.fetchone()
cursor.execute('insert into table4 values (%s, %s);', (lines[0]+3, lines[1]))
cursor.execute('Select * from table4;')
results = cursor.fetchall()
print("results fetchall", results)



conn.commit()
conn.close()
cursor.close()
