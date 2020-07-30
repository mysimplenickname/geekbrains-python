from functools import reduce

initial_list = [i for i in range(100, 1001) if i % 2 == 0]

print(f"Initial list: {initial_list}")
print(f"Result: {reduce(lambda x, y: x * y, initial_list)}")
