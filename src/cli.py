try:
    from math_operations import multiply
except ImportError:
    from src.math_operations import multiply

def main():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"Calculation Result: {a} * {b} = {multiply(a, b)}")

if __name__ == "__main__":
    main()
