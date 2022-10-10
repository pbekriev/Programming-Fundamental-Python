def even_num(number):
    if number % 2 == 0:
        return True
    return False


numbers = input().split()
int_numbers = list(int(x) for x in numbers)
even_list = filter(even_num, int_numbers)
print(list(even_list))
