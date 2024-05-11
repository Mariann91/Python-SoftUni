n = int(input())

line_stars_count = 0

if n % 2 == 0:
    line_stars_count = 2
else:
    line_stars_count = 1


for i in range(int((n + 1) / 2)):
    dashes_count = int((n - line_stars_count) / 2)
    
    print(dashes_count * "-", end="")
    print(line_stars_count * "*", end="")
    print(dashes_count * "-", end="")
    print()
    line_stars_count += 2

line_stars_count -= 4

for i in range(int(n / 2)):
    print("|", end="")
    print(line_stars_count * "*", end="")
    print("|", end="")
    print()
