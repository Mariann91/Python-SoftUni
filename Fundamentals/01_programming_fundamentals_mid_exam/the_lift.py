people_count = int(input())
wagon_state = [int(num) for num in input().split()]

left_places = False
for i in range(len(wagon_state)):

  if wagon_state[i] < 4:
    people_to_add = 4 - wagon_state[i]
    if people_to_add > people_count:
      people_to_add = people_count
      left_places = True
          
    wagon_state[i] += people_to_add
    people_count -= people_to_add

if left_places:
  print("The lift has empty spots!")

if people_count > 0:
    print(f"There isn't enough space! {people_count} people in a queue!")

print(*wagon_state, sep=" ")    
