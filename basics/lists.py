myList = ['Jorge', 345, False, 45.23]

print(myList[0])

print(myList[2])

print(type(myList[1]))

#modifing lists

myList = myList + ['Lopez']
print(myList)

myList[4] = True
print(myList)

# myList[5] = True  # error for index out of range, here is not like JS where I can create new elements indexing

# concatenating lists

myNumbers = [2, 3, 6]

print(myList+myNumbers)

# insert()

myNumbers.insert(1, 2.5)
print(myNumbers)

#delete 

del myNumbers[1]
print(myNumbers)

#remove() 

myNumbers = myNumbers + [2]
print(myNumbers)
myNumbers.remove(2) # just eliminate the first coincidence
print(myNumbers)

# find element 
if 'Jorge' in myList:
    print('Jorge is in the list')

# loop in the list

for elem in myList:  # in JS is for of loop 
    print(elem)

#length 

print(len(myList))
print(len(myNumbers))


# sort()

newList = ['yellow', 'red', 'green', 'grey', 'blue', 'purple']

newList.sort()  # this modifys the original list

print(newList)

newList.sort(reverse=True)  # sort and then reverse the list

print(newList)

newList = ['yellow', 'red', 'green', 'grey', 'blue', 'purple'] # original list

newList.reverse()  #reverse the original list   

print(newList)

# sorted() does not change the original list 


newList = ['yellow', 'red', 'green', 'grey', 'blue', 'purple'] # original list

sorted(newList)

print(newList)
print(sorted(newList))



