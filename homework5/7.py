import json

with open(r"test_file_7", "r") as test_file_in:
    final_list = list()

    companies_dict = dict()
    average_dict = dict()

    total = 0
    number_of_companies = 0

    line = test_file_in.readline()
    while line != '':
        number_of_companies += 1

        line = line.split(' ')
        companies_dict[line[0]] = round(float(line[2]) - float(line[3]), 2)
        if companies_dict[line[0]] > 0:
            total += companies_dict[line[0]]

        line = test_file_in.readline()

    average_dict["average_income"] = round(total / number_of_companies, 2)

    final_list.append(companies_dict)
    final_list.append(average_dict)

    with open(r"test_file_8", "w") as test_file_out:
        json.dump(final_list, test_file_out)
