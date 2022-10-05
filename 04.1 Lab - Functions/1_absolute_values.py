numbers = input().split()
abs_number = []
for num in numbers:
    abs_number.append(abs(float(num)))
print(abs_number)

# numbers = list(map(float, input().split(" ")))
# result = [abs(num) for num in numbers]
# print(result)
