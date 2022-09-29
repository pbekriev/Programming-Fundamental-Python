number_of_lines = int(input())

# constant values
COMMAND_EVEN = "even"
COMMAND_ODD = "odd"
COMMAND_POSITIVE = "positive"
COMMAND_NEGATIVE = "negative"

# accepting numbers from user input
numbers = []

for _ in range(number_of_lines):
    current_number = int(input())
    numbers.append(current_number)

command = input()

filtered_number = []

# number_filtering
for number in numbers:
    filtered_passes = (
        (command == COMMAND_EVEN and number % 2 == 0) or
        (command == COMMAND_ODD and number % 2 != 0) or
        (command == COMMAND_POSITIVE and number >= 0) or
        (command == COMMAND_NEGATIVE and number < 0)
    )
    if filtered_passes:
        filtered_number.append(number)

print(filtered_number)
