import random

initial_list = [random.randint(0, 9) for i in range(10)]

print(f"Initial list: {initial_list}")

final_list = [i for i in initial_list if initial_list.count(i) == 1]

print(f"Final list:   {final_list}")
