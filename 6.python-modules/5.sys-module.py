#!/usr/bin/python3

#implementing sys module.

#importing modules
import os
import sys

if len(sys.argv) != 3:
    print('Usage:')
    print(f'<script name.py> <Your String Value> <upper|lower|title>')
    sys.exit()

usr_str = sys.argv[1]
usr_action = sys.argv[2]
os.system('clear')
print('***Using Sys modules***'.center(os.get_terminal_size().columns).title())
if usr_action == 'upper':
    print(usr_str.upper())
elif usr_action == 'lower':
    print(usr_str.lower())
elif usr_action == 'title':
    print(usr_str.title())
else:
    print('Your option is invalid,Please provide valid option: upper|lower|title')


