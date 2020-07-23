revenue = float(input("Enter the firm revenue value: "))
cost = float(input("Enter the firm cost value: "))

if cost > revenue:
    print("The firm incurs losses.")
elif cost < revenue:
    profit = revenue - cost
    print("The firm makes a profit. A profitability equals %.02f%%" % (profit / revenue * 100))

    employees_number = int(input("Enter a number of employees: "))
    if employees_number > 0:
        print("Profit for one employee - %.02f" % (profit / employees_number))
else:
    print("The firm does not make a profit.")
