#implementing tuples

import os
os.system("clear")

#Define tuple
mytuple = (1,1,2,3,4,5,6,7,8,9,10)
print('Original Tuple: ',mytuple)
print('Type of Tuple: ', type(mytuple))

#Chnage value of tuple
mytuple = (1,2,3,4,5,[1,2,3,4,5],'Python Scripting')
print('\nReassigned Tuple: ', mytuple)
print('Type of Tuple: ', type(mytuple))

#print tuple values
print('\n1st value of tuple: ',mytuple[0])
print('5th value of tuple: ',mytuple[5])

#slicing on tuples
print(':',mytuple[:])
print('0:4 ',mytuple[0:4])
print('3:',mytuple[3:])
print(':3',mytuple[:3])
print(':-3',mytuple[:-3])
print('-5:',mytuple[-5:])

#Moding value of tuple.
mytuple[5][2] = 6
print('\nModified mutable value of tuple: ',mytuple)

#performing + and * operation on tuple.
tuple1 = (1,2,3)
tuple2 = (4,5,6)
tuple3 = ("Python",)
result = (tuple1 + tuple2)
print(f"\nAddition of {tuple1} & {tuple2} is: {result}")
result = (tuple3 * 3)
print(f"\nMultiplication of {tuple3} * 3 is: {result}")

#deleting tuple
newtuple = 0,9,8,7,6,5,4,3,2,1
print('\nNew Tuple: ',newtuple)
print('Type of tuple: ', type(newtuple))
del newtuple
print('New Tuple: ',newtuple)
