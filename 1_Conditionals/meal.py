#Practice Set 1 Problem 5

def main():
    time = input("What time is it? ")
    newTime = convert(time)
    if newTime >= 7 and newTime <= 8:
        print("breakfast time")
    elif newTime >= 12 and newTime <= 13:
        print("lunch time")
    elif newTime >= 18 and newTime <= 19:
        print("dinner time")

def convert(time):
    hour = float(time[:time.index(":")])
    minute =   float(time[time.index(":")+1:])
    newTime = hour + minute/60
    return newTime

if __name__ == "__main__":
    main()
