import os
os.system("clear")

mystring='Python Scripting version:3.8'
print('\n Original String:', mystring)
print('\n Check Boolean value of string?:', bool(mystring))
print('\n Check EndsWith G?:', mystring.endswith("G"))
print('\n Check StartsWith P?:', mystring.startswith("P"))
print('\n Check Is Upper?:', mystring.isupper())
print('\n Check Is Title?:', mystring.istitle())
print('\n Check Is Lower?:', mystring.islower())
print('\n Check Is Lower?:', mystring.islower())
print('\n Check Is Space?:', mystring.isspace())
mynewstring=' '
print('\n New String:', mynewstring)
print('\n Check Is Space?:', mynewstring.isspace())
print('\n Check Is Alpha?:',mystring.isalpha())
print('\n Check Is AlphaNum?:', mystring.isalnum())
print('\n Check Is Numeric?:',mystring.isnumeric())
