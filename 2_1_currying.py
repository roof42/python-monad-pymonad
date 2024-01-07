#-------------------------------------------------------------
#Currying using higher order functions
#-------------------------------------------------------------
def plus(a):
    def add(b):
        return a + b
    return add
# Usage
result = plus(2)(3) # <-- This is currying
plusTwo = plus(2) # <-- This is partial apply
print(plusTwo(3))

#Exercise   
def get_multiplier(factor):
    return None
    # def multiply(x):
    #     return Do something here
    # return And here

# result_double = double(5)
# result_triple = triple(5)

# print(result_double) 
# print(result_triple)
