class ComplexNumber:
    re: int
    im: int

    def check_user_input(self, user_number: tuple):
        try:
            return int(user_number[0]), int(user_number[1])
        except ValueError:
            print("You should enter a pair of numbers.")
            exit()

    def __init__(self, user_number: tuple):
        self.re = self.check_user_input(user_number)[0]
        self.im = self.check_user_input(user_number)[1]

    def __add__(self, other):
        return ComplexNumber((self.re + other.re, self.im + other.im))

    def __mul__(self, other):
        re_sum = self.re * other.re + (self.im * other.im * -1 if self.im != 0 and other.im != 0 else self.im * other.im)
        im_sum = self.re * other.im + self.im * other.re

        return ComplexNumber((re_sum, im_sum))

    def __str__(self):
        output = ''
        if self.re != 0:
            output += str(self.re)

        if self.im != 0:
            if self.re != 0 and self.im > 0:
                output += '+'

            if self.im == 1:
                output += 'i'
            elif self.im == -1:
                output += '-i'
            else:
                output += str(self.im) + 'i'

        if output == '':
            output += '0'

        return output


number_1 = ComplexNumber(tuple(input("Enter a pair of numbers: ").split(' ')))
print(f"z1 = {number_1}")

number_2 = ComplexNumber(tuple(input("Enter a pair of numbers: ").split(' ')))
print(f"z2 = {number_2}")

print(f"z1 + z2 = {number_1} + {number_2} = {number_1 + number_2}")

number_3 = ComplexNumber(tuple(input("Enter a pair of numbers: ").split(' ')))
print(f"z3 = {number_3}")

number_4 = ComplexNumber(tuple(input("Enter a pair of numbers: ").split(' ')))
print(f"z4 = {number_4}")

print(f"z3 * z4 = {number_3} * {number_4} = {number_3 * number_4}")
