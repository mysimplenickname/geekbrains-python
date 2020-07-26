number_of_products = input("Enter a number of products: ")
if number_of_products.isdigit():
    number_of_products = int(number_of_products)
else:
    print("You should enter a number.")
    exit()

products = []
for i in range(1, number_of_products + 1):
    product_name = input(f"Enter a name of product number {i}: ")

    product_price = input(f"Enter a price of product number {i}: ")
    while not product_price.isdigit():
        print("You should enter a number. Try again.")
        product_price = input(f"Enter a price of product number {i}: ")
    product_price = float(product_price)

    product_amount = input(f"Enter an amount of product number {i}: ")
    while not product_amount.isdigit():
        print("You should enter a number. Try again.")
        product_amount = input(f"Enter an amount of product number {i}: ")
    product_amount = int(product_amount)

    product_units = input(f"Enter units for product number {i}: ")

    print(f"Product number {i} added: \n"
          f"   name: {product_name}\n"
          f"   price: {product_price}\n"
          f"   amount: {product_amount}\n"
          f"   units: {product_units}\n")

    product_tuple = (i, dict(name=product_name, price=product_price, amount=product_amount, units=product_units))
    products.append(product_tuple)

name_list = set()
price_list = set()
amount_list = set()
units_list = set()

for i in products:
    name_list.add(i[1].get("name"))
    price_list.add(i[1].get("price"))
    amount_list.add(i[1].get("amount"))
    units_list.add(i[1].get("units"))

statistics = dict(name=list(name_list), price=list(price_list), amount=list(amount_list), units=list(units_list))

for i in statistics:
    print(f"{i}: {statistics.get(i)}")
