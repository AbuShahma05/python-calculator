while True:
    operation = input("\nChoose operation (+, -, *, /) or q to quit: ")

    if operation == "q":
        print("Calculator closed.")
        break

    if operation not in ["+", "-", "*", "/"]:
        print("Invalid operation. Please choose +, -, *, or /.")
        continue

    number = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    if operation == "+":
        print("Result:", number + number2)

    elif operation == "-":
        print("Result:", number - number2)

    elif operation == "*":
        print("Result:", number * number2)

    elif operation == "/":
        if number2 == 0:
            print("You cannot divide by zero.")
        else:
            print("Result:", number / number2)