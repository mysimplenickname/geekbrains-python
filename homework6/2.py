def user_input_check(user_number):
    try:
        return int(user_number)
    except ValueError:
        print("You should enter an integer number.")
        exit()


class Road:
    _length: int
    _width: int

    def __init__(self, user_length: int, user_width: int):
        self._length = user_length
        self._width = user_width

    _mass_per_sq_meter = 25
    _height = 0.05

    def calc_method(self):
        print(self._length * self._width * self._mass_per_sq_meter * self._height)


user_length = user_input_check(input("Enter the length: "))
user_width = user_input_check(input("Enter the width: "))

road = Road(user_length, user_width)
road.calc_method()
