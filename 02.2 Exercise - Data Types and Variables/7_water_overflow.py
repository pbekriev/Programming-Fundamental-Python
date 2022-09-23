number_of_lines = int(input())
capacity = 255
water_counter = 0

for line in range (number_of_lines):
    liters_water = int(input())

    if capacity - liters_water < 0:
        print(f"Insufficient capacity!")
        continue
    capacity -= liters_water
    water_counter += liters_water
print(water_counter)