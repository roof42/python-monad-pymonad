from functools import partial


def double(a):
    return a * 2


def add_number(a, b):
    return a + b


def square(a):
    return a**2


class UseCase:
    def __init__(self, double_func, add_one_func, square_func):
        self.double_func = double_func
        self.add_one_func = add_one_func
        self.square_func = square_func

    def __call__(self, value):
        res = self.double_func(self.add_one_func(value))
        return self.square_func(res) + 1


if __name__ == "__main__":
    use_case = UseCase(
        double_func=double,
        add_one_func=partial(add_number, b=1),
        square_func=square,
    )
    result = use_case(3)
    print(f"Result: {result}")
