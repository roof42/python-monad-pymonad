from functools import partial


def add(x, y):
    return x + y


class Add:
    def __init__(self, x):
        self.x = x

    def __call__(self, y):
        return self.x + y


def main():
    add_five = partial(add, 5)
    result = add_five(10)
    print(f"Result: {result}")

    add_ten = Add(10)
    result = add_ten(10)
    print(f"Result: {result}")

    print(Add(10)(20))


if __name__ == "__main__":
    main()
