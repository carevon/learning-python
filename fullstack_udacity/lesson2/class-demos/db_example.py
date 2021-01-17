import psycopg2

connection = psycopg2.connect('dbname=example user=postgres password=guerradostronos')

cursor = connection.cursor()

cursor.execute(''' DROP TABLE IF EXISTS tasks;''')
cursor.execute('''
    CREATE TABLE tasks (
        id INTEGER PRIMARY KEY,
        name VARCHAR NOT NULL,
        completed BOOLEAN NOT NULL DEFAULT False
    );
''')

connection.commit()
cursor.close()
connection.close()
