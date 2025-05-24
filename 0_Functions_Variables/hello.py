# Notes relating to variables, functions, fstrings, etc.

# Asks user for their name || also, use the string methods we just learned
# name = input("What's your name? ").strip().title()

# remove whitespace from str
# name = name.strip()

# Capitalize user's name
# name = name.capitalize()
# name = name.title()

# Split user's name into first name and last name
# first, last = name.split(" ")

# Says hello to user
# print(f"hello, {name}")

# Printing quotes
# print("hello, \"friend\"")

#how to define your own function
def hello(person="world"):
    print("Hello", person)

def main():
    name = input("What's your name? ")
    hello(name)

main()