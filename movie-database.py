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

        print('Successfully added %s to the database.' % the_name)
    
    except Error as e:
        print('The error "%s" occurred.' % e)

def good_name(connection, the_name):
    """Returns True if the name does not already exist in the table.
    """
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM my_movies WHERE name = "%s"' % the_name)

    # If there aren't any rows with that name, the name is fine to add.
    if not cursor.fetchall():
        return True
    else:
        return False

def search(connection, parameters_and_values):
    """Takes a connection and a dictionary of parameters and associated values to search a table for. Returns that portion of the table.
    """
    cursor = connection.cursor()

    query = 'SELECT * FROM my_movies WHERE '

    for p, v in parameters_and_values.items():
        query += '%s = "%s" AND ' % (p, v)
    
    query = query[:-4]

    cursor.execute(query)

    return cursor.fetchall()

def update(connection, parameter, value, name):
    """Updates a row of the table (identifed by name) by changing the parameter to the new value.
    """
    try:
        cursor = connection.cursor()
        query = 'UPDATE my_movies SET %s = "%s" WHERE name = "%s"'
        values = (parameter, value, name)
        
        cursor.execute(query % values)
        connection.commit()
    except Error as e:
        print('The error "%s" occurred.' % e)

def delete(connection, name):
    """Deletes a row of the table (identified by name).
    """
    try:
        cursor = connection.cursor()
        query = 'DELETE FROM my_movies WHERE name = "%s"'
        
        cursor.execute(query % name)
    except Error as e:
        print('The error "%s" occurred.' % e)






# TODO: a display() function to print the table nicely, no matter how many rows. 


def main():
    # These two lines only need to run once.
    #mysql_connection = connect('localhost', 'root', 'Scoopy23$')
    #create_database(mysql_connection, 'Movies')

    connection = connect_to_database('localhost', 'root', 'Scoopy23$', 'Movies')

    # This line only needs to run once.
    #create_movie_table(connection.cursor())

    # Start a new task. 
    while True:
        # Make sure the task is chosen properly. 
        while True:
            try:
                task = int(input('What would you like to do? \n 1. Add a movie \n 2. Search movies \n 3. Update a movie \n 4. Delete a movie \n 5. See all movies \n'))
                assert task >= 1 and task <= 5
                break
            except ValueError:
                print('Please enter a number.')
            except:
                print('Please pick between 1-5.')
        
        # Add a movie.    
        while task == 1:
            print('ADD A MOVIE')

            # Get name.
            n = input('Name: ')
            # If the name is already in the database, then quite the adding of the movie.
            if good_name(connection, n) == False:
                print('That movie is already in the database.')
                break

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

            # Start a new task.
            break
        
        # Search movies. 
        while task == 2:
            parameters = {1:'name', 2:'year', 3:'country', 4:'primary_feel', 5:'secondary_feel'}
            another_par = 1
            pars_and_vars = {}  # The dictionary of all parameters and values used in the search. 

            # Will iterate as long as user wants to filter by another parameter.
            while another_par == 1:
                # Will print a subsection of the table depending on the new par/val (added to the old). Can then choose whether or not to add another par/val. 
                while True:
                    try:
                        print('How would you like to search for movies?')
                        for num, p in parameters.items():
                            # If the parameter is alreay used, make it bold.
                            if p in pars_and_vars:
                                print('\033[1m%d. By %s\033[0m' % (num, p))
                            else:
                                print('%d. By %s' % (num, p))

                        option = int(input())
                        assert option >= 1 and option <= 5
                        break
                    except ValueError:
                        print('Please enter a number.')
                    except:
                        print('Please pick between 1-5.')
                
                # If that parameter has already been used, ask for a different one. 
                if parameters[option] in pars_and_vars:
                    print('You have already filtered by %s. Please choose a different parameter.' % parameters[option])
                    continue
                else:
                    p = input('%s to search for: ' % parameters[option].capitalize())
                    if parameters[option] == 'year':
                        p = int(p)
                    pars_and_vars[parameters[option]] = p

                    results = search(connection, pars_and_vars)
                    # If there are no movies in the results, end the search entirely.
                    if not results:
                        print('No movies match those criteria.')
                        break
                    print(results)

                # Check if user wants to filter by even further parameters, if currently have fewer than five parameters. 
                if len(pars_and_vars) == 5:
                    break
                while True:
                    try:
                        another_par = int(input('Want to filer these movies further? \n 1. Yes \n 2. No \n'))
                        assert another_par >= 1 and another_par <= 2
                        break
                    except ValueError:
                        print('Please enter a number.')
                    except:
                        print('Please pick between 1-2.')

            # Start a new task.
            break

        # Update a movie.   
        while task == 3:
            name = input('Which movie would you like to update? ')

            # Get that movie by name.
            result = search(connection, {'name':name})

            # If there's no movie with that name, exit this task.
            if not result:
                print('That movie is not in the database.')
                break

            parameters = {1:'name', 2:'year', 3:'country', 4:'primary_feel', 5:'secondary_feel'}
            while True:
                try:
                    # Print the movie's current info.
                    print(result)
                    print('Which parameter would you like to update?')
                    for num, p in parameters.items():
                        print(' %s. %s' %(num, p.capitalize()))
                    change = int(input())
                    assert change >= 1 and change <= 5
                    break
                except ValueError:
                    print('Please enter a number.')
                except:
                    print('Pick a number between 1-5.')
            
            value = input('What should %s\'s %s be? ' % (name, parameters[change]))

            # Update that parameter of the movie with the new value. 
            update(connection, parameters[change], value, name)

            # Start a new task.
            break

        # Delete a movie.
        while task == 4:
            name = input('Which movie would you like to delete? ')

            # Get that movie by name.
            result = search(connection, {'name':name})

            # If there's no movie with that name, exit this task.
            if not result:
                print('That movie is not in the database.')
                break

            while True:
                try:
                    sure = int(input('Are you sure you want to delete %s? \n 1. Yes \n 2. No \n' % name.capitalize()))
                    assert sure >= 1 and sure <= 2
                    break      
                except ValueError:
                    print('Please enter a number.')  
                except:
                    print('Pick a number between 1-2.')   
            
            if sure == 1:
                delete(connection, name)
            
            break


        # See all movies. 
        while task == 5:
            pass
        







if __name__ == '__main__' :
    main()


