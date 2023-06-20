phone_book = {}

while True:
    info = input()

    if "-" not in info:
        break

    contact, number = info.split("-")
    phone_book[contact] = number

names_to_search = int(info)

for _ in range(names_to_search):
    name = input()

    if name in phone_book.keys():
        number = phone_book[name]
        print(f"{name} -> {number}")
    else:
        print(f"Contact {name} does not exist.")
      
