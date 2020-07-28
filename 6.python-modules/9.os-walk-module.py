#!/usr/bin/python3

#implementing os.walk() in python.

import os

os.system('clear')
path = '/home/ec2-user/Python-Scripting/6.python-modules/walk'
#print(list(os.walk(path)))
print('\n')
print("***Print Each Path's Directory and files***\n".center(os.get_terminal_size().columns))
for p,d,f in os.walk(path):
    print('Path:',p)
    print('\tDirectories:',d)
    print('\tFiles:',f)
    print('\n')
print("***Print list of files for each path***\n".center(os.get_terminal_size().columns).title())
for p,d,f in os.walk(path):
    if len(f)!=0:
        print('Path:',p)
        for files in f:
            print('\tFile:',os.path.join(p,files))
