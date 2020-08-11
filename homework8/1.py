import datetime


def user_input_check(user_number):
    try:
        return int(user_number)
    except ValueError:
        print("You should enter a date in format 'dd-mm-yyyy'.")
        exit()


class Date:
    str_date: str

    def __init__(self, str_date=''):
        self.str_date = str_date

    @classmethod
    def extract_date(cls, str_date):
        int_date = [user_input_check(i) for i in str_date.split('-')]
        return f"Your date in the format of list of integers: {int_date}."

    @staticmethod
    def check_date(str_date):
        date_format = "%d-%m-%Y"
        try:
            datetime.datetime.strptime(str_date, date_format)
            return f"Your date is correct."
        except ValueError:
            print("You should enter a correct date.")
            exit()


print(Date.extract_date("01-01-2020"))
print(Date.check_date("01-01-2020"))
