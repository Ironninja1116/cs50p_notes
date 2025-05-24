# Notes segment 4

name = input("What's your name? ")


#if elif else
if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Gryffindor")
else:
    print("Who?")
       

#vs equivalent match statement
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

