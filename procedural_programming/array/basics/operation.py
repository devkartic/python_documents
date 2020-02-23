# operation with array

from array import *

# For number array type integer 'i'
numbers = array('i', [3, 4, 5, 6, 7])

# new array create squire of each element of array
newNumbers = array('i', (a*a for a in numbers))

# use for loop
for e in newNumbers:
    print(e, '', end='')

print()

# use while loop for printing array
e = 0
while e < len(newNumbers):
    print(newNumbers[e], '', end='')
    e += 1




