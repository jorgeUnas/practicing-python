x = 30
y = 20

if x == y:
    print('x is equal to y')
elif x > y:
    print('x is greater than y')
else: 
    print('x is not greater than y')

#multiple if

pizza = ['mozzarela', 'cheese', 'tomato']

if 'mozzarela' in pizza: 
    print('Good cheese!')
if 'olives' in pizza:
    print('particular taste')
if 'tomato' in pizza:
    print('The classic one!')

# exercise:

temp = 21

if temp <= 0: 
    print('Its freezing')
elif temp <= 20:
    print('it feels cold')
else: 
    print('Now its hot')