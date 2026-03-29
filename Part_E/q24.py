#  First we Define functions for operations #
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot be divided by zero"

# Then, write the code for the Main program loop #
while True:
    print("\noptions:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 5:
        print("Exiting the calculator. Thanks for using me!")
        break

    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    if choice == 1:
        print("Result:", add(number1, number2))
    elif choice == 2:
        print("Result:", subtract(number1, number2))
    elif choice == 3:
        print("Result:", multiply(number1, number2))
    elif choice == 4:
        print("Result:", divide(number1, number2))
    else:
        print("Invalid choice. Please select from options 1-5.")

# Functions defined for each operation. #
# while True loop keeps showing menu until user selects Exit. #
# Calls the appropriate function based on user choice. #
# Handles division by zero. #