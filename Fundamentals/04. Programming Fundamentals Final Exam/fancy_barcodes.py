import re

pattern = r"^@#+[A-Z][A-Za-z\d]+[A-Z]@#+$"
interval = int(input())

for _ in range(interval):
    barcode = input()
    result = re.match(pattern, barcode)
    group = ""

    if result:
        for char in barcode:
            if char.isdigit():
                group += char
        if group:
            print(f"Product group: {group}")
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")
      
