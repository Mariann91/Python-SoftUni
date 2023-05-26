def calculate(type, num):
    if type == "int":
        return int(num) * 2
    elif type == "real":
        return f"{float(num) * 1.5:.2f}"
    elif type == "string":
        return f"${num}$"


data_type = input()
number = input()

print(calculate(data_type, number))
