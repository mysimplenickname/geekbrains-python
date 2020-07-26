user_month = input("Enter a number of month: ")
if user_month.isdigit():
    user_month = int(user_month)
else:
    print("You should enter a number.")
    exit()

if not ((user_month > 0) and (user_month < 13)):
    print("You should enter a number from 1 to 12.")
    exit()

months_dict = {
    "winter": [12, 1, 2],
    "spring": [3, 4, 5],
    "summer": [6, 7, 8],
    "autumn": [9, 10, 11]
}

for i in months_dict:
    for j in months_dict.get(i):
        if user_month == j:
            print(f"The season of your month is {i}.")
            break
