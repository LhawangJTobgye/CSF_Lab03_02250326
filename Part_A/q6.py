print("Menu:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

if choice == 1:
    print("Result:", x + y)
elif choice == 2:
    print("Result:", x - y)
elif choice == 3:
    print("Result:", x * y)
elif choice == 4:
    if y != 0:
        print("Result:", x / y)
    else:
        print("Cannot divide by zero")
else:
    print("choice is not available")

# Shows a menu for addition, subtraction, multiplication, division. #
# Uses if-elif-else to select the operation. #
# Checks division by zero. #