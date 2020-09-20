from psycopg2 import connect # to connect postgresql to python
from getpass import getpass # to prompt for the password during the connection

# params: server_name, db_name, port, user_name & password.
conn = connect(dbname='postgres', user='postgres', password=getpass(prompt='Password: ', stream=None), host='localhost', port=5432)

print('connection successful')  # this won't be executed if conn is not defined properly (incorrect params)

# As we have already established a connection, we can now execute any kind of SQL Query here.
# To run an SQL Query, we need to create a cursor using the conn object above.
cursor = conn.cursor()  # cursor is created

# to execute an SQL query, we do the following
cursor.execute('''
CREATE TABLE student(ID serial, name text, age int, address text);
''')
print('table created')

# after we execute the Query using the execute() method, we need to commit to the database as follows:
conn.commit()
print('changes committed to the db')

print('closing connection to the db....')
conn.close()
print('connection to the db is closed.')

'''
Output
------
Password: your_password
connection successful
table created
changes committed to the db
closing connection to the db...
connection to the db is closed
'''

# Open psql and check whether the `student` table is created under the `postgres` user.
