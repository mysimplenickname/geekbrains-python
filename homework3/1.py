def user_input_check(user_number):
    """
        This function is used to check if user number is an integer number.
        :param user_number
        :return: An integer number or None
    """
    try:
        return int(user_number)
    except ValueError:
        print("You should enter a number. Try again.")
        return


def div_func(a, b):
    """
        This function is used to divide number a by number b.
        :param a:
        :param b:
        :return: a / b or Undefined
    """
    try:
        return a / b
    except ZeroDivisionError:
        return "Undefined"


user_a = None
while user_a is None:
    user_a = user_input_check(input("Enter the first number: "))

user_b = None
while user_b is None:
    user_b = user_input_check(input("Enter the second number: "))

print(f"{user_a} / {user_b} = {div_func(user_a, user_b)}")
