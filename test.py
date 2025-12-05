# Missing implementation for multiplication operation.
# AI Review: The multiplication operation is not implemented; add a function for multiplication.

def add(a, b):
    return a + b

# AI Review: Function name is misspelled; should be 'subtract' instead of 'subtrcat'.
def subtrcat(a, b):
    return a - b

# AI Review: The correct function name 'subtract' should be used here.
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
            # AI Review: Function name is misspelled; should be 'subtract' instead of 'subtrcat'.
            result = subtract(num1, num2)
        
        elif operator == '/':
            result = divide(num1, num2)
       
        else:
            print("⚠️ Invalid operator. Use +, -, *, or /.\n")
            continue

        print(f"Result: {result}\n")

# Progress: 50% (Add, divide implemented; subtract function has a spelling error and is not called correctly; multiplication is missing.)