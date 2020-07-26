user_string = input("Enter your string: ")
user_string = user_string.split(' ')

counter = 1
for i in user_string:
    print(f"{counter:2}. {i[:10]}")
    counter += 1
