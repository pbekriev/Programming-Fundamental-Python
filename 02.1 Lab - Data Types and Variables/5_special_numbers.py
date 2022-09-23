number = input()

for num in range (1, int(number) + 1):
    digit = str(num)

    def sum_digits(digit):
        return sum(int(x) for x in digit if x.isdigit())

    if (sum_digits(digit) == 5) or (sum_digits(digit) == 7) or (sum_digits(digit) == 11):
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")
