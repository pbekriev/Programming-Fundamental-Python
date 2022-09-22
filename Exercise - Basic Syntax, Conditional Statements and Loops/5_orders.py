number_of_orders = int(input())
total_price = 0

for loop in  range (number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsule_per_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    elif  31 < days or days < 1:
        continue
    elif 2000 < capsule_per_day or capsule_per_day < 1:
        continue
    else:
        price_per_order = price_per_capsule * days * capsule_per_day
        total_price += price_per_order
        print(f"The price for the coffee is: ${price_per_order:.2f}")
print(f"Total: ${total_price:.2f}")