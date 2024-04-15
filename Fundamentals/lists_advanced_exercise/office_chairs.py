total_free_chairs = 0
enough_free_chairs = True

for room_number in range(1, int(input()) + 1):
    
    room, visitors = input().split()
    
    room_chairs = len(list(room))
    int_vistors = int(visitors)
    
    
    if room_chairs >= int_vistors:
        total_free_chairs += room_chairs - int_vistors 
    else:
        enough_free_chairs = False
        print(f"{int_vistors - room_chairs} more chairs needed in room {room_number}")
        
if enough_free_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")
