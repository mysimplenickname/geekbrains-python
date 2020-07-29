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


# Global variable for summing numbers
global_sum = 0


def sum_func(string):
    """
        This function is used to sum numbers from the sequence.
        :param string:
        :return: An exit character
    """
    global global_sum
    string = string.split(' ')
    for i in string:
        if user_input_check(i) is not None:
            global_sum += int(i)
        elif i == 'q':
            return 'q'


print("Enter a sequence of numbers than press 'Enter' to sum them or press 'q' to exit.")

user_string = None
control_symbol = None
while control_symbol is None:
    user_string = input("> ")
    control_symbol = sum_func(user_string)
    print(f"The sum is {global_sum}")
