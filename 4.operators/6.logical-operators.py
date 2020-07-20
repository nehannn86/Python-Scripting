#Implementing Logical Operators.
import os
os.system('clear')
x1 = 5
x2 = 7
y1 = 2
y2 = 4

print('***Logical Operators***')
print(f'X1 = {x1} Y1 = {y1}\nX2 = {x2} Y2 = {y2}\n')
print(f'{x1} > {y1} and {x2} > {y2}: ',x1 > y1 and x2 > y2)
print(f'{x1} < {y1} and {x2} < {y2}: ',x1 < y1 and x2 < y2)
print(f'{x1} > {y1} and {x2} < {y2}: ',x1 > y1 and x2 < y2)
print(f'{x1} < {y1} and {x2} > {y2}: ',x1 < y1 and x2 > y2)

print(f'\n{x1} > {y1} or {x2} > {y2}: ',x1 > y1 or x2 > y2)
print(f'{x1} < {y1} or {x2} < {y2}: ',x1 < y1 or x2 < y2)
print(f'{x1} > {y1} or {x2} < {y2}: ',x1 > y1 or x2 < y2)
print(f'{x1} < {y1} or {x2} > {y2}: ',x1 < y1 or x2 > y2)

print(f'\nnot({x2} > {y2}): ',not(x2 > y2))
print(f'not({x2} < {y2}): ',not(x2 < y2))
print(f'not({x2} < {y2}): ',not(x2 > y2))
print(f'not({x2} > {y2}): ',not(x2 > y2))

print(f'\nall([{x1} > {y1},{x2} > {y2}])',all([x1 > y1,x2 > y2]))
print(f'all([{x1} < {y1},{x2} < {y2}])',all([x1 < y1,x2 < y2]))
print(f'all([{x1} > {y1},{x2} < {y2}])',all([x1 > y1,x2 < y2]))
print(f'all([{x1} < {y1},{x2} > {y2}])',all([x1 < y1,x2 > y2]))

print(f'\nany([{x1} > {y1},{x2} > {y2}])',any([x1 > y1,x2 > y2]))
print(f'any([{x1} < {y1},{x2} < {y2}])',any([x1 < y1,x2 < y2]))
print(f'any([{x1} > {y1},{x2} < {y2}])',any([x1 > y1,x2 < y2]))
print(f'any([{x1} < {y1},{x2} > {y2}])',any([x1 < y1,x2 > y2]))

