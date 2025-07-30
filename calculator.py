# calculator.py
# A simple calculator that performs +, -, *, / on two numbers.

def calculate():
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers (e.g., 10 or 3.5).")
        return

    op = input("Choose operation (+, -, *, /): ").strip()

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = a / b
    else:
        print("Invalid operation. Please choose +, -, *, or /.")
        return

    print(f"{a} {op} {b} = {result}")

if __name__ == "__main__":
    calculate()
