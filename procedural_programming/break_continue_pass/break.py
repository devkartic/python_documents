# Break in python

available = 3

candy = int(input('How many candies you wand : '))
i = 1

while i < candy:
    if i > available:
        print('Out of stock!')
        break;

    print('candy')
    i += 1

print('Bye')



