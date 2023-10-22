n = int(input())

# creating first triangle
for count in range(1, n + 1):
    print(" " * (n - count), end="")  # placing spaces before stars with end to place stars on the same line
    print(*["*"] * count)  # placing stars by unpacking list of stars to use default space places

# creating second triangle by backwards for cycle
for count in range(n - 1, -1, -1):
    print(" " * (n - count), end="")
    print(*["*"] * count)
