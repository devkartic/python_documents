# if block python called if suite
# Blocks define an indentation, like tab = 4 spaces
# Also we can use brackets but it optional in python
# Example with nested loops

number = 6
result = number % 2

if result == 0:
    print('Even number')
    if number > 6:
        print('Greater than 6')
    elif number < 6:
        print('Less than 6')
    else:
        print('Equal to 6')
else:
    print('Odd number')

print('Bye')

