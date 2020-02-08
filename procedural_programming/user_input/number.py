# By default input function return string type value. If we want any calculation on it then type conversion
# must be required

a = input('Enter the first number ')
print('Type of first input ', type(a))
a = int(a)
b = input('Enter the second number ')
print('Type of second input ', type(b))
b = int(b)

result = a + b

print(result)

