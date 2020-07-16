#creating simple list
vowels = ['a','e','i','o','u']
print('List: ',vowels)
print('List Type: ',type(vowels))
print('1st value of list:',vowels[0])
print('2nd value of list:',vowels[1])
print('3rd value of list:',vowels[2])
print('4th value of list:',vowels[3])
print('5th value of list:',vowels[4])

#Creating nested list
nestedlist = ['Python',[0,1,2,3,4,5],'Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',0,1,2,3,4,5,6,7,8,9,10,0,0,0]
print('\nNested List: ',nestedlist)
print('Nested List Type: ',type(nestedlist))
print('1st value of first value: ',nestedlist[0][0])
print('1st value of second value: ',nestedlist[1][0])

print('Printing using slicing method: ',nestedlist[2:8])

print('\nOriginal list:',nestedlist)
nestedlist[0] = 'Python Scripting'
print('\nModified list:',nestedlist)

#implementing index() operation on list.
index1 = nestedlist.index('Sunday')
print("Index of 'Sunday' in nested list: ", index1)

#implementing count() operation on list.
count1 = nestedlist.count(0)
print('Count "0" in the list: ',count1)

#implementing clear() operation on list
print('List before clear() operation: ', vowels)
vowels.clear()
print('List after clear() operation: ',vowels)

#list available operations on list
print('Available operations on list:\n',dir(nestedlist))

#appending list with new value.
nestedlist.append(11)
print('\nAdded 11 to list using append() operation: ',nestedlist)

#removing an value from the list.
nestedlist.remove(0)
print('\nRemoved 0 from the list: ', nestedlist)

#inserting new value to the list at first position
nestedlist.insert(0,'Welcome')
print("\nAdded 'Welcome' at 0th position using insert(index,Value) operation: ",nestedlist)

#implemeting extend() operation on list
nestedlist.extend([12,13,14,15])
print("\nAdding list to a list as a values of list: ", nestedlist)

#implementing pop() operation on list
nestedlist.pop()
print("\npop() removes the last value from the list: ", nestedlist)
print('\nRemoving 9th index value using pop: ',nestedlist.pop(9))

#implementing sor() operation on list.
list1= [4,2,4,5,7,1,3,9,6,10,8]
list1.sort()
print("\nSorted List: ", list1)
list1.sort(reverse=True)
print("\nReversed List: ", list1)



