def int_func(string):
    """
        This function is used to convert a lowercase string to a title string with the first capital letter.
        :param string:
        :return: A title string with the first capital letter
    """
    new_string = chr(ord(string[0]) - 32)
    new_string += string[1:]
    return new_string


user_string = input("Enter your string: ").split(' ')
output_string = ''
for i in user_string:
    output_string += int_func(i) + ' '

print(f"Output string: {output_string[:len(output_string) - 1]}")
