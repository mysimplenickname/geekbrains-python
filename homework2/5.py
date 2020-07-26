rating = [8, 8, 5, 3, 3, 3, 2, 1, 1]

user_rating = input("Enter your rating: ")
if user_rating.isdigit():
    user_rating = int(user_rating)
    rating.append(user_rating)
else:
    print("You should enter a number.")
    exit()

i = len(rating) - 1
while (rating[i] > rating[i - 1]) and (i > 0):
    rating[i], rating[i - 1] = rating[i - 1], rating[i]
    i -= 1

print(f"New rating: {rating}")
