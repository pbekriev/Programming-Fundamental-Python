def data_type(type, data):
    if type == "int":
        return int(data) * 2
    elif type == "real":
        return f"{(float(data) * 1.5):.2f}"
    else:
        return f"${data}$"


type_input = input()
data_input = input()
print(data_type(type_input, data_input))
