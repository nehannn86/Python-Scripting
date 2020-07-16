#working with input and output syntax.

num1 = int(input('\nEnter Number1: '))
num2 = eval(input('Enter Number2: '))
add = num1 + num2
sub = num1 - num2

print(f'\nGiven Number1: {num1}\nGiven Number2: {num2}')
print(f'Addition of {num1} & {num2} is: {add}\nSubstraction of {num1} & {num2} is: {sub}')
