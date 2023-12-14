from pymonad.either import Left, Right

def divide(a, b):
    return Right(a/b) if b != 0 else Left("Error: Division by zero")

# Example usage
result = divide(10, 2)  # Result: Right(5.0)
result = divide(10, 0)  # Result: Left('Error: Division by zero')

print(result)