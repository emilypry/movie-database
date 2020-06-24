
'''
if 0==0:
    a = input('What is your name? ')
    print('Welcome, %s.' % a)
'''



# can start immediately (with no conditions) and continue indefinitely
#   if needs condition (even if trivial), and will only go once
#   for needs particular number of items to loop through

# can terminate without having to meet a condition
#   can't break from if

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