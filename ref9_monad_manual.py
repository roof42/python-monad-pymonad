class Maybe:
    def is_some(self):
        return self.__class__ == Some
    
class Some(Maybe):
    def __init__(self, value):
        self.value = value

    def bind(self, func):
        return func(self.value)

    def __str__(self):
        return f"Some({self.value})"
    
class Nothing(Maybe):
    def bind(self, func):
        return self

    def __str__(self):
        return f"Nothing"    

def divide(a, b):
    if b == 0:
        return Nothing()
    else:
        return Some(a / b)

result = (
    Some(10)
    .bind(lambda y: divide(y, 2))
    .bind(lambda y: divide(y, 0))  # This in Nothing
)

if result.is_some:
    print(f"Result is Right: {result}")
else:
    print(f"Result is {result}")

result = (
    Some(10)
    .bind(lambda y: divide(y, 0))
    .bind(lambda y: divide(y, 2))
)

if result.is_some:
    print(f"Result is Right: {result}")
else:
    print(f"Result is {result}")

result = (
    Some(10)
    .bind(lambda y: divide(y, 0)) # This in Nothing
    .bind(lambda y: divide(y, 2))  
)

# Expression: m >>= (\x -> f x >>= g)
result_left = (
    Some(10)
    .bind(lambda y: divide(y, 2).bind(lambda z: divide(z, 0)))
)

# Expression: (m >>= f) >>= g
result_right = (
    Some(10)
    .bind(lambda y: divide(y, 2))
    .bind(lambda z: divide(z, 0))
)

print(f"Result left: {result_left} Result right: {result_right}")