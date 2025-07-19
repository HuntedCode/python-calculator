num, num2, total = 0, 0, 0
accepted_operators = {"+", "-", "*", "/", "%", "^", ""}

def get_input_number():
    """Returns valid numerical input from user."""

    while(True):
        try:
            user_input = float(input("Please enter a number: "))
        except ValueError:
           print("That is not a valid number!")
        else:
            return user_input
            

def get_input_operator():
    """Returns valid mathematical operator from user."""

    while(True):
        operator = input("Please enter an operator (+, -, *, /, %, ^) or leave it blank to finish your calculation: ")
        if operator in accepted_operators:
            break
        else:
            print("That is not a valid operator!")
    
    return operator

def check_divide_by_zero(operator, operand):
    """Checks if user is dividng by 0 and returns True if detected."""

    if (operator == "/" and operand == 0):
        return True
    else:
        return False

def perform_calculation(current_total, operator, operand):
    """Performs mathematical calculation based on number and operator params."""
    
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

while(True):
    operator = get_input_operator()
    if operator == "":
        break
    
    input_num = 0

    while(True):
        input_num = get_input_number()
        if (check_divide_by_zero(operator, input_num)):
            print("Cannot divide by 0!")
        else:
            break

    total = perform_calculation(total, operator, input_num)

    print("Total: " + str(total))

print("Final total: ", str(total))