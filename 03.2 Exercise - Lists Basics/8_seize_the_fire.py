fire_level = input().split("#")
water_amount = int(input())
total_effort = 0
cells_put_out = []
for fire_cell in fire_level:
    fire_level_with_cell = fire_cell.split(" = ")
    type_of_fire = fire_level_with_cell[0]
    value_of_cell = int(fire_level_with_cell[1])
    if type_of_fire == "High" and 81 <= value_of_cell <= 125 or \
            type_of_fire == "Medium" and 51 <= value_of_cell <= 80 or \
            type_of_fire == "Low" and 1 <= value_of_cell <= 50:
        if water_amount >= value_of_cell:
            water_amount -= value_of_cell
            cells_put_out.append(value_of_cell)
            total_effort += value_of_cell * 0.25

cells_final = [" - "+(str(cell)) for cell in cells_put_out]
print(f"Cells:")
if cells_final:
    print("\n".join(cells_final))
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {sum(cells_put_out)}")
