interval = int(input())

positives, negatives = [], []
for _ in range(interval):
    current_number = int(input())

    if current_number >= 0:
        positives.append(current_number)
    else:
        negatives.append(current_number)

print(f"{positives}\n{negatives}\nCount of positives: {len(positives)}\nSum of negatives: {sum(negatives)}")
