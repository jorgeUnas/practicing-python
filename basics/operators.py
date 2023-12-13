# aritmetic operators

a = 5
b = 2

c = a + b
d = a - b
e = a * b
f = a / b
g = a ** b
i = a % b

print([c, d, e, f, g, i])

#assignment operators

z = 10

z += b
print(z)

z -= b
print(z)

z *= a
print(z)

z /= b
print(int(z)) #division converts to float

z **= b
print(z)

# comparison operators 

x = 100 
y = 500
w = 100

print(x == y)
print(x != w)
print(x > y)
print(x < y)
print(x >= w)
print(x <= y)

# Logical operators

a = 4 

print(a > 2 and a < 9)
print(a > 3 or a == 5)
print(not(a > 2 and a < 9))

# identity operators
print('identity operators')

a = 3
b = 4
c = a

print(a is b)
print(a is c)
print(a is not c)

# membership operators
print('membership operators')

numbs = [1,2,3,4,5,6,7,8,9,10]

print(10 in numbs)
print(0 in numbs)
print(0 not in numbs)

#bitwise operators

print('bitwise operators')

a = 24 
b = 60

print(bin(24))
print(bin(60))

print(a & b)
print(a | b)
print(a ^ b)