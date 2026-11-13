"""Introductory examples of defining, calling, and returning from functions."""


def greet(name, greeting="Hello"):
    """Return a greeting for the given name."""
    return f"{greeting}, {name}!"


def calculate_total(unit_price, quantity):
    """Return the cost of a quantity of items before any discount."""
    return unit_price * quantity


def apply_discount(total, discount_percent=0):
    """Return a total after applying a percentage discount."""
    return total - total * discount_percent / 100


print(greet("Python learner"))
print(greet("Python learner", "Welcome"))

subtotal = calculate_total(12.50, 4)
print(f"Subtotal: {subtotal:.2f}")
print(f"After 10% discount: {apply_discount(subtotal, 10):.2f}")
print(f"Without a discount: {apply_discount(subtotal):.2f}")

# Practice: write a function that converts a temperature from Celsius to
# Fahrenheit, then call it with a few different values.