message = input()

digits = [digit for digit in message if digit.isdigit()]

take_list = [int(digits[index]) for index in range(len(digits)) if index % 2 == 0]
skip_list = [digits[index] for index in range(len(digits)) if index % 2 != 0]

chars = [char for char in message if not char.isdigit()]

new_string = ""
for i in range(len(take_list)):
    take_number = take_list[i]
    skip_number = skip_list[i]
    new_string += "".join(chars[:take_number])
    del chars[0:take_number + int(skip_number)]
print(new_string)
