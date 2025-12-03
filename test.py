# AI Review: The 'subtract' function is incorrectly named 'subtrcat'. It should be 'subtract' to match the operation.
def add(a, b):
    return a + b

def subtrcat(a, b):
    return a - b

# AI Review: The 'subtract' function is missing. It should be defined to handle subtraction.
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
            # AI Review: The 'subtract' function is incorrectly referenced as 'subtract' instead of 'subtrcat'.
            result = subtract(num1, num2)
        
        elif operator == '/':
            result = divide(num1, num2)
       
        else:
            print("⚠️ Invalid operator. Use +, -, *, or /.\n")
            continue

        print(f"Result: {result}\n")

# Progress Analysis:
# - Addition: 100%
# - Subtraction: 0% (function not defined correctly)
# - Multiplication: 0% (missing implementation)
# - Division: 100%
# Overall progress: 50% (2 out of 4 operations implemented correctly)