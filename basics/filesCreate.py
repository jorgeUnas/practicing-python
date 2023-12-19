# create a file, write 3 equal lines with loops and read the file

# Creation

a = open('myNewFile.txt', 'w')  # w creates the file each time executed
a.close()

# writing

a = open('myNewFile.txt', 'a')
for i in range(3):
    a.write(str(i) + ' Hello people\n')
a.close()

# reading

with open('myNewFile.txt') as myFile:
    content = myFile.read()
    print(content)
 
