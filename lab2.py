num1String = input("Enter a number: ")
num1 = int(num1String)
operatorString = input("Enter an operator: ")
num2String = input("Enter another number: ")
num2 = int(num2String)

operators = {
    "+": (num1String + " + " + num2String + " = " + str(num1+num2)),
    "-": (num1String + " - " + num2String + " = " + str(num1-num2)),
    "*": (num1String + " * " + num2String + " = " + str(num1*num2)),
    "/": (num1String + " / " + num2String + " = " + str(num1/num2)),
    "%": (num1String + " % " + num2String + " = " + str(num1%num2)),
    "^": (num1String + " ^ " + num2String + " = " + str(num1**num2))
}

if operators.get(operatorString) is not None:
    print(operators.get(operatorString))
else:
    print("Error, " + operatorString + " is not a valid operator.")

# more efficient way to do it:
# match operatorString:
#     case "+":
#         print(num1String + " " + operatorString + " " + num2String + " = " + str(num1+num2))
#     case "-":
#         print(num1String + " " + operatorString + " " + num2String + " = " + str(num1-num2))
#     case "*":
#         print(num1String + " " + operatorString + " " + num2String + " = " + str(num1*num2))
#     case "/":
#         print(num1String + " " + operatorString + " " + num2String + " = " + str(num1/num2))
#     case "%":
#         print(num1String + " " + operatorString + " " + num2String + " = " + str(num1%num2))
#     case "^":
#         print(num1String + " " + operatorString + " " + num2String + " = " + str(num1**num2))
#     case _:
#         print("Error, " + operatorString + " is not a valid operator.")
