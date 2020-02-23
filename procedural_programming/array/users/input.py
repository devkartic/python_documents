# Array input from user

from array import *

numbers = array('i', [])

n = int(input('Enter the length of array '))

for e in range(n):
    num = int(input('Enter the next element '))
    numbers.append(num)

print(numbers)

# For searching user given index of value in array by manual function
searchValue = int(input('Enter the search element '))
i = 0
for e in numbers:
    if e == searchValue:
        print(e, 'stored in index of', i)
        break
    i += 1

# For searching user given index of value in array by build in function

print(numbers.index(searchValue))






