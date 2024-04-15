electrons = int(input())

counter = 1
shells = []

while (electrons):
    
    electrons_to_add = 2 * counter ** 2
    
    if electrons < electrons_to_add:
        
        electrons_to_add = electrons
    
    electrons -= electrons_to_add
    shells.append(electrons_to_add)
    counter += 1

print(shells)
    
