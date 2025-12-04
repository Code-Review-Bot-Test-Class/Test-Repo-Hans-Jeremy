# Missing requirement: The program should implement multiplication.
# Missing requirement: The function name for subtraction is misspelled.
# AI Review: The function name should be corrected to 'subtract' to match the call in the main function.
# AI Review: The multiplication operation is not implemented; add a function for multiplication and handle it in the main function.

def add(a, b):
    return a + b

def subtrcat(a, b):
    return a - b
    

def divide(a, b):
    return a / b

def main():
    print("🧮 Simple Calculator")
    print("Operations: +, -, *, /")

    while True:
        num1 = input("Enter the first number (or 'q' to quit): ")
        
        if num1.lower() == 'q':
            print("Goodbye!")
            break
        
        num2 = input("Enter the second number: ")
        operator = input("Enter an operator (+, -, *, /): ")

        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("⚠️ Invalid number. Try again.\n")
            continue

        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)  # AI Review: This should call 'subtrcat' instead of 'subtract'.
        
        elif operator == '/':
            result = divide(num1, num2)
       
        else:
            print("⚠️ Invalid operator. Use +, -, *, or /.\n")
            continue

        print(f"Result: {result}\n")

# Progress analysis:
# - Addition: 100%
# - Subtraction: 0% (function name misspelled)
# - Multiplication: 0% (not implemented)
# - Division: 100%
# Overall progress: 50%