#!/usr/bin/python3

#implementing platform module to get system information.
import os
import sys
import platform as p

ts = os.get_terminal_size().columns
print(os.system('clear'))
print('***platform module***'.center(ts).title())
print('System Details:\n')
print('SYSTEM ARCHITECTURE: ',p.architecture())
print('LIBC VERSION: ',p.libc_ver())
print('MACHINE: ',p.machine())
print('NODE: ',p.node())
print('PROCESSOR: ',p.processor())
print('PYTHON BUILD: ',p.python_build())
print('PYTHON COMPILER: ',p.python_compiler())
print('PYTHON IMPLEMENTATION: ',p.python_implementation())
print('PYTHON REVISION: ',p.python_revision())
print('PYTHON VERSION: ',p.python_version())
print('PYTHON VERSION TUPLE: ',p.python_version_tuple())
print('RE: ',p.re)
print('RELEASE: ',p.release())
print('SYSTEM: ',p.system())
print('UNAME: ',p.uname())
print('VERSION: ',p.version())
