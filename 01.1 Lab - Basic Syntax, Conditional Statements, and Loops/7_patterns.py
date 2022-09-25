num = int(input())
stars = "*"
for loop in range (1, num + 1):
    print(loop * "*")
for loop2 in range (num - 1, 0, -1):
    print(loop2 * "*")