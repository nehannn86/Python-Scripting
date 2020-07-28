#!/usr/bin/python3

#implementing os.path() module.
import os.path

print('Default Seperator os System: ',os.path.sep)
print('Basename of given path: ',os.path.basename('/home/ec2-user/Python-Scripting'))
print('Directory name of given path: ',os.path.dirname('/home/ec2-user/Python-Scripting'))
print('Join Path of two different: ',os.path.join('/home/ec2-user','Python-Scripting/1.basics'))
print('Split given path: ',os.path.split('/home/ec2-user/Python-Scripting/1.basics'))
print('Size of given path: ',os.path.getsize('/home/ec2-user/Python-Scripting'))
print('Check if given path exist: ',os.path.exists('/home/ec2-user/Python-Scripting'))
print('Check if it is file: ',os.path.isfile('/home/ec2-user/Python-Scripting/1.basics/1.first_script.py'))
print('Check if it is file: ',os.path.isfile('/home/ec2-user/Python-Scripting/1.basics/first_script.py'))
print('Check if it is dir: ',os.path.isdir('/home/ec2-user/Python-Scripting/1.basics/1.first_script.py'))
print('Check if it is dir: ',os.path.isdir('/home/ec2-user/Python-Scripting/1.basics'))
print('Check if it is softlink: ',os.path.islink('/home/ec2-user/Python-Scripting/sflink'))
