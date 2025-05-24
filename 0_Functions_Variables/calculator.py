# Notes relating to variables, functions, operations, etc.

#x = float(input("What's x? "))
#y = float(input("What's y? "))

# z = round(x/y,2)
# print(z)

#z = x/y
#print(f"{z:.2f}")

# rounding to whatever decimal place is listed on right side
# print(round(x+y,0))

# z = round(x + y)

# print(f"{z:,}")


# practicing return values

def square(number):
    return number**2 #number*number OR pow(number,2) would also work

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

main()