import shutil
import os

newFile = open('demo2.txt', 'w')
newFile.close()

newFile = open('demo2.txt', 'w')
newFile.write('Hi, I am a new paragraph.')
newFile.close()

shutil.copy('demo2.txt', 'demo2Copy.txt')

otherFile = open('demo2Copy.txt', 'a')
otherFile.write('\nI am an appended paragraph.')
otherFile.close()

newFile = open('demo2.txt', 'r')
print(newFile.read())
newFile.close()

otherFile = open('demo2Copy.txt', 'r')
print(otherFile.read())
otherFile.close()

