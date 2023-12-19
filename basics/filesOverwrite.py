with open('demo.txt') as myFile:   # with open and close the file 
    content = myFile.read()
    print(content)  

print('------------------------------------------')
a = open('demo.txt', 'w') # w overwrite the file
print(a.write('\nI overwrite the content'))
a.close()

with open('demo.txt') as myFile:   # with open and close the file 
    content = myFile.read()
    print(content)  