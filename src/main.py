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


if __name__ == "__main__":
    print("Calculator demo")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
    print(f"4 * 3 = {multiply(4, 3)}")
    print(f"2 ** 3 = {power(2, 3)}")