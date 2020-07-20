#implementing arithmetic operators.
import os

os.system("clear")

def Addition(num1 , nume2): 
    Addition = num1 + num2
    print(f'Addition of {num1} & {num2} is: ',Addition)

def Substraction(num1, num2):
    Substraction = num1 - num2
    print(f'Substraction of {num1} & {num2} is: ',Substraction)

def Multiplication(num1, num2):
    Multiplication = num1 * num2
    print(f'Multiplication of {num1} & {num2} is: ',Multiplication)

def Division(num1, num2):
    Division = num1 / num2
    print(f'Division of {num1} & {num2} is: ',Division)

def Modulus(num1, num2):
    Modulus = num1 % num2
    print(f'Modulus of {num1} & {num2} is: ',Modulus)

def Floor_Division(num1, num2):
    FloorDivision = num1 // num2
    print(f'Floor Division of {num1} & {num2} is: ',Floor_Division)

def Exponential(num1, num2):
    Exponential = num1 ** num2
    print(f'Exponential of {num1} & {num2} is: ',Exponential)

print('***Arithmetic Operators***')
print('Chhose the operation to perform by typing option number:\n1. Addition\n2. Substraction\n3. Multiplication\n4. Division\n5. Modulus\n6. Floor Division\n7. Exponential')
option = int(input('Enter your Option: '))
num1=int(input('Enter Nmumber1: '))
num2=int(input('Enter Nmumber2: '))

if option == 1:
    Addition(num1, num2)
elif option == 2:
    Substraction(num1, num2)
elif option == 3:
    Multiplication(num1, num2)
elif option == 4:
    Division(num1, num2)
elif option == 5:
    Modulus(num1, num2)
elif option == 6:
    Floor_Division(num1, num2)
elif option == 7:
    Exponential(num1, num2)
else:
    print("Invalid Option...!")
    exit()




