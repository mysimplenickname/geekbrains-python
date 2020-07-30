import random

initial_list = [random.randint(0, 128) for i in range(10)]

print(f"Initial list: {initial_list}")

print(f"Final list:   {[initial_list[i] for i in range(1, len(initial_list)) if initial_list[i] > initial_list[i - 1]]}")
