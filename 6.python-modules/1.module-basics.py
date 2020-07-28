#!/usr/bin/python3

#working with modules.

#list all default modules of python.
print('Modules of Python:\n',help('modules'))

#to import module
import math

#to list particular modules documentation. 
print('Documentation of math module:\n',help('math'))

#list all the operations of module.
print('All the functions of math module:\n',dir(math))

#to use function/variable of module.
('Using pow function of math module:\n')
num = 5
print('Number: ',num)
print(f'Square of {num} is:',pow(num,2))
