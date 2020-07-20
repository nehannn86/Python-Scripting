#implementing assignment operators.
import os

os.system("clear")
a = 21
b = 10
c = 0
print('***Assignment Operators***')
print(f'Value of a: {a}\nValue of b: {b}\nValue of c: {c}')
c = a + b
print("c = a + b: ",c)

c += a
print("c += a:  ", c) 

c -= a
print("c -= a: ", c) 

c *= a
print("c *= a: ", c) 

c /= a 
print("c /= a: ", c) 

c  = 2
print("c = 2")

c %= a
print("c %= a: ", c)

c **= a
print("c **= a: ", c)

c //= a
print("c //= a: ", c)


