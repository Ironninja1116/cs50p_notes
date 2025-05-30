#Practice Set 3 Problem 2

menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
       }

#create variable for cost
totalCost = 0

#add items to menu, ignoring fake items
while(True):
    try:
        currentItem = input("Item: ")
        for item in menu:
            if item.lower() == currentItem.lower():
                totalCost += menu[item]
                print(f"Total: ${totalCost:.2f}")
                break
    #use EOFError to detect when ctrl+d is pressed
    except EOFError:
        break

