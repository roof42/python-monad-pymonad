from pymonad.either import Left, Right
from pymonad.tools import curry

@curry(2)
def divide(a, b):
    return (
        Right(a/b) 
        if b != 0 
        else Left("Error: Division by zero")
    )

result = Right(10).then(divide(2)).then(divide(5))

print(result)