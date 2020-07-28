#!/usr/bin/python3

#implementing getpass module.

import os
import getpass
print(os.system('clear'))
print('***getpass module***'.center(os.get_terminal_size().columns).title())
print('UserName: ',getpass.getuser())
usrpass = getpass.getpass(prompt = 'Enter Your Password: ')
print('Password entered by you: ', usrpass)
