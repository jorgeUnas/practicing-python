try:
    num = int(input('Write a number here '))
    print('Your number is:', num)
except ValueError:
    print('Make sure it is a number')