def check_the_room(number_of_room):
    total_free_chairs = 0
    total_needed_chairs = 0
    for room in range(1, number_of_room + 1):
        free_chairs, visitors = input().split()
        difference = len(free_chairs) - int(visitors)
        if difference >= 0:
            total_free_chairs += difference
        else:
            total_needed_chairs += abs(difference)
            print(f"{abs(difference)} more chairs needed in room {room}")
    return total_free_chairs, total_needed_chairs


room_number = int(input())
free_chairs, needed_chairs = check_the_room(room_number)
if free_chairs >= needed_chairs:
    print(f"Game On, {free_chairs} free chairs left")
