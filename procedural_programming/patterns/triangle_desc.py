# Triangle descending pattern in python
# range(n) function means 0 to n

number = 4

for i in range(number):
    for j in range(number-i):
        print('# ', end='')
    print()



