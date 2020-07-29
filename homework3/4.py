# The first way:
# def my_func(x, y):
#     """
#         This function is used to calculate a value of the number raised to the power.
#         :param x:
#         :param y:
#         :return: A value of the number raised to the power.
#     """
#     result = 1
#     while y:
#         result *= x
#         y -= 1
#     return 1 / result


# The second way:
def my_func(x, y):
    """
        This function is used to calculate a value of the number raised to the power.
        :param x:
        :param y:
        :return: A value of the number raised to the power.
    """
    result = 1
    while y:
        result /= x
        y -= 1
    return result


def user_input_check(user_number):
    """
        This function is used to check if user number is an integer number.
        :param user_number
        :return: An integer number or None
    """
    try:
        return int(user_number)
    except ValueError:
        return


user_x = None
correct_flag = 1
while user_x is None or correct_flag:
    user_x = user_input_check(input("Enter the first number that is bigger than zero: "))
    if (user_x is not None) and (user_x > 0):
        correct_flag = 0
    else:
        print("You should enter a number that is bigger than zero. Try again.\n")

print()

user_y = None
correct_flag = 1
while user_y is None or correct_flag:
    user_y = user_input_check(input("Enter the second number that is less than zero: "))
    if (user_y is not None) and (user_y < 0):
        correct_flag = 0
    else:
        print("You should enter a number that is less than zero. Try again.\n")

print(f"\n{user_x} to the power of {user_y} is {my_func(user_x, abs(user_y))}")
