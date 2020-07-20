#implementing dict in python.

import os
os.system("clear")

#defining dict 
mydict = {'A':'Apple','B':'Ball','C':'Cat','D':'Dog','E':'Elephant'}
print('mydict: ',mydict)
print('Datatype of mydict: ',type(mydict))

#creating dictionary using dict()
mydict1 = dict({1:1,2:2,3:3,4:4,5:5})

#empty dictionary
emptydict = {}
print('emptydict: ',emptydict)

#get values from dict.
print('First Value of mydict:',mydict['A'])
print('Second Value of mydict:',mydict['B'])
print('Third Value of mydict:',mydict.get('C'))
print('Fourth Value of mydict:',mydict.get('D'))
print('Five Value of mydict:',mydict.get('E'))

#modifying values of dict.
mydict['A'] = 'Ant'
mydict['B'] = 'Boy'
mydict['C'] = 'Corn'
mydict['D'] = 'Donkey'
mydict['E'] = 'Eyes'
mydict['F'] = 'Fish'
print('\nModified mydict: ', mydict)

#print list of keys & values from mydict.
print('All the keys of mydict: ',mydict.keys())
print('All the values of mydict: ',mydict.values())

#checking object of dicts
print('mydict1: ',mydict1)
newmydict1 = mydict1.copy()
print('newmydict1: ',newmydict1)
print(f'mydict1 id : {id(mydict1)}, newmydict1 id : {id(newmydict1)}\n')

#list availabe operations for dict.
print(dir(mydict))

#implementing pop() operation on dict.
print('\nmydict1: ',mydict1)
print('Removing last value using pop(): ', mydict1.pop(5))
print('mydict1: ',mydict1)

#implementing update method.
mydict1.update({5:5,6:6,7:7,8:8,9:9,10:10})
print('mydict1: ',mydict1)

#creating new dict from keys.
keys = ['a','e','i','o','u']
mydict2 = dict.fromkeys(keys)
print('mydict2: ',mydict2)
mydict2['a'] = 'a'
mydict2['e'] = 'b'
mydict2['i'] = 'c'
mydict2['o'] = 'd'
mydict2['u'] = 'e'
print('mydict2: ',mydict2)

mydict2.setdefault('a','A')
mydict2.setdefault('Name','Neha')
print('mydict2 with setdefault operation: ',mydict2)

#clear operation on mydict2
mydict2.clear()
print('mydict2 after clear() operation: ',mydict2)

#delete dict
del mydict2
