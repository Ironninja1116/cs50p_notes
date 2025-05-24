# Notes segment 3

'''
def evenOrOdd(x):
    if x % 2 == 0:
        print(f"{x} is even")
    else:
        print(f"{x} is odd")
'''

#one line way of doing this function, "pythonic statement"
def evenOrOdd(x):
    return (x % 2 == 0)

def main():
    x = int(input("What's x? "))
    evenOrOdd(x)

main()

