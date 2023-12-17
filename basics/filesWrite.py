with open('demo.txt') as myFile:   # with open and close the file 
    content = myFile.read()
    print(content)  

print('------------------------------------------')
a = open('demo.txt', 'a')
print(a.write('\nI am a new line of text'))
a.close()

with open('demo.txt') as myFile:   # with open and close the file 
    content = myFile.read()
    print(content)  
