import re

with open(r"test_file_5", "r") as test_file:
    subjects_dict = dict()
    line = test_file.readline()
    while line != '':
        line = re.split(r"([A-Za-z]+): ([0-9]*)([()a-z-]+) ([0-9]*)([()a-z-]+) ([0-9]*)([()a-z-]+)", line)

        subjects_dict[line[1]] = 0
        for i in range(2, 8, 2):
            if line[i] != '':
                subjects_dict[line[1]] += int(line[i])

        line = test_file.readline()

    print(f"Subjects dictionary: {subjects_dict}")
