numbers = input().split(", ")
for num in numbers:
    print(num == num[::-1])
