# Data type in Python
# 1. None
# 2. Numeric
# 3. List
# 4. Tuple
# 4. Set
# 4. String
# 4. Range
# 5. Math
# 6. Dictionary


# 1. None: None is like to be null

# 2 Numeric : int, float, complex, bool

n = 3
print(type(n))
f = 3.5
print(type(f))
c = n-9j
print(type(c))
b = n < f
print(type(b))


# Convert variable type to another data type

a = 3.4

b = int(a)
print(b)

b = complex(a)
print(b)

# 3. Sequence like List, Tuple, Set, String, Range

number = [2, 3, 4]
print(type(number))

number = (2, 3, 4)
print(type(number))

number = {2, 3, 4}
print(type(number))

string = 'string';
print(type(string))

print(type(range(10)))

# Get Even number by range
print(list(range(2, 10, 2)))


