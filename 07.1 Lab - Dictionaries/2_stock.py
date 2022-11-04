products_quantities = input().split()
search = input().split()
products_quantities_dict = {}
for index in range(0, len(products_quantities), 2):
    key = products_quantities[index]
    value = int(products_quantities[index + 1])
    products_quantities_dict[key] = value

for item in search:
    if item in products_quantities_dict:
        print(f"We have {products_quantities_dict[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")
