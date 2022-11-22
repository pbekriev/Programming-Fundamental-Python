import re

sentence = input()
some_word = input()
pattern = fr'\b{some_word}\b'
matches = re.findall(pattern, sentence, flags=re.IGNORECASE)
print(len(matches))