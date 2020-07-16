#defining string.

string = 'Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.'

#defining four substrings

substring1 = 'Python'
substring2 = 'is'
substring3 = 'it'
substring4 = 'scripting'

#printing origin string.

print('string: ',string)
print('Length of string is: ', len(string))

#implementing count() operation on the above string

print('\nPerforming count() operation on the above string:')
count1 = string.count(substring1)
count2 = string.count(substring2)
count3 = string.count(substring3)
count4 = string.count(substring4)
print(f'Count of substring:"{substring1}" is: {count1}')
print(f'Count of substring:"{substring2}" is: {count2}')
print(f'Count of substring:"{substring3}" is: {count3}')
print(f'Count of substring:"{substring4}" is: {count4}')

#implementing index() Operation on string

index1 = string.index(substring1)
index2 = string.index(substring2)
index3 = string.index(substring3)
index4 = string.index(substring4)
print('\nPerforming index() operation on the above string:')
print(f'Index of substring "{substring1}" is: {index1}')
print(f'Index of substring "{substring2}" is: {index2}')
print(f'Index of substring "{substring3}" is: {index3}')
print(f'Index of substring "{substring4}" is: {index4}')

#implementing find() operation on string

find1 = string.find(substring1)
find2 = string.find(substring2)
find3 = string.find(substring3)
find4 = string.find(substring4)
print('\nPerforming find() operation on the above string:')
print(f'Find of substring "{substring1}" is: {find1}')
print(f'Find of substring "{substring2}" is: {find2}')
print(f'Find of substring "{substring3}" is: {find3}')
print(f'Find of substring "{substring4}" is: {find4}')
