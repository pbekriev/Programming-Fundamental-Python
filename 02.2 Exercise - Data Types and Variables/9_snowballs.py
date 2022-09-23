number_of_snowballs = int(input())
snowball_max_value = 0
max_time = 0
max_quality = 0
max_weight = 0
for loop in range(number_of_snowballs):
    weight_of_snowball = int(input())
    time_to_target = int(input())
    quality_of_snowball = int(input())

    snowball_value = int(weight_of_snowball / time_to_target) ** quality_of_snowball
    if snowball_value > snowball_max_value:
        snowball_max_value = snowball_value
        max_time = time_to_target
        max_quality = quality_of_snowball
        max_weight = weight_of_snowball

print(f"{max_weight} : {max_time} = {snowball_max_value} ({max_quality})")
