#!/usr/bin/python3

#implementing os.system() module.
#Create platform independent script for listing present working directory and list of files in a directory.
import os
import platform

print('***OS.SYSTEM() MODULE***'.center(os.get_terminal_size().columns))
if platform.system()=='Windows':
      print('Present Working Directory')
      os.system('echo %CD%')
      print('List Directory:')
      os.system('dir')
else:
      print('Present Working Directory:')
      os.system('pwd')
      print('List Directory Files:')
      os.system('ls -lhrt')
