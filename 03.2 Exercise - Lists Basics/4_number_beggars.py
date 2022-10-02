line_of_money = input().split(", ")
count_of_beggars = int(input())
line_of_money_as_digit = []
list_of_money_after = []

for money in line_of_money:
    line_of_money_as_digit.append(int(money))

index = 0

while index < count_of_beggars:
    sum_for_current_beggar = 0

    for current_index in range(index, len(line_of_money_as_digit), count_of_beggars):
        sum_for_current_beggar += line_of_money_as_digit[current_index]

    list_of_money_after.append(sum_for_current_beggar)
    index += 1

print(list_of_money_after)
