#Practice Set 2 Problem 1

#take in intiial camelCase input
camelVersion = input("camelCase: ")

#turn into list
camelList = list(camelVersion)
snakeList = list(camelVersion)

#iterate through lists and update the snakelist to replace each capital letter with _lowercase
#offset tracks how many extra characters are in snakeList because of the added underscores
offset = 0
for i in range(len(camelList)):
    if camelList[i] != camelList[i].lower():
        snakeList[i+offset:i+offset+1] = "_" + camelVersion[i].lower()
        offset += 1

#final output
print("snake_case: ", end="")
#print out each char in snakeList
for letter in snakeList:
    print(letter, end="")

