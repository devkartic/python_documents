# input from cmd
# argv(Filename, param1, param3, param3, ...)  [0, 1, 2, 3, ...]
# run cmd $python command.py 5 6 for bellow the program

import sys

x = int(sys.argv[1])
y = int(sys.argv[2])

z = x + y

print(z)




