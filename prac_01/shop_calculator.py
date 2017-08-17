total_price = 0
number_of_items = int(input("Number of items: "))

while number_of_items < 0:
    print("invalid number of items! ")
    number_of_items = int(input("Number of items: "))

for i in range(0, number_of_items):
    price_of_item = float(input("Price of item: "))
    total_price += price_of_item

if total_price > 100:
    discount_price = 0.9 * total_price
    print("Total price for {} items is ${:.2f}".format(number_of_items, discount_price))
else:
    print("Total price for {} items is ${:.2f}".format(number_of_items, total_price))
