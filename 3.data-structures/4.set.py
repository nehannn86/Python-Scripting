#implementing set in python.

#define sets
myset = {0,1,2,3,4,5,6,7,8,9,10}
emptyset = set()
myset1 = {('a','e','i','o','u'),"Python",1,2,3,4,5}
print(f'emptyset:{emptyset}\nDatatype of emptyset:{type(emptyset)}\nmyset:{myset}\nDatatype of myset:{type(myset)}\nmyset1{myset1}\nDatatype of myset1:{type(myset1)}\n')

#modifying values of a set.
myset.add(11)
print('added 11 to myset: ',myset)
myset.update([11,12,13,14,15])
print('added multiple values to myset: ',myset)

#deleting from sets
myset.discard(15)
print('Discarded 15 from myset: ',myset)
myset.remove(0)
print('Removed 0 from myset: ',myset)

#clear operation on set
myset1.clear()
print('myset1 after clear() operation: ',myset1)

#Mathematic operations on sets

A = {1,2,3,4,4,5}
B = {3,4,5,6,7,8}

print('\nSet A: ',A,'\nSet B: ',B)

print('\nUinon of Set A & Set B: ',A|B)
print('Intersection of Set A & Set B: ',A&B)
print('Difference of Set A & Set B: ',A-B)
print('Difference of Set B & Set A: ',B-A)
print('Symmetric Difference of Set A & Set B: ',A^B)

