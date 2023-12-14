from toolz import curry

# Define a curried function for division
@curry
def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError as e:
        raise ValueError(f"Error: {e}")

# Example usage
safe_divide = divide(10)  # Partial application

try:
    result = safe_divide(2)  # Result: 5.0
    result = safe_divide(0)  # Raises ValueError: Error: division by zero
except ValueError as e:
    print(f"Error handling: {e}")
