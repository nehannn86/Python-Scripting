#!/usr/bin/python3

#create platform independent script for searching a file.

import os
import platform
import string

print('***Search file***'.center(os.get_terminal_size().columns).title())
req_file = input('Enter Your File Name: ')
if platform.system()=='Windows':
	pdrives = string.ascii_uppercase
	drives = []
	for i in pdrives:
		if os.path.exists(i +':\\'):
			drives.append(i+':\\')
	print(drives)
	for drive in drives:
		for p,d,f in os.walk(drive):
			for file in f:
				if file==req_file:
					print('File exists at:',os.path.join(p,file))
else:
	for p,d,f in os.walk('/'):
		for file in f:
			if file == req_file:
				print('File exist at:',os.path.join(p,file))
