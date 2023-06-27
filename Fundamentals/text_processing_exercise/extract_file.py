file_path = input().split("\\")

last_part = file_path[-1]
file_name, extension = last_part.split(".")

print(f"File name: {file_name}")
print(f"File extension: {extension}")
