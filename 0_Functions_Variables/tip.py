# Problem set 0, Problem 5

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    stringDollars = d.replace("$","",-1)
    return float(stringDollars)

def percent_to_float(p):
    stringPercent = p.replace("%","",-1)
    return float(stringPercent) / 100

main()