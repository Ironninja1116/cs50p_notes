# Section 2 Notes Segment 3

def main():
    #print_column(3)
    #print_row(4)
    print_square(3)

def print_column(height):
    for _ in range(height):
        print("#")

def print_row(width):
    print("?" * width)

def print_square(size):
    #for each row in square
    for _ in range(size):
        #for each brick in row
        for _ in range(size):
            #print brick
            print("#", end="")
        print("\n", end="")

main()