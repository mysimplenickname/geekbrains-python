def check_user_input(user_number):
    try:
        return int(user_number)
    except ValueError:
        print("You should enter a number.")
        exit()


class MyZeroDivisionException(Exception):
    @staticmethod
    def check_division_by_zero(number_1, number_2):
        try:
            return number_1 / number_2
        except ZeroDivisionError:
            return f"You can't divide by zero."


user_number_1 = check_user_input(input("Enter the first number: "))
user_number_2 = check_user_input(input("Enter the second number: "))

print(MyZeroDivisionException.check_division_by_zero(user_number_1, user_number_2))
