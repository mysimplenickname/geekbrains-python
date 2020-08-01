with open(r"test_file_1", "w") as test_file:
    print("Enter some strings: ")
    user_string = input("> ")
    while user_string != '':
        print(user_string, file=test_file)
        user_string = input("> ")

print("All your strings have been written.")
