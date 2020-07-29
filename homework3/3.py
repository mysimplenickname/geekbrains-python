def user_input_check(user_number):
    """
        This function is used to check if user number is a positive integer number.
        :param user_number:
        :return: A positive integer number or None
    """
    if user_number.isdigit():
        return int(user_number)
    else:
        print("Enter a correct number. Try again.")
        return


def my_func(a, b, c):
    """
        This function is used to determine the largest sum of three numbers.
        :param a:
        :param b:
        :param c:
        :return: The largest sum
    """
    ab = a + b
    ac = a + c
    bc = b + c

    if ab > ac:
        if ab > bc:
            return ab
        else:
            return bc
    elif ac > bc:
        return ac
    else:
        return bc


user_a = None
while user_a is None:
    user_a = user_input_check(input("Enter the 1th number: "))

user_b = None
while user_b is None:
    user_b = user_input_check(input("Enter the 2th number: "))

user_c = None
while user_c is None:
    user_c = user_input_check(input("Enter the 3th number: "))

print(f"The sum of the biggest numbers is {my_func(user_a, user_b, user_c)}.")
