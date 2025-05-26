#Practice Set 2 Problem 2

#initial variables
accepted_list = [5, 10, 25]
total_paid = 0

#Loops until enough money is paid
while total_paid < 50:
    print(f"Amount Due: {50-total_paid}")
    currentCoin = int(input("Insert Coin: "))
    for coin in accepted_list:
        if currentCoin == coin:
            total_paid += currentCoin
            break

#Print change
print(f"Change Owed: {total_paid-50}")