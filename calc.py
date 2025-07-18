num, num2, total = 0, 0, 0
accepted_operators = {"+", "-", "*", "/", "%", "^"}

while(True):
    num = input("Please enter a number: ")
    if(num.isnumeric()):
        num = float(num)
        break
    else:
        print("That is not a valid number!")
    
while(True):
    operator = input("Please enter an operator (+, -, *, /, %, ^): ")
    if operator in accepted_operators:
        break
    else:
        print("That is not a valid operator!")

while(True):
    num2 = input("Please enter a number: ")
    if(num2.isnumeric()):
        num2 = float(num2)

        if (operator == "/" and num2 == 0):
            print("Cannot divide by 0!")
            continue
        break
    else:
        print("That is not a valid number!")

match operator:
    case "+":
        total = num + num2
    case "-":
        total = num - num2
    case "*":
        total = num * num2
    case "/":
        total = num / num2
    case "%":
        total = num % num2
    case "^":
        total = num ** num2

print("Total: " + str(total))
       