#Practice Set 2 Problem 4

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #make sure length of plate is 2-6 characters
    if not (2 <= len(s) <= 6):
        return False
    #make sure first two characters are letters (using isalpha())
    if not (s[0:2].isalpha()):
        return False
    #make sure all are letters/numbers (using isalnum())
    if not (s.isalnum()):
        return False
    #check for numbers in middle
    mode = "letters"
    for i in range(2,len(s)):
        if mode == "letters" and not s[i].isalpha():
            #first number cannot be 0
            if s[i] == "0":
                return False
            mode = "numbers"
        elif mode == "numbers" and s[i].isalpha():
            return False
    #if passed all conditions, return true
    return True

main()