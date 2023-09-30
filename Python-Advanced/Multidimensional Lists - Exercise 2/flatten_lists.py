line = input().split("|")

sub_list = []

for element in line[::-1]:
    sub_list.extend(element.split())

print(*sub_list, sep=" ")
