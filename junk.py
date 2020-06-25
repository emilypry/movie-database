






movies = {}

while True:
    task = int(input('What would you like to do? \n 1. Enter a new movie \n 2. See all movies \n'))

    while task == 1:
        name = input('Name of movie: ')
        if name in movies.keys():
            print('%s has already been entered. Please enter a new movie.' % name) 
            continue

        year = input('Year of movie: ')
        while year.isdigit() == False:
            print('Please enter the year.')
            year = input('Year of movie: ')


        movies[name] = year
        break

    while task == 2:
        if not movies:
            print('No movies.')
        else:
            print('Movies:')
            for m in movies:
                print(m)
        break




# can start immediately (with no conditions) and continue indefinitely
#   if needs condition (even if trivial), and will only go once
#   for needs particular number of items to loop through

# can terminate, or start new iteration, without having to meet a condition
#   can't break from if
#   can with for, if know how many items to iterate through

'''
again = 'yes'
while again == 'yes':
    num = int(input('Enter a number: '))
    print('Hooray ' * num)

    again = input('Want to go again? ')


while True:
    num = int(input('Enter a number: '))
    print('Hooray ' * num)
    again = input('Want to go again? ')

    if again != 'yes':
        break

'''
again = 'yes'
while again == 'yes':
    num = int(input('Enter a number between 1 and 3: '))
    if num == 1:
        print('You picked 1.')
        again = input('Again? ')
    elif num == 2:
        print('You picked 2.')
        again = input('Again? ')
    else:
        print('You picked 3.')
        again = input('Again? ')

while True:
    num = int(input('Enter a number between 1 and 3: '))
    if num == 1:
        print('You picked 1.')
        continue