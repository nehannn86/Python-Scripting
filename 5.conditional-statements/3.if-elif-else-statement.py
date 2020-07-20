#Implementing if...elif...else statement.
import os
os.system('clear')

print('***If...ElIf...Else***')
print('Arithmetic Calculator: ')
usrinput1 = int(input('Enter your First Number: '))
usrinput2 = int(input('Enter your Second Number: '))

operation = int(input('1. Addition\n2. Substraction\n3. Multiplication\n4.Division\nType your option number: '))

if operation == 1:
    print(f'Addition value of {usrinput1} and {usrinput2} is: ',usrinput1 + usrinput2)
elif operation == 2:    
    print(f'Substraction value of {usrinput1} and {usrinput2} is: ',usrinput1 - usrinput2)
elif operation == 3:    
    print(f'Multplication value of {usrinput1} and {usrinput2} is: ',usrinput1 * usrinput2)
elif operation == 4:    
    print(f'Divition value of {usrinput1} and {usrinput2} is: ',usrinput1 / usrinput2)
else:
    print('Please Type correct option number.')
