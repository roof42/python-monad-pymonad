class Ok:
    def __init__(self, value):
        self.value = value

    def bind(self, func):
        return func(self.value)

    def __str__(self):
        return f"Right({self.value})"

class Fail:
    def __init__(self, error_message):
        self.error_message = error_message

    def bind(self, func):
        return self

    def __str__(self):
        return f"Left({self.error_message})"

class Maybe:
    @staticmethod
    def ok(value):
        return Ok(value)

    @staticmethod
    def fail(error_message):
        return Fail(error_message)
    
    @staticmethod
    def is_ok(instance):
        return isinstance(instance, Ok)

# Updated divide function
def divide(a, b):
    if b == 0:
        return Maybe.fail("Division by zero error")
    else:
        return Maybe.ok(a / b)

# Example usage of Maybe monad with Right and Left
result = (
    Maybe.ok(10)
    .bind(lambda y: divide(y, 2))
    .bind(lambda y: divide(y, 0))  # This will result in an error
)

if Maybe.is_ok(result):
    print(f"Result is Right: {result}")
else:
    print(f"Result is Left: {result}")
