#Implementing IF statement.
import os 
os.system('clear')
ts = os.get_terminal_size().columns
print('***If Else Statement**i*')
print('Comparing two numbers: ')
usrinput1 = eval(input('Enter first number: '))
usrinput2 = eval(input('Enter second number: '))
if usrinput1 == usrinput2:
    print(f'Both the numbers are Equal.')
else: 
    print(f'Both the numbers are Not Equal.')
    


