#implementing strip function

string1 = "*Python Scripting*"
string2 = 'xoxo love xoxo'

print('\nString1: ', string1)
print('Striped value of string1: ', string1.strip('*'))
print('Performing strip() on right side of string1: ', string1.rstrip('*'))
print('\nString2: ', string2)
print('Striped Value of string2: ', string2.strip('xoxo'))

print('Perfroming strip() on left side of string: ', string2.lstrip('xoxo'))
#implementing split value

string3 = "\nPython Scripting Is Fun & Easy"
string4 = 'Milk,Bread,Fruits,Vegitables'

print('\nString3: ', string3)
print('Splitting string3 at every space: ', string3.split( ))

print('\nString4: ', string4)
print('Splitting string4 at every ,: ', string4.split(','))
