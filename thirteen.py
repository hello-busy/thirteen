#!/usr/bin/env python3
"""
A program that demonstrates the number thirteen in various formats.
"""

def show_thirteen():
    """Display the number thirteen in various formats."""
    number = 13
    
    print("The Number Thirteen")
    print("=" * 20)
    print(f"Decimal: {number}")
    print(f"Binary: {bin(number)}")
    print(f"Hexadecimal: {hex(number)}")
    print(f"Octal: {oct(number)}")
    print(f"Roman: {to_roman(number)}")
    print(f"English: {to_english(number)}")
    print(f"Squared: {number ** 2}")
    print(f"Is Prime: {is_prime(number)}")

def to_roman(num):
    """Convert number to Roman numerals."""
    if num == 13:
        return "XIII"
    return str(num)  # Simple implementation for 13

def to_english(num):
    """Convert number to English word."""
    if num == 13:
        return "thirteen"
    return str(num)  # Simple implementation for 13

def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    """Main function to run the program."""
    show_thirteen()

if __name__ == "__main__":
    main()