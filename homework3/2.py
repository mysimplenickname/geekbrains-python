# A library for using regular expressions
import re


def user_input_check(user_number):
    """
        This function is used to check if user number is a positive integer number.
        :param user_number:
        :return: A positive integer number or None
    """
    if user_number.isdigit():
        return int(user_number)
    else:
        return


def main_func(name, surname, birth_year, city, email, phone_number):
    """
        This function is used to print a string with all parameters in one line.
        :param name:
        :param surname:
        :param birth_year:
        :param city:
        :param email:
        :param phone_number:
        :return: A string with all parameters in one line
    """
    print(f"Hello {name} {surname}! "
          f"Your birth year is {birth_year}. "
          f"You are from {city}. "
          f"Your email and phone number are {email} and {phone_number}. "
          f"Have a nice day!")


user_name = input("Enter your name: ")

user_surname = input("Enter your surname: ")

user_birth_year = None
correct_flag = 1
while user_birth_year is None and correct_flag:
    user_birth_year = user_input_check(input("Enter your birth year: "))
    if (user_birth_year is not None) and (user_birth_year > 0) and (user_birth_year < 2021):
        correct_flag = 0
    else:
        print("You should enter a correct birth year. Try again.")

user_city = input("Enter your home town: ")

user_email = None
correct_flag = 1
while user_email is None or correct_flag:
    user_email = input("Enter your email: ")
    # On the next string I used regular expression for checking email correctness.
    if re.match("([A-Za-z0-9_-]+)@([A-Za-z0-9]+)\.([A-Za-z]+)", user_email) is not None:
        correct_flag = 0
    else:
        print("You should enter a correct email. Try again.")

user_phone_number = None
correct_flag = 1
while user_phone_number is None or correct_flag:
    str_user_phone_number = input("Enter your phone number (11 digits): ")
    user_phone_number = user_input_check(str_user_phone_number)
    if (user_phone_number is not None) and (len(str_user_phone_number) == 11):
        correct_flag = 0
    else:
        print("You should enter a correct phone number. Try again.")

main_func(name=user_name,
          surname=user_surname,
          birth_year=user_birth_year,
          city=user_city,
          email=user_email,
          phone_number=user_phone_number)
