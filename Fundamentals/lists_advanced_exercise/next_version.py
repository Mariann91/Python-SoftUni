first, second, third = [int(num) for num in input().split(".")]

third += 1

if third > 9:
    third = 0
    second += 1
    
    if second > 9:
        second = 0
        first += 1

print(f"{first}.{second}.{third}")
