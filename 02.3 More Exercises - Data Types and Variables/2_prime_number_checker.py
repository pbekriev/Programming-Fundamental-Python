number_for_check = int(input())
check = True
for loop in range (2, number_for_check):
    if number_for_check % loop == 0:
        check = False
        break
print(check)