reservations = {input() for _ in range(int(input()))}

command = input()

while command != "END":
    guest = command
    reservations.remove(guest)
    command = input()

print(len(reservations))
[print(guest) for guest in sorted(reservations)]
