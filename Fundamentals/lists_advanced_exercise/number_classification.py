numbers = [int(num) for num in input().split(", ")]

numbers_info = {
    "Positive": [],
    "Negative": [],
    "Even": [],
    "Odd": [],
}

for num in numbers:
    
    if num >= 0:
        numbers_info["Positive"].append(num)
    else:
        numbers_info["Negative"].append(num)
    
    if num % 2 == 0:
        numbers_info["Even"].append(num)
    else:
        numbers_info["Odd"].append(num)

for item, values in numbers_info.items():
    print(f"{item}: {', '.join(str(num) for num in values)}")
