a=int(input("Enter 1st Number: "))
operator=input("Enter operator(+, -, *, /): ")
b=int(input("Enter 2nd Number: "))

def calculate(a, operator, b):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '/':
        if b != 0:
            return a / b
        else:
            print("Division by 0 is impossible")

     
    elif operator == '*':
        return a * b




print(calculate(a, operator, b))