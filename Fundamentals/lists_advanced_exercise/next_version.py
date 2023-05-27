current_version = [int(num) for num in input().split(".")]

for i in range(len(current_version) - 1, -1, -1):
    if current_version[i] < 9:
        current_version[i] += 1

    else:
        current_version[i] = 0
        current_version[i - 1] += 1
        if current_version[i - 1] == 10:
            current_version[i - 1] = 0
            current_version[i - 2] += 1
    break

print(*current_version, sep=".")
