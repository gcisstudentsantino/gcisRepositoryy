
def choose_operation():
    print("calculator menu")
    print("1. addition")
    print("2. substraction")
    print("3. multiplication")
    print("4. division")

    operation = int(input("choose option:"))
    return operation

def choose_operand(operand_number):
    operand = int(input(operand_number))
    return operand

def division_type():
    print("divison menu")
    print("1. integer division")
    print("2. regular division")
    division = int(input("choose division type"))
    return division_type

def preform_operation(operation, operand1, operand2):
    result = 0

    if operation == 1:
        result = operand1 + operand2
    elif operation == 2:
        result = operand1 - operand2
    elif operation == 3:
        result = operand1 * operand2
    elif operation == 4:
        div_type = get_division_type()
        if div_type == 1:
            result = operand1 // operand2
        else:
            result = operand1 / operand2

    return result

def main():

    operation = choose_operation()

    operand1 = choose_operand("first")
    operand2 = choose_operand("second")

    print("operands:", operand1, "and", operand2)

    result = preform_operation(operation, operand1, operand2)
    print(result)

main()


