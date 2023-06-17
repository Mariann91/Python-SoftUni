MAX_SIZE = 4

people_count = int(input())
wagons = [int(wagon) for wagon in input().split()]

left_places = False
for i in range(len(wagons)):

    if wagons[i] < MAX_SIZE:
        free_places = MAX_SIZE - wagons[i]
        if free_places > people_count:
            free_places = people_count
            left_places = True

        wagons[i] += free_places
        people_count -= free_places

if left_places:
    print("The lift has empty spots!")
elif not left_places and people_count != 0:
    print(f"There isn't enough space! {people_count} people in a queue!")

print(*wagons, sep=" ")
