# Calculator + Recursion
# Add
def add(n1, n2):
    return n1+n2


# Subtract
def subtract(n1, n2):
    return n1-n2


# Multiply
def multiply(n1, n2):
    return n1*n2


# Divide
def divide(n1, n2):
    return n1/n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    def calculation_function(n1, n2):
        answer = operations[operation_symbol](n1=num1, n2=num2)
        return answer

    num1 = int(input("What's the first number?: \n"))
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick a symbol from the line above: ")
    num2 = int(input("What's the next number?: \n"))
    answer = operations[operation_symbol](n1=num1, n2=num2)
    # print(f"{num1} {operation_symbol} {num2} = {answer}")
    is_response = True
    while is_response == True:
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        repeat = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")
        if repeat == 'y':
            is_response = True
            operation_symbol = input("Pick a symbol from the line above: ")
            num2 = int(input("What's the next number?: \n"))
            num1 = answer
            print(num1)
            answer = calculation_function(n1=num1, n2=num2)
        elif repeat == 'n':
            is_response = False
            calculator()


calculator()

