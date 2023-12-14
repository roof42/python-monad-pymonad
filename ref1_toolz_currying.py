from toolz import curry

# Uncurried function
def add_three_numbers(x, y, z):
    return x + y + z

# Curried function using toolz.curry
curried_add = curry(add_three_numbers)

# Partial application
add_five = curried_add(2)(3)

# Full application
result = add_five(5)

print(result)  # Output: 10