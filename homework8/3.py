class MyOnlyIntegerException(Exception):
    @staticmethod
    def check_user_input(user_number, tmp_list: list):
        try:
            tmp_list.append(int(user_number))
            return tmp_list
        except ValueError:
            if user_number != "stop":
                print(f"You should enter a number.")


int_list = []
user_input = None
while user_input != "stop":
    user_input = input("Enter a number or 'stop' to stop: ")
    MyOnlyIntegerException.check_user_input(user_input, int_list)

print(int_list)
