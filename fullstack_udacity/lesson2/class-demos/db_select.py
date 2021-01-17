import psycopg2

# Estabilish a connection, starting a session, begins a transaction
connection = psycopg2.connect('dbname=example user=postgres password=guerradostronos')

# Sets a cursor to begin executing commands
cursor = connection.cursor()

cursor.execute("SELECT id, name, completed FROM tasks;")
result = cursor.fetchall()
# cursor.fetchmany(3)
# cursor.fetchone()  # fetches the first result in the result set
print(result)

cursor.close()
connection.close()  # close the connection (not done automatically)