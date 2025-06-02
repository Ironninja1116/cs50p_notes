#Section 4 Notes Section 3

import sys

#using command-line arguments, and basic error handling
'''
try:
    print("hello, my name is", sys.argv[1], sys.argv[2])
    print(sys.argv)
except IndexError:
    print("Error: Not enough arguments were provided")
'''

#different form of exception handling
'''
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])
'''

#sys.exit to end program early
'''
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])
'''

#handles multiple names, uses a slice to skip index 0
print("hello, my name is ", end="")
for arg in sys.argv[1:]:
    print (arg, end=" ")


