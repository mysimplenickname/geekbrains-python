def user_input_check(user_number):
    try:
        return int(user_number)
    except ValueError:
        print("You should enter an integer number.")
        exit()


def create_user_matrix():
    user_matrix_length = user_input_check(input("Enter the length of the matrix: "))
    user_matrix_height = user_input_check(input("Enter the height of the matrix: "))

    matrix = list()

    for i in range(user_matrix_height):
        line = list()
        for j in range(user_matrix_length):
            line.append(user_input_check(input(f"Enter a {j + 1}th number of {i + 1}th line of the matrix: ")))
        print()
        matrix.append(line)

    return matrix


class Matrix:
    matrix: list

    def __init__(self, user_matrix):
        self.matrix = user_matrix

    def __str__(self):
        return str('\n'.join([' '.join([str(i) for i in j]) for j in self.matrix]))

    def __add__(self, other):
        self_matrix_length = len(self.matrix[0])
        self_matrix_height = len(self.matrix)

        other_matrix_length = len(other.matrix[0])
        other_matrix_height = len(other.matrix)

        if self_matrix_length == other_matrix_length and self_matrix_height == other_matrix_height:
            return Matrix([[(self.matrix[i][j] + other.matrix[i][j]) for j in range(self_matrix_length)] for i in range(self_matrix_height)])
        else:
            return f"You can't add matrices with different sizes."


matrix_1 = Matrix(create_user_matrix())
matrix_2 = Matrix(create_user_matrix())

print(matrix_1)
print()

print(matrix_2)
print()

print(matrix_1 + matrix_2)
print()

print('-' * 20)

matrix_3 = Matrix(create_user_matrix())

print(matrix_1)
print()

print(matrix_3)
print()

print(matrix_1 + matrix_3)
