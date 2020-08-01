import random

with open(r"test_file_4", "w") as test_file:
    for i in range(10):
        test_file.write(str(random.randint(1, 10)))
        if i < 9:
            test_file.write(" ")
    print(file=test_file)

with open(r"test_file_4", "r") as test_file:
    line = test_file.readline().split(' ')

    total = 0
    for i in line:
        total += int(i)

    print(f"Total sum is {total}.")
