#!/usr/bin/env python3
"""
CLI Application for accepting two numbers and displaying their multiplication.
Can be executed interactively or via command-line arguments.
"""

import sys
import argparse
from math_operations import multiply


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Multiply two numbers (Problem Statement C - ML DevOps POE)"
    )
    parser.add_argument(
        "--num1", "-a", type=float, help="First number for multiplication", default=None
    )
    parser.add_argument(
        "--num2", "-b", type=float, help="Second number for multiplication", default=None
    )
    return parser.parse_args()


def interactive_mode():
    print("=" * 60)
    print(" ML DevOps POE - Problem Statement C: Number Multiplication ")
    print("=" * 60)
    try:
        raw_a = input("Enter the first number: ").strip()
        num1 = float(raw_a)
    except ValueError:
        print(f"Error: '{raw_a}' is not a valid number.")
        sys.exit(1)

    try:
        raw_b = input("Enter the second number: ").strip()
        num2 = float(raw_b)
    except ValueError:
        print(f"Error: '{raw_b}' is not a valid number.")
        sys.exit(1)

    # Convert to int if whole number
    if num1.is_integer():
        num1 = int(num1)
    if num2.is_integer():
        num2 = int(num2)

    result = multiply(num1, num2)
    print("-" * 60)
    print(f"Calculation : {num1} * {num2}")
    print(f"Result      : {result}")
    print("=" * 60)
    return result


def main():
    args = parse_arguments()

    if args.num1 is not None and args.num2 is not None:
        num1 = int(args.num1) if args.num1.is_integer() else args.num1
        num2 = int(args.num2) if args.num2.is_integer() else args.num2
        result = multiply(num1, num2)
        print(f"Multiplication Result: {num1} * {num2} = {result}")
        return 0
    else:
        interactive_mode()
        return 0


if __name__ == "__main__":
    sys.exit(main())
