stars_count = int(input())

print((stars_count + 1) * " ", end="")
print("|")

for i in range(stars_count, 0, -1):
    multiplier = i - 1
	
    print(multiplier * " ", end="")
    print((stars_count - multiplier) * "*", end=" ")
    print("|", end=" ")
    
    print((stars_count - multiplier) * "*", end=" ")
    print(multiplier * " ", end="")
    
    print()	
