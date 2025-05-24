#Practice Set 1 Problem 2

# ask for and assign greeting, also, use strip to remove leading whitespace, and make lowercase
greeting = input("enter a greeting: ").strip().lower()


# determine what condition greeting falls under and output money accordingly
if greeting[0:5] == "hello":
    print("$0")
elif greeting[0] == "h":
    print("$20")
else:
    print("$100")



