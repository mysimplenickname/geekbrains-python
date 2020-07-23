number = int(input("Enter a number: "))

max_digit = 0
while number > 0:
    if number % 10 > max_digit:
        max_digit = int(number % 10)
    number /= 10

print(f"The maximal digit is {max_digit}.")
