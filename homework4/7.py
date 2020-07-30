def user_input_check(user_number):
    try:
        return int(user_number)
    except ValueError:
        print("You should enter a number.")
        exit()


def gen(user_number):
    result = 1
    for i in range(1, user_number + 1):
        result *= i
        yield result


print(f"Your list: {[i for i in gen(user_input_check(input('Enter a number: ')))]}")
