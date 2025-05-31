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
        #removing comma from month, but first make sure a comma is actually there
        try:
            dateList[1] = dateList[1][:dateList[1].index(",")]
        except ValueError:
            continue
        if dateList[0] not in months or not (31 >= int(dateList[1]) >= 0):
            continue
        print(f"{int(dateList[2]):04d}-{months.index(dateList[0])+1:02d}-{int(dateList[1]):02d} ")
        break
    #slash format
    #month and day must be valid
    try:
        if not(12 >= int(dateList[0]) >= 1) or not(31 >= int(dateList[1]) >= 1):
            continue
        print(f"{int(dateList[2]):04d}-{int(dateList[0]):02d}-{int(dateList[1]):02d} ")
        break
    except ValueError:
        continue