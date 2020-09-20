from psycopg2 import connect # to connect postgresql to python
from getpass import getpass # to prompt for the password during the connection

# params: server_name, db_name, port, user_name & password.
conn = connect(dbname='postgres', user='postgres', password=getpass(prompt='Password: ', stream=None), host='localhost', port=5432)

print('connection successful')  # this won't be executed if conn is not defined properly (incorrect params)

'''
Output
------
Password: your_password
connection successful
'''
