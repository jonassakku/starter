"""Simple calculator demo for Git practice."""

def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return a minus b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def power(a: float, b: float) -> float:
    """Return a raised to the power of b."""
    return a ** b


def divide(a: float, b: float) -> float:
    """Return a divided by b. Raises ZeroDivisionError if b is 0."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def modulo(a: float, b: float) -> float:
    """Return the remainder of a divided by b."""
    return a % b


if __name__ == "__main__":
    print("=== Calculator Demo ===")
    print(f"add(2, 3)      = {add(2, 3)}")
    print(f"subtract(5, 2) = {subtract(5, 2)}")
    print(f"multiply(4, 3) = {multiply(4, 3)}")
    print(f"divide(10, 2)  = {divide(10, 2)}")
    print(f"power(2, 3)    = {power(2, 3)}")
    print(f"modulo(10, 3)  = {modulo(10, 3)}")
