a = 5
b = 10.67
c = 'Hello World'
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))

print(isinstance(b, float))
print(isinstance(a, float))

print(a)
print(float(a))
print(a) #Data type is preserved
print(float('60'))

#Now lets chack strings 

firstStr = 'Hi'
secondStr = firstStr

print(firstStr)
print(secondStr)

firstStr = 'I changed'

print(firstStr)
print(secondStr) # It didn't change

secondStr = firstStr # Now I make the change possible

print(firstStr)
print(secondStr)

# title() lower() and upper()

firstName = 'jorge'
lastName = 'unas'

print(firstName.title())
print(firstName.upper())

fisrtName = 'JORGE'
print(firstName.lower())


#concatenation:

fullName = fisrtName + ' ' + lastName 

print(fullName)
print(fullName.title()) # capitalize first letters

# print(fullName.title() + ' is ' + 40 + ' years old.') # result in typeerror
print(fullName.title() + ' is ' + str(40) + ' years old.') # result in typeerror
