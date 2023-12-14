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

print(result_addition)       # Output: 7
print(result_multiplication)  # Output: 12
#-------------------------------------------------------------
#Currying
#-------------------------------------------------------------
def plus(a):
    def add(b):
        return a + b
    return add

# Usage
result = plus(2)(3)
# Partial apply 
plusTwo = plus(2)
print(plusTwo(3))
