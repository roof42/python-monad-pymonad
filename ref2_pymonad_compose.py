from pymonad.either import Left, Right
from pymonad.tools import curry
# Function to parse an integer
def parse_int(value):
    try:
        return Right(int(value))
    except ValueError as e:
        return Left(f"Error parsing integer: {e}")

# Function to square a number
def square(value):
    return value ** 2

# Function to convert a string to uppercase
def string_template(value):
    return f"FINAL RESULT {value}"

# Example usage
result = Right('5').then(parse_int).then(square).then(string_template)

print(result)
