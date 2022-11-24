import re

command = input()
pattern = r"%([A-Z][a-z]+)%[^\|\$%\.]*<([A-z]+)>[^\|\$%\.]*\|(\d+)\|[^\|\$%\.\d]*(\d+\.?\d*)\$"
income = 0
while command != "end of shift":
    result = re.search(pattern, command)
    if result:
        customer_name, product, quantity, price = result.groups()
        total_price = int(quantity) * float(price)
        print(f"{customer_name}: {product} - {total_price:.2f}")
        income += total_price
    command = input()
print(f"Total income: {income:.2f}")
