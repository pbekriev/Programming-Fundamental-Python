collection_of_item = input().split("|")
budget = float(input())
bought_item_price = []
profit = 0
for item_and_price in collection_of_item:
    item_price = item_and_price.split("->")
    item = item_price[0]
    price = float(item_price[1])
    if (item == "Clothes" and price <= 50.00) or \
            (item == "Shoes" and price <= 35.00) or \
            (item == "Accessories" and price <= 20.50):
        if budget >= price:
            budget -= price
            profit += price * 0.4
            bought_item_price.append(price * 1.4)
for prices in bought_item_price:
    print(f"{prices:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")
if budget + sum(bought_item_price) >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
