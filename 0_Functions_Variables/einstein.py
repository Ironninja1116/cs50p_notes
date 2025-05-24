# Problem set 0, Problem 4

# remember, input returns a string

def main():
    c = 300000000
    m = input("Enter mass in kilograms (round to nearest whole number): ")
    E = int(m) * pow(c,2)
    print(f"{E}")

main()