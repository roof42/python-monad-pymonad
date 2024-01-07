#-------------------------------------------------------------
#Currying using toolz
#-------------------------------------------------------------
from toolz import curry

#Definition
@curry
def plus(a, b):
    return a + b

# Usage
result = plus(2)(3) # <-- This is currying
plusTwo = plus(2) # <-- This is partial apply
print(plusTwo(3))

