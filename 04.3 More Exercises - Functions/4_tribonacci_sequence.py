def tribonacci(n):
    list_of_number = []
    for n in range(1, n + 1):
        if n == 0 or n == 1 or n == 2:
            list_of_number.append(1)
        elif n == 3:
            list_of_number.append(2)
        else:
            list_of_number.append(sum(list_of_number[-1:-4:-1]))
    return list_of_number


number = int(input())
list_of_str = map(str, tribonacci(number))
print(" ".join(list_of_str))
