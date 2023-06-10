people_count = int(input())
wagons_state = [int(num) for num in input().split()]

empty_slots = False
for i in range(len(wagons_state)):

    if wagons_state[i] < 4:
        free_places = 4 - wagons_state[i]
        if free_places > people_count:
            free_places = people_count
            empty_slots = True

        people_count -= free_places
        wagons_state[i] += free_places

if empty_slots:
    print(f"The lift has empty spots!")
elif not empty_slots and people_count != 0:
    print(f"There isn't enough space! {people_count} people in a queue!")

print(*wagons_state, sep=" ")
