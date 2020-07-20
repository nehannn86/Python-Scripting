#Implementing nested if...else statements.

import os
os.system('clear')
print('***Nested if..else***')
numbers = {1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten'}
n = int(input('Numbers to Words from 1 to 10:\nGive Any Number Between 1-10: '))
if n in numbers:
    if n == 1:
        print('The word for n is : ',numbers.get(n))
    elif n == 2:
        print('The word for n is : ',numbers.get(n))
    elif n == 3:
        print('The word for n is : ',numbers.get(n))
    elif n == 4:
        print('The word for n is : ',numbers.get(n))
    elif n == 5:
        print('The word for n is : ',numbers.get(n))
    elif n == 6:
        print('The word for n is : ',numbers.get(n))
    elif n == 7:
        print('The word for n is : ',numbers.get(n))
    elif n ==8:
        print('The word for n is : ',numbers.get(n))
    elif n ==9:
        print('The word for n is : ',numbers.get(n))
    else:
        print('The word for n is : ',numbers.get(n))
else:
    print('Please give number withing the range of 1 to 10')

