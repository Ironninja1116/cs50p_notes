#Practice Set 3 Problem 1

def main():
    frac = input("Enter a fraction formatted as X/Y: ")
    perc = fracToPercent(frac)
    print(perc)

def fracToPercent(f):
    fraction = f
    while True:
        try:
            #split into numerator and denominator
            n = int(fraction[:fraction.index("/")])
            d = int(fraction[fraction.index("/")+1:])
            #divide into a percentage, and make sure its an int
            percent = round(n/d * 100)
            #convert to letter based on number, or reprompt if 
            if n > d:
                fraction = input("Invalid fraction. Try again: ")
                continue
            elif percent >= 99:
                return "F"
            elif percent <= 1:
                return "E"
            else:
                return str(percent) + "%"
        except ValueError:
            fraction = input("Invalid fraction. Try again: ")
        except ZeroDivisionError:
            fraction = input("Invalid fraction. Try again: ")

#make sure to call main function
main()