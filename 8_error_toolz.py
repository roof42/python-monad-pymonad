from toolz import curry
# Define a curried function for division
@curry
def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError as e:
        raise ValueError(f"Error: {e}")

try:
    result = divide(10)(0)
except ValueError as e:
    print(f"Error handling: {e}")
