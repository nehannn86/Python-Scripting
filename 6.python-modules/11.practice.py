#!/usr/bin/python3

#check if given path is file or directory.
import os.path
print(os.system("clear"))
path = input('Enter your path: ')

if os.path.exists(path) & os.path.isfile(path):
    print(f'Given path Exists at location: {path} and it is a file')
elif os.path.exists(path) & os.path.isdir(path):
    print(f'Given path Exists at location: {path} and it is a Directory')
elif os.path.exists(path) & os.path.islink(path):
    print(f'Given path Exists at location: {path} and it is a Soft Link')
else:
    print('Please provide valid path.')
