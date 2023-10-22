# 1 Solution wihout functions

n = int(input())

# creating first triangle
for count in range(1, n + 1):
    print(" " * (n - count), end="")  # placing spaces before stars with end to place stars on the same line
    print(*["*"] * count)  # placing stars by unpacking list of stars to use default space places

# creating second triangle by backwards for cycle
for count in range(n - 1, -1, -1):
    print(" " * (n - count), end="")
    print(*["*"] * count)

# 2 Solution with single function

def print_figure(number, triangle_number):
    
    for count in range(1, number + 1):
            print(" " * (number - count), end="")
            print(*["*"] * count)
        
    for count in range(n - 1, -1, -1):
        print(" " * (n - count), end="")
        print(*["*"] * count)


n = int(input())

print_figure(n)


# 3 Solution with 2 seperate functions 

def print_row(number, count):
    print(" " * (number - count), end="")
    print(*["*"] * count)


def rhombus(number):

    for num in range(1, number + 1):
        print_row(number, num)

    for num in range(number - 1, -1, -1):
        print_row(number, num)


n = int(input())

rhombus(number=n)
