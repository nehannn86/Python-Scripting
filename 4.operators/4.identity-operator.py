#Implementing identity operators.
import os
os.system('clear')
x1 = 4
y1 = 7
x2 = 'Python'
y2 = 'Python'
x3 = [1,2,3]
y3 = [1,2,3]

print('Identity Operator')
print(f'X1: {x1}\nX2: {x2}\nX3: {x3}\nY1: {y1}\nY2: {y2}\nY3: {y3}')
print(f'{x1} is {y1}:',x1 is y1)
print(f'{x2} is {y2}:',x2 is y2)
print(f'{x3} is {y3}:',x3 is y3)
print(f'{x1} is not {y1}:',x1 is not y1)
print(f'{x2} is not {y2}:',x2 is not y2)
print(f'{x3} is not {y3}:',x3 is not y3)

