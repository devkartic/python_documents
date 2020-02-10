# For else in python
# Break statement in for must required

numbers = [5, 10, 15, 20, 25]

for number in numbers:
    if number % 7 == 0:
        print(number, '', end='')
        break
else:
    print('Not Found')


