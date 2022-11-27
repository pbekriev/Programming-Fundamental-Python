import re


data = input()
pattern = r"(\#|\|)([a-z A-Z]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"
result = re.finditer(pattern, data)

print_result = ""
calories = 0

for elements in result:
    print_result += f"Item: {elements[2]}, Best before: {elements[3]}, Nutrition: {elements[4]}\n"
    calories += int(elements[4])

number_of_days = int(calories / 2000)

print(f"You have food to last you for: {number_of_days} days!")
print(print_result)