# Section 2 Notes Segment 1

#while loop
'''
i = 3
while i != 0:
    print("meow")
    i -= 1
'''

#bad for loop
'''
for i in [0,1,2]:
    print("meow")
'''

#good for loop using range, equivalent to top
'''
for i in range(3):
    print("meow")
'''

#best practice, since i doesn't really represent anything
'''
for _ in range(3):
    print("meow")
'''

#not as important, but also equivalent
'''
print(("meow" + "\n") * 3, end="")
'''

#input validation - ensures positive value
'''
while True:
    n = int(input("What's n? "))
    if n > 0:
        break
    
for _ in range(n):
    print("meow")
'''

#every concept up to this point put together
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")

main()

