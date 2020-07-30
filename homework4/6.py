from itertools import count, cycle
import random


def user_input_check(user_number):
    try:
        return int(user_number)
    except ValueError:
        print("You should enter a number.")
        exit()


def first_func(user_number):
    final_list = list()
    for i in count(user_number):
        if i < user_number + 11:
            final_list.append(i)
        else:
            break
    return final_list


def second_func(user_list):
    counter = 0
    final_list = list()
    for i in cycle(user_list):
        if counter < 15:
            final_list.append(i)
        else:
            break
        counter += 1
    return final_list


print(f"Your list: {first_func(user_input_check(input('Enter a number: ')))}\n")

initial_list = [random.randint(0, 9) for i in range(5)]
print(f"Initial list: {initial_list}")
print(f"Final list:   {second_func(initial_list)}")
