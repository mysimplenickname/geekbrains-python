a = float(input("Enter a: "))
b = float(input("Enter b: "))

day_number = 1
print("Day {}: {:.02f} km".format(day_number, a))
while a < b:
    day_number += 1
    a *= 1.1
    print("Day {}: {:.02f} km".format(day_number, a))

print("The sportsman reached the result \"at least {:.02f} km\" on day {}.".format(b, day_number))
