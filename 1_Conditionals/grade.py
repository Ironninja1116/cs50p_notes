# Notes segment 2

score = int(input("Score: "))

if 90 <= score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")  
elif score >= 70 and score < 80:
    print("Grade: C")  
elif score >= 60 and score < 70:
    print("Grade: D")  
elif score >= 0 and score < 60:
    print("Grade: F")  
else:
    print("Invalid, must be a number between 0 and 100")