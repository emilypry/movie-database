import mysql.connector 
from mysql.connector import Error 

def connect(host_name, username, password):
    """Connects to your MySQL account. 
    """
    connection = None

    try:
        connection = mysql.connector.connect(host=host_name, user=username, passwd=password)
        print('Connected to MySQL successfully.')
    except Error as e:
        print('The error "%s" occurred.' % e)
    
    return connection

def create_database(connection, database_name):
    """Creates a new database in MySQL.
    """
    cursor = connection.cursor()
    
    try:
        cursor.execute('CREATE DATABASE %s' % database_name)
        print('Created the "%s" database successfully.' % database_name)
    except Error as e:
        print('The error "%s" occurred.' % e)

def connect_to_database(host_name, username, password, database_name):
    """Connects to a particular database in MySQL.
    """
    connection = None

    try:
        connection = mysql.connector.connect(host = host_name, user = username, passwd = password, database = database_name)
        print('Connected to the "%s" database successfully.' % database_name)
    except Error as e:
        print('The error "%s" occurred.' % e)

    return connection


def create_movie_table(cursor):
    """Creates a table, my_movies, in MySQL.
    """

    try:
        cursor.execute('CREATE TABLE my_movies (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), year INT, country VARCHAR(255), primary_feel VARCHAR(255), secondary_feel VARCHAR(255))')
        print('Table "my_movies" created successfully.')
    except Error as e:
        print('The error "%s" occurred.' % e)







def main():
    # These two lines only need to run once.
    #mysql_connection = connect('localhost', 'root', 'Scoopy23$')
    #create_database(mysql_connection, 'Movies')

    connection = connect_to_database('localhost', 'root', 'Scoopy23$', 'Movies')
    cursor = connection.cursor()

    # This line only needs to run once.
    #create_movie_table(cursor)
    
    '''
    what to do on each iteration?
    -add new movie
    -search for set of movies
    -update movie info


    '''




if __name__ == '__main__' :
    main()


