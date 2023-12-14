# Reading files

a = open('demo.txt', 'r')

print(a.read())

print('----------------------------')
print('readline()')

a = open('demo.txt', 'r')
print(a.readline())        # reads just 1 line
a.close()

print('----------------------------')
print('read(#)')

a = open('demo.txt', 'r')
print(a.read(7))        # reads just 7 caracters
a.close()

print('----------------------------')
print('with')

with open('demo.txt') as myFile:   # with open and close the file 
    content = myFile.read()
    print(content)        
