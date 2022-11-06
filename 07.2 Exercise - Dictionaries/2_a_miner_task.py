resource = {}
while True:
    curent_resource = input()
    if curent_resource == "stop":
        break
    curent_quantity = int(input())
    if curent_resource not in resource.keys():
        resource[curent_resource] = 0
    resource[curent_resource] += curent_quantity
for resource, quantity in resource.items():
    print(f"{resource} -> {quantity}")
