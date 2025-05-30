#Practice Set 3 Problem 3

#make empty list and dictionary
groceryDict = {}
groceryList = []

#add items one per line, while loop until ctrl+d is pressed
while True:
    try:
        #flag to determine whether or not to skip the second half of the for loop
        skip = False
        currentItem = input("")
        #check if existing item
        for item in groceryList:
            if currentItem.lower() == item.lower():
                #if matching item is found
                groceryDict[currentItem.lower()] += 1
                skip = True
                break
        #do if no items are matching
        if skip:
            continue
        groceryDict[currentItem.lower()] = 1
        groceryList.append(currentItem.lower())
    #if ctrl+d pressed
    except EOFError:
        #sorts alphabetically
        groceryList.sort()
        for item in groceryList:
            print(f"{groceryDict[item]} {item.upper()}" )
        break

