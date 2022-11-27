import re

string = input()
pattern = r"(\:{2}|\*{2})([A-Z][a-z]{2,})\1"
digits = re.findall(r"\d", string)
emojis = re.finditer(pattern, string)
valid_emojis = {}
add_item =[]
for item in emojis:
    valid_emojis[item.group(2)] = 0
    add_item.append(item.group(1))

for emoji in valid_emojis:
    for letter in emoji:
        valid_emojis[emoji] += ord(letter)

cool_threshold_sum = 1

for digit in digits:
    cool_threshold_sum *= int(digit)

print(f"Cool threshold: {cool_threshold_sum}")
if len(valid_emojis) > 0:
    print(f"{len(valid_emojis)} emojis found in the text. The cool ones are:")
    index = 0
    for key, value in valid_emojis.items():
        if value > cool_threshold_sum:
            print(f"{add_item[index]}{key}{add_item[index]}")
        index += 1