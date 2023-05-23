string = input().split()
shuffle_count = int(input())
start = string.pop(0)
end = string.pop(-1)

for _ in range(shuffle_count):
    shuffled_string = []

    for (a, b) in zip(string[:len(string) // 2], string[len(string) // 2:]):
        shuffled_string.append(b)
        shuffled_string.append(a)
    string = shuffled_string

print([start] + string + [end])
