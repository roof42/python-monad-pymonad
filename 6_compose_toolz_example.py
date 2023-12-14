from toolz import pipe

# Define functions
def add_two(x):
    return x + 2

def multiply_by_three(x):
    return x * 3

def subtract_five(x):
    return x - 5

# Compose functions
basic = subtract_five(multiply_by_three(add_two(2)))
result = pipe(2, add_two, multiply_by_three, subtract_five)
print(basic)
print(result)
