

def calculate(a, operator, b):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '/':
        if b != 0:
            return a / b
        else:
            print("Error: Division by zero")
    elif operator == '*':
        return a * b

    else:
        return "invalid input"







while True:
    a=int(input("Enter 1st Number: "))
    operator=input("Enter operator(+, -, *, /): ")
    b=int(input("Enter 2nd Number: "))

    result = calculate(a, operator, b)
    print("result: ", result)

    repeat = input("Run again? (y/n): ").strip().lower()
    if repeat != 'y':
        print("Goodbye")
        break
  
    