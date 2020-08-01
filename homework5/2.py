with open(r"test_file_2", "r") as test_file:
    counter = 0
    line = test_file.readline()
    while line != '':
        counter += 1

        words_counter = 0
        line = line.split(' ')
        for i in line:
            if i != '.\n' and i != ',\n' and i != '!\n' and i != '?\n' and i != '\n':
                words_counter += 1

        print(f"Number of words in the line {counter} is {words_counter}.")

        line = test_file.readline()

    print(f"Number of strings in the file is {counter}.")
