
# Calculation Functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
# Input Handling Function
def perform_calculation():
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = add(num1, num2)
        elif operator == "-":
            result = subtract(num1, num2)
        elif operator == "*":
            result = multiply(num1, num2)
        elif operator == "/":
            result = divide(num1, num2)
        else:
            print("Invalid operator!")
            return

        print("Result:", result)

    except ValueError:
        print("Invalid input! Please enter numbers only.")
# Main Menu
def calculator_menu():
    while True:
        print("\n--- Simple Calculator ---")
        print("1. Perform Calculation")
        print("2. Clear")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            perform_calculation()
        elif choice == "2":
            print("Calculator cleared.")
        elif choice == "3":
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

calculator_menu()
