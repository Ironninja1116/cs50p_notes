#Practice Set 1 Problem 4

def math(left, operation, right):
    #match statement to seperate functionality based on operator
    match(operation):
        case "+":
            print(f"{(left+right):.1f}")
        case "-":
            print(f"{(left-right):.1f}")
        case "*":
            print(f"{(left*right):.1f}")
        case "/":
            print(f"{(left/right):.1f}")
        

def main():
    #take in expression
    expression = input("Expression: ")

    #split into 3 seperate parts
    L = float(expression[:expression.index(" ")])
    expression = expression[expression.index(" ")+1:]
    O = expression[:expression.index(" ")]
    expression = expression[expression.index(" ")+1:]
    R = float(expression)

    #call math function
    math(L, O, R)

main()