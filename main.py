while True:

    user_input = input("Simple Calculator: ")

    if "+" in user_input:
        parts = user_input.split("+")
        result = int(parts[0].strip()) + int(parts[1].strip())
        print(result)
    elif "-" in user_input:
        parts = user_input.split("-")
        result = int(parts[0].strip()) - int(parts[1].strip()) 
        print(result)
    elif "x" in user_input:
        parts = user_input.split("x")
        result = int(parts[0].strip()) * int(parts[1].strip())
        print(result)
    elif "/" in user_input:
        parts = user_input.split("/")
        result = int(parts[0].strip()) / int(parts[1].strip())
        print(result)

    
    if user_input == 'quit':
        print("Goodbye")
        break