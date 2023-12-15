pizza = ['mozzarela', 'cheese', 'tomato']

for ingredient in pizza:
    print(ingredient)


# range()

for i in range(8):
    print(i)

for i in range(400, 405):
    print(i)

for i in range(5, 15, 2):
    print(i)


# print the odd numbers until 11
print('Exercise: ood numbers from 1 to 11')
for i in range(1, 12, 2):
    print(i)

# While loops
print('---------------------------')
print('While loops')

a = 0
while a <= 5:
    print(a)
    a += 1

print(a) # = 6, a was altered at the end

b = 1
c = 'Hello World'
while b <= 3:
    print(c)
    b += 1

print('\n')
print('use of continue')

x = 0
while x < 6:
    x += 1
    if x == 4:
        continue
    print(x)

print('\n')
print('use of break')

x = 0
while x < 6:
    x += 1
    if x == 4:
        print('break point')
        break
    print(x)

# Nested loops
print('--------------------------')
print('Nested loops')

# example: 
vocals = ['a', 'e', 'i']

for x in range(1, 4):
    print(x)
    for vocal in vocals:
        print(vocal)
    print('\n')

animals = ['dog', 'cat', 'lion', 'bird']
colors = ['white', 'black', 'brown']

for animal in animals:
    for color in colors:
        print(F'The {animal} is {color}')
    print('\n')


