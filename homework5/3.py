SALARY = 20000

with open(r"test_file_3_1", "r") as test_file:
    counter = 0
    total = 0
    line = test_file.readline()

    print("List of employees that have a salary less than 20000: ") if line != '' else print("The file is empty!")

    while line != '':
        counter += 1

        line = line.split(' ')
        total += float(line[1])
        if float(line[1]) < SALARY:
            print(line[0])

        line = test_file.readline()

    print(f"\nAverage salary is {total / counter}.")

print("-" * 64)

eng_numbers_list = ["One", "Two", "Three", "Four"]
rus_numbers_list = ["Один", "Два", "Три", "Четыре"]

with open(r"test_file_3_2", "r") as test_file_in:
    with open(r"test_file_3_3", "w") as test_file_out:
        counter = 0
        line = test_file_in.readline()
        while line != '':
            line = line.replace(eng_numbers_list[counter], rus_numbers_list[counter])
            counter += 1

            test_file_out.write(line)

            line = test_file_in.readline()
