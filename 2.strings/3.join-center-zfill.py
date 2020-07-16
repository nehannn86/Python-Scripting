
#getting terminal size using os module.

import os
tsize=os.get_terminal_size().columns
print('Terminal Size is:',tsize)

#getting original string

string='PYTHON SCRIPTING'
print('Original String:',string)

#using join() method

newstring = '-'.join(string)
print('New String created using Join() Function:',newstring)

#using center() method

print('Centered String:\n',string.center(tsize))
print('Left Sided String:\n',string.ljust(tsize))
print('Right Sided String:\n',string.rjust(tsize))

#using zfill() method

print('New String created using Zfill() Function:', newstring.zfill(40))
