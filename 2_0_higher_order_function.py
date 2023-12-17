#-------------------------------------------------------------
#Higher order function
#-------------------------------------------------------------
def apply_operation(operation, x, y):
    return operation(x, y)

# Binary operation functions
def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

# Usage of the higher-order function
result_addition = apply_operation(add, 3, 4)
result_multiplication = apply_operation(multiply, 3, 4)
