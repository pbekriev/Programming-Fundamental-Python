import re

sentence = input()
pattern = r'\b_([A-Za-z0-9]+)\b'
found_names = re.findall(pattern, sentence)
print(','.join(found_names))