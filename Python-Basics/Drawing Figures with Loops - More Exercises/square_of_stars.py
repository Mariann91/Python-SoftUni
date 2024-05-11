stars_count = int(input())
output = []

for i in range(stars_count):
    output.append("*")

[print(" ".join(output)) for _ in range(stars_count)]
