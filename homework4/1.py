import sys


def user_input_check(user_number, user_arg):
    try:
        return float(user_number)
    except ValueError:
        print(f"You should enter a float number for {user_arg}.")
        exit()


user_args = sys.argv
if len(user_args) < 4:
    print("You should enter number of working hours, pay rate per hour and amount of bonus.")
    exit()

user_hours, user_pay_rate, user_bonus = user_input_check(user_args[1], "number of working hours"), \
                                        user_input_check(user_args[2], "pay rate per hour"), \
                                        user_input_check(user_args[3], "amount of bonus")

print(f"Your salary is {(user_hours * user_pay_rate) + user_bonus}$.")
