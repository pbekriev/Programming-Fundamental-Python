import re

dates = input()
pattern = r"(\d{2})([\/.-])([A-Z][a-z]{2})\2(\d{4})"
result = re.findall(pattern, dates)
for mach in result:
    print(f"Day: {mach[0]}, Month: {mach[2]}, Year: {mach[3]}")