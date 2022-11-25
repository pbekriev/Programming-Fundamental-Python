def check_true(first, second, third, fourth):
    if first and second and third and fourth:
        return True


import re

text = input()

name_pattern = r"\%([A-Z][a-z]+)\%"
item_pattern = r"\<([\w]+)\>"
quant_pattern = r"\|([0-9]+)\|"
price_pattern = r"([0-9]+\.*[0-9]*)\$"
total = 0
while text != "end of shift":
    name = re.findall(name_pattern, text)
    item = re.findall(item_pattern, text)
    quantity = re.findall(quant_pattern, text)
    price = re.findall(price_pattern, text)
    if check_true(name, item, quantity, price):
        total += float(quantity[0]) * float(price[0])
        print(f"{''.join(name)}: {''.join(item)} - {float(quantity[0]) * float(price[0]):.2f}")
    text = input()
if total != 0:
    print(f"Total income: {total:.2f}")



# import re
#
# command = input()
# pattern = r"%([A-Z][a-z]+)%[^\|\$%\.]*<([A-z]+)>[^\|\$%\.]*\|(\d+)\|[^\|\$\%\.]*([1-9]+[\.\d]*)\$"
# income = 0
# while command != "end of shift":
#     result = re.search(pattern, command)
#     if result:
#         customer_name, product, quantity, price = result.groups()
#         total_price = int(quantity) * float(price)
#         print(f"{customer_name}: {product} - {total_price:.2f}")
#         income += total_price
#     command = input()
# print(f"Total income: {income:.2f}")
