word = input()

rev_word = ""

for loop in range (len(word) - 1, -1, -1):
    rev_word += word[loop]
print(rev_word)

# Other way Slicing

#word = input()
#print(word[::-1])