#Practice Set 1 Problem 1

#prompt user
answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

#ensure answer works case-insensitively
answer = answer.lower()

#check equivalency and output answer
if answer == "42" or answer == "forty-two" or answer == "forty two":
    print("Yes")
else:
    print("No")