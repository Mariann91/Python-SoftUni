food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
weight = float(input()) * 1000

for day in range(1, 31):

    food -= 300

    if day % 2 == 0:
        hay -= food * 0.05

    if day % 3 == 0:
        cover -= weight / 3

    if food < 300 or hay < (food * 0.05) or cover < (weight / 3):
        print("Merry must go to the pet store!")
        break
else:
    print(f"Everything is fine! Puppy is happy! Food: {food / 1000:.2f},"
          f" Hay: {hay / 1000:.2f}, Cover: {cover / 1000:.2f}.")
