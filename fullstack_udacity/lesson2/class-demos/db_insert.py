import psycopg2

connection = psycopg2.connect('dbname=example user=postgres password=guerradostronos')

cursor = connection.cursor()

# first insert method
cursor.execute("INSERT INTO tasks (id, name, completed) VALUES (%s, %s, %s);", (1, "limpar o quarto", True))

# 2nd insert method
SQL = "INSERT INTO tasks (id, name, completed) VALUES (%(id)s, %(name)s, %(completed)s);"
data = {'id': 2, 'name': 'lavar a louça', 'completed': False}
cursor.execute(SQL, data)

connection.commit()
cursor.close()
connection.close()