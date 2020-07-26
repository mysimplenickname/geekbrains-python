user_number = input("Enter a number of elements: ")
if user_number.isdigit():
    user_number = int(user_number)
else:
    print("You should enter a number.")
    exit()

user_list = []
while user_number:
    user_list.append(input("Enter an element of the list: "))
    user_number -= 1

print(f"Original list: {user_list}")

for i in range(1, len(user_list), 2):
    user_list[i], user_list[i - 1] = user_list[i - 1], user_list[i]

print(f"Result list:   {user_list}")
