# Variable in python

num = 5;

# Get variable address

address = id(num)

# if multiple variable hold same value then those variable are in same address.
# That's why python is more memory efficient.
# For get type of variable use type()

a = 10
b = a
address_of_a = id(a)
address_of_b = id(b)
address_of_10 = id(10)
print(address_of_a, address_of_b, address_of_10)

# a change value 10 to 8
a = 8
# a change value 10 to 15
b = 15
# 10 is still now allocated in memory as garbage collection
print(id(a), id(b), id(10))

