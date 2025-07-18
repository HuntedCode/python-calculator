num, num2, total = 0, 0, 0
accepted_operators = {"+", "-", "*", "/", "%", "^"}

while(True):
    num = input("Please enter a number: ")
    if(num.isnumeric()):
        num = float(num)
        break
    
while(True):
    operator = input("Please enter an operator (+, -, *, /, %, ^): ")
    if operator in accepted_operators:
        break

while(True):
    num2 = input("Please enter a number: ")
    if(num2.isnumeric()):
        num2 = float(num2)
        break

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
       