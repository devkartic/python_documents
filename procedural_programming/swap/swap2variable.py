# swap into 2 variable

a = 5
b = 7

print(a, b)

# Swap with 3rd variable
temp = a
a = b
b = temp

print(a, b)

# Swap without 3rd variable
a = a + b
b = a-b
a = a-b

print(a, b)

# Swap in python. Note : Rote 2 in python
a, b = b, a
print(a, b)

