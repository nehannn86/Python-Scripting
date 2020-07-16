#working with multiple variables & string in print statement.

var1 = 5
var2 = 10.0
var3 = 'Python Scripting'
var4 = 10 + 20j

print('Printing multiple variables belove in a single print statement:')
#1st Method
print("1st Method:")
print(f'Variable1: {var1} , Variable2: {var2} , Variable3: {var3} , Variable4: {var4}')
#2nd Method
print("2nd Method:")
print('Variables: ', var1,var2,var3,var4)
#3rd Method
print('3rd Method')
print('{} {} {} {}'.format(var1,var2,var3,var4))

