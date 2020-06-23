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
    try:
        cursor = connection.cursor()

        query = 'INSERT INTO my_movies (name, year, country, primary_feel, secondary_feel) VALUES (%s, %s, %s, %s, %s)'
        values = (the_name, the_year, the_country, the_primary_feel, the_secondary_feel)
        cursor.execute(query, values)

        connection.commit()

        print('Successfully added %s to my_movies.' % the_name)
    
    except Error as e:
        print('The error "%s" occurred.' % e)

def search(connection, the_parameter, the_value):
    try:  
        cursor = connection.cursor()

        query = 'SELECT * FROM my_movies WHERE %s = %s'
        values = (the_parameter, the_value)
        cursor.execute(query, values)
    except:
        print('Something went wrong with the search.')

    return cursor.fetchall()



def main():
    # These two lines only need to run once.
    #mysql_connection = connect('localhost', 'root', 'Scoopy23$')
    #create_database(mysql_connection, 'Movies')

    connection = connect_to_database('localhost', 'root', 'Scoopy23$', 'Movies')

    # This line only needs to run once.
    #create_movie_table(connection.cursor())

    while True:
        try:
            task = int(input('What would you like to do? \n 1. Add a movie \n 2. Search movies \n 3. Update a movie \n 4. Delete a movie \n 5. See all movies \n'))
            assert task >= 1 and task <= 5
            break
        except ValueError:
            print('Please enter a number.')
        except:
            print('Please pick between 1-5.')
        
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

        # Add the movie to my_movies.
        add_movie(connection, n, y, c, p, s)

    elif task == 2:
        # Search movies. 

        # show all movies with a given parameter
        # then can add another parameter, showing fewer
        # or, can reset all parameters and start fresh (maybe go back one step???)

        while True:
            try:
                option = int(input('How would you like to search for movies? \n 1. By name \n 2. By year \n 3. By country \n 4. By primary feel \n 5. By secondary feel \n'))
                assert option >= 1 and option <= 5
                break
            except ValueError:
                print('Please enter a number.')
            except:
                print('Please pick between 1-5.')

        if option == 1:
            # Search by name.
            pass
        elif option == 2:
            # Search by year.
            pass
        elif option == 3:
            # Search by country.
            pass
        elif option == 4:
            # Search by primary feel.
            pass
        else:
            # Search by secondary feel. 
            pass


        
    elif task == 3:
        # Update a movie.
        pass
    elif task == 4:
        # Delete a movie. 
        pass
    else:
        # See all movies.
        pass
    







if __name__ == '__main__' :
    main()


