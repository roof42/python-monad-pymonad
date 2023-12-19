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
