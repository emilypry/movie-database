import mysql.connector 
from mysql.connector import Error 

def connect(host_name, username, password):
    connection = None

    try:
        connection = mysql.connector.connect(host=host_name, user=username, passwd=password)
        print('Connected to MySQL successfully.')
    except Error as e:
        print('The error "%s" occurred.' % e)
    
    return connection

def create_database(connection, database_name):
    cursor = connection.cursor()
    
    try:
        cursor.execute('CREATE DATABASE %s' % database_name)
        print('Created the "%s" database successfully.' % database_name)
    except Error as e:
        print('The error "%s" occurred.' % e)

    return cursor

def connect_to_database(host_name, username, password, database_name):
    connection = None

    try:
        connection = mysql.connector.connect(host = host_name, user = username, passwd = password, database = database_name)
        print('Connected to the "%s" database successfully.' % database_name)
    except Error as e:
        print('The error "%s" occurred.' % e)

    return connection






def main():
    # These two lines must only be done once.
    '''
    mysql_connection = connect('localhost', 'root', 'Scoopy23$')
    cursor = create_database(mysql_connection, 'Movies')
    '''

    connection = connect_to_database('localhost', 'root', 'Scoopy23$', 'Movies')





if __name__ == '__main__' :
    main()


