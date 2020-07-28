#!/usr/bin/python3

#implementing os module.
import os
import sys

os.system('clear')
path = '/home/ec2-user/Python-Scripting'

print('***OS Module***'.center(os.get_terminal_size().columns).title())
print('\nDefault Seperator: ',os.sep)
print('\nCurrent Working Directory: ',os.getcwd())
print(f'\nChange Directory To: {path}',os.chdir(path))
print('\nCurrent Working Directory: ',os.getcwd())
print('\nCreate Directory: ',os.mkdir('new-directory'))
print('\nList Directory: ',os.listdir())
print('\nRename Directory: ',os.rename('new-directory','directory'))
print('\nList Directory: ',os.listdir())
print('\nRemove Newly Created Directory: ',os.rmdir('directory'))
print('\nList Directory: ',os.listdir())
print('\nUser Id: ',os.getuid())
print('\nProcess Id: ',os.getpid())
print('\nGroup Id: ',os.getgid())
print('\n Environment Variables:\n')
for i in os.environ:
    print(i,'=',os.environ.get(i))

