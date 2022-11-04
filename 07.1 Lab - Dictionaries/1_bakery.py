food_quantities = input().split()
bakery = {}
for index in range(0, len(food_quantities), 2):
    key = food_quantities[index]
    value = int(food_quantities[index + 1])
    bakery[key] = value
print(bakery)
