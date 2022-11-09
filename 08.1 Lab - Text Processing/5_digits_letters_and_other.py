text = input()
letters = []
digits = []
other = []
for symbol in text:
    if symbol.isalpha():
        letters.append(symbol)
    elif symbol.isdigit():
        digits.append(symbol)
    else:
        other.append(symbol)
print("".join(digits))
print("".join(letters))
print("".join(other))
