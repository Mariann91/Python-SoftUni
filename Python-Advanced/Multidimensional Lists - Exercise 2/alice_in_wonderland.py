size = int(input())
matrix = [[int(el) if el.isdigit() else el for el in input().split()] for _ in range(size)]

commands = {
  "up": lambda x: x - 1,
  "down": lambda x: x + 1,
  "right": lambda x: x + 1,
  "left": lambda x: x - 1,
}
valid_range = range(size)
bags_of_tea = 0
loops_break = False

for row in range(size):
  for col in range(size):

    if matrix[row][col] == "A":
      alice_row = row
      alice_col = col
      matrix[row][col] = "*"

      while bags_of_tea < 10:
        command = input()

        if command == "up" or command == "down":
          alice_row = commands[command](alice_row)

          if alice_row in valid_range:
            alice_current_location = matrix[alice_row][alice_col]
            matrix[alice_row][alice_col] = "*"

            if alice_current_location == "R":
              print("Alice didn't make it to the tea party.")
              loops_break = True
              break
            elif str(alice_current_location).isdigit():
              bags_of_tea += alice_current_location
          else:
            print("Alice didn't make it to the tea party.")
            loops_break = True
            break

        if command == "right" or command == "left":
          alice_col = commands[command](alice_col)

          if alice_col in valid_range:
            alice_current_location = matrix[alice_row][alice_col]
            matrix[alice_row][alice_col] = "*"

            if alice_current_location == "R":
              print("Alice didn't make it to the tea party.")
              loops_break = True
              break
            elif str(alice_current_location).isdigit():
              bags_of_tea += alice_current_location
          else:
            print("Alice didn't make it to the tea party.")
            loops_break = True
            break
      else:
        loops_break = True
        print("She did it! She went to the party.")

    if loops_break:
      break
  if loops_break:
    break

[print(*row) for row in matrix]
