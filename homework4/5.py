from functools import reduce


def multiply_func(a, b):
    return a * b


initial_list = [i for i in range(100, 1001) if i % 2 == 0]

print(f"Initial list: {initial_list}")
print(f"Result: {reduce(multiply_func, initial_list)}")
