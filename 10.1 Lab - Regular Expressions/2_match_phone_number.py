import re

numbers= input()
patter = r"\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b"

result = re.findall(patter, numbers)
print(", ".join(result))
