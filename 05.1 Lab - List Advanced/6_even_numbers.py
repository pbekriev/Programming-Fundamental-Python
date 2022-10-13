numbers = list(map(int, input().split(', ')))
# index = [x for x in range(len(numbers)) if numbers[x] % 2 == 0]
index = [x for x, y in enumerate(numbers) if y % 2 == 0]

print(index)
