numbers = input().split()
list_num = list(map(int, numbers))
print(f"The minimum number is {min(list_num)}\n"
      f"The maximum number is {max(list_num)}\n"
      f"The sum number is: {sum(list_num)}")
