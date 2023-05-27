first = input().split(", ")
second = input().split(", ")

output = []
for word1 in first:
    for word2 in second:
        if word1 in word2:
            output.append(word1)
            break

print(output)
