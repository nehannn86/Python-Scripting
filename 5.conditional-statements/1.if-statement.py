#Implementing IF statement.
import os 
os.system('clear')
ts = os.get_terminal_size().columns
print('***If Statement***')
usrinput = input('Enter your string: ')
usropt = int(input('1. Center Allignment\n2. Right Allignment\n3. Left Allignment\nType your option number: '))
if usropt == 1:
    print('$Center Allignment$\n',usrinput.center(ts).title())
if usropt == 2:
    print('$Left Allignment$\n',usrinput.ljust(ts).title())
if usropt == 3:
    print('$Right Allignment$\n',usrinput.rjust(ts).title())


