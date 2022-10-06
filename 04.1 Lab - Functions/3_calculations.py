def calculator(input_operator, first_num, second_num):
    if input_operator == "add":
        return first_num + second_num
    elif input_operator == "subtract":
        return first_num - second_num
    elif input_operator == "multiply":
        return first_num * second_num
    elif input_operator == "divide":
        return int(first_num / second_num)


input_operator = input()
first_num = int(input())
second_num = int(input())
print(calculator(input_operator, first_num, second_num))
