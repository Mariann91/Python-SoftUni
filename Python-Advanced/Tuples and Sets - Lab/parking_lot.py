n = int(input())

parking_lot = set()

for _ in range(n):
  command, number = input().split(", ")

  if command == "IN":
    parking_lot.add(number)

  if command == "OUT" and parking_lot:
    parking_lot.remove(number)

if parking_lot:
  print(*parking_lot, sep="\n")
else:
  print("Parking Lot is Empty")
