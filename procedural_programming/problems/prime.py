# Prime number in python

number = 11

for num in range(2, int(number/2)):
    if number % num == 0:
        print('Not Prime')
        break
else:
    print('Prime')




