products = {}
command = input()
while command != "buy":
    current_command = command.split()
    names = current_command[0]
    prices = float(current_command[1])
    quantities = int(current_command[2])
    if names not in products.keys():
        products[names] = [prices, quantities]
    else:
        products[names][0] = prices
        products[names][1] += quantities
    command = input()
for name, info in products.items():
    prices = info[0]
    quantities = info[1]
    print(f"{name} -> {(prices * quantities):.2f}")
