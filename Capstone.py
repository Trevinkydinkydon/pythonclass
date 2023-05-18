# Add function: adds two numbers together
def add(x, y):
    return x + y

# Subtract function: subtracts two numbers
def subtract(x, y):
    return x - y

# Multiply function: multiplies two numbers
def multiply(x, y):
    return x * y

# Divide function: divides two numbers
def divide(x, y):
    return x / y

# Modulo function: calculates the remainder of division
def modulo(x, y):
    return x % y

# Power function: calculates the power of a number
def power(x, y):
    return x ** y

# Square root function: calculates the square root of a number
def square_root(x):
    return math.sqrt(x)

# Logarithm function: calculates the logarithm of a number
def logarithm(x, base=10):
    return math.log(x, base)

# Main calculator loop
while True:
    # Display menu options
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulo")
    print("6. Power")
    print("7. Square Root")
    print("8. Logarithm")
    print("9. Exit")

    # Get user input for operation choice
    choice = input("Enter your choice (1-9): ")

    # Check the choice and perform the corresponding operation
    if choice == '1':
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("Result: ", add(num1, num2))
    elif choice == '2':
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("Result: ", subtract(num1, num2))
    elif choice == '3':
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("Result: ", multiply(num1, num2))
    elif choice == '4':
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if num2 == 0:
            print("Error: Cannot divide by zero")
        else:
            print("Result: ", divide(num1, num2))
    elif choice == '5':
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if num2 == 0:
            print("Error: Cannot perform modulo with zero")
        else:
            print("Result: ", modulo(num1, num2))
    elif choice == '6':
        num1 = float(input("Enter the base number: "))
        num2 = float(input("Enter the exponent: "))
        print("Result: ", power(num1, num2))
    elif choice == '7':
        num = float(input("Enter the number: "))
        print("Result: ", square_root(num))
    elif choice == '8':
        num = float(input("Enter the number: "))
        base = float(input("Enter the logarithm base (default is 10): "))
        print("Result: ", logarithm(num, base))
    elif choice == '9':
        print("Exiting")
