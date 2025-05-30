#Practice Set 3 Problem 4

months = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
         ]

#split into month, day, and year
while True:
    date = input("Date: ")
    dateList = date.split("/")
    #spacing format
    if len(dateList) != 3:
        dateList = date.split(" ")
        if len(dateList) != 3:
            continue
        #spacing format starts here
        if dateList[0] not in months or not (31 >= int(dateList[1][0]) >= 0):
            continue
        print(f"{dateList[2]}-{dateList[0]}-{dateList[1][0]} ")
        break
    #slash format
    #month and day must be valid
    if not(12 >= int(dateList[0]) >= 1) or not(31 >= int(dateList[1]) >= 1):
        continue
    print(f"{dateList[2]}-{dateList[0]}-{dateList[1]} ")
    break