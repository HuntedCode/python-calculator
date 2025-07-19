num, num2, total = 0, 0, 0
accepted_operators = {"+", "-", "*", "/", "%", "^"}

def get_input_number():
    while(True):
        num = input("Please enter a number: ")
        if num.isnumeric():
           return float(num)
        else:
            print("That is not a valid number!")

def get_input_operator():
    while(True):
        operator = input("Please enter an operator (+, -, *, /, %, ^): ")
        if operator in accepted_operators:
            break
        else:
            print("That is not a valid operator!")
    
    return operator

def check_divide_by_zero(operator, operand):
    if (operator == "/" and operand == 0):
        return False
    else:
        return True

def perform_calculation(current_total, operator, operand):
    new_total = 0

    match operator:
        case "+":
            new_total = current_total + operand
        case "-":
            new_total = current_total - operand
        case "*":
            new_total = current_total * operand
        case "/":
            new_total = current_total / operand
        case "%":
            new_total = current_total % operand
        case "^":
            new_total = current_total ** operand
    
    return new_total

total = get_input_number()
operator = get_input_operator()

while(True):
    num = get_input_number()
    if (check_divide_by_zero(operator, num)):
        break
    else:
        print("Cannot divide by 0!")

total = perform_calculation(total, operator, num)

print("Total: " + str(total))