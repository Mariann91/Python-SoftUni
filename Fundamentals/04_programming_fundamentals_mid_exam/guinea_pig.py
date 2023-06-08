food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
guinea_pig_weight = float(input()) * 1000

for day in range(1, 31):
    if food < 300 or hay < 300 * 0.05 or guinea_pig_weight < guinea_pig_weight / 3:
        print("Merry must go to the pet store!")
        break

    food -= 300

    if day % 2 == 0:
        hay -= food * 0.05

    if day % 3 == 0:
        cover -= guinea_pig_weight / 3
else:
    print(f"Everything is fine! Puppy is happy! Food: {food / 1000:.2f}, Hay: {hay / 1000:.2f}, Cover: {cover / 1000:.2f}.")