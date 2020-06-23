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

def add_movie(connection, the_name, the_year, the_country, the_primary_feel, the_secondary_feel):
    pass





def main():
    # These two lines only need to run once.
    #mysql_connection = connect('localhost', 'root', 'Scoopy23$')
    #create_database(mysql_connection, 'Movies')

    connection = connect_to_database('localhost', 'root', 'Scoopy23$', 'Movies')

    # This line only needs to run once.
    #create_movie_table(connection.cursor())

    while True:
        try:
            task = int(input('What would you like to do? \n 1. Add a movie \n 2. Search movies \n 3. Update a movie \n 4. Delete a movie \n'))
            assert task >= 1 and task <= 4
            break
        except ValueError:
            print('Please enter a number.')
        except:
            print('Please pick between 1-4.')
        
    print(task)

    if task == 1:
        # Add a movie. 
        print('ADD A MOVIE')

        # Get name.
        n = input('Name: ')

        # Get year.
        while True:
            try:
                y = int(input('Year: '))
                break
            except ValueError:
                print('Please enter a year.')

        # Get country.
        c = input('Country: ')

        # Get primary_feel and secondary_feel. 
        feel_choices = {1:'Heart-warming', 2:'Scary', 3:'Depressing', 4:'Meditative', 5:'Fun', 6:'Intense', 7:'Complicated', 8:'Wonderful', 9:'Funny', 10:'Light-hearted', 11:'Disturbing', 12:'Thoughtful', 13:'Other'}

        feel = []
        feel_num = ['primary', 'secondary']

        for i in range(0, 2): 
            while True:
                try:
                    print('%s feel:' % feel_num[i].capitalize())
                    for num, word in feel_choices.items():
                        print('%d. %s' % (num, word))
                    f = int(input())
                    assert f >= 1 and f <= 13
                    break
                except ValueError:
                    print('Please enter a number.')
                except:
                    print('Please pick between 1-13.')
            
            if f == 13:
                feel.append(input('Describe, in one word, the %s feel: ' % feel_num[i]))
            else:
                feel.append(feel_choices.get(f))

        p, s = feel[0], feel[1]

        print(p, s)

        
        



        '''
        p = int(input('Primary feel \n 1. Heart-warming \n 2. Scary \n 3. Depressing \n 4. Meditative \n 5. Intense \n 6. Complicated \n 7. Wonderful \n 8. Fun \n 9. Funny \n 10. Light-hearted \n 11. Disturbing \n 12. Thoughtful \n 13. Other'))
       
        '''



        
    elif task == 2:
        # Search movies. 
        pass
    elif task == 3:
        # Update a movie.
        pass
    else:
        # Delete a movie. 
        pass
    







if __name__ == '__main__' :
    main()


