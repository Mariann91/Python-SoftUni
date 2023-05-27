wagons_count = int(input())

wagons = [0] * wagons_count

command = input()

while command != "End":
    command = command.split()
    action = command[0]

    if action == "add":
        people = int(command[1])
        wagons[-1] += people
    elif action == "insert":
        index = int(command[1])
        people = int(command[2])
        wagons[index] += people
    elif action == "leave":
        index = int(command[1])
        people = int(command[2])
        wagons[index] -= people

    command = input()

print(wagons)

