from math import ceil

def print_glass(step, num):
    stars_count = n * 2
    
    if step == 1 or step == num:
        print(stars_count * "*", end="")
    else:
        print("*", end="")
        print((stars_count - 2) * "/", end="")
        print("*", end="")
    
n = int(input())

middle = ceil(n / 2)

for i in range(1, n + 1):
    print_glass(i, n)
 
    if i == middle:
	    print(n * "|", end="")
    else:
        print(n * " ", end="")

    print_glass(i, n)
    print()
