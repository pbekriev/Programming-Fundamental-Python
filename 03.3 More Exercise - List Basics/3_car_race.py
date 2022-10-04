time_line = input().split()
left_car_time = 0
right_car_time = 0

for time_index in range(len(time_line) // 2):
    if time_line[time_index] != "0":
        left_car_time += int(time_line[time_index])
    else:
        left_car_time = left_car_time * 0.8
    if time_line[-1-time_index] != "0":
        right_car_time += int(time_line[-1-time_index])
    else:
        right_car_time = right_car_time * 0.8

if left_car_time < right_car_time:
    print(f"The winner is left with total time: {left_car_time:.1f}")
else:
    print(f"The winner is right with total time: {right_car_time:.1f}")