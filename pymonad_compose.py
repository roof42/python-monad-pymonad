from pymonad.either import Left, Right

def then(either, func):
    return either.bind(func)

def to_int(s):
    try:
        return Right(int(s))
    except ValueError:
        return Left("Error: Cannot convert to int")

def add_five(x):
    return x + 5

def double(x):
    return x * 2

def to_string(x):
    return f"A{x}"

# Example usage using >>
result = (
    to_int("10")
    .then(double)
    .then(add_five)
    .then(to_string)
)

# Print the result or handle errors
print(result)