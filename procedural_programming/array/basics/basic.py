# Array in python

from array import *
# import array as arr


names = array('i', [3, 4, 5, 6, 7])

# len() returns size of array size
print(len(names))

# buffer_info() returns address and array size
print(names.buffer_info())

# typecode property returns array type
print(names.typecode)

# reverse() use for getting array reverse order, but not return any values. It's return None.
names.reverse()
print(names)




