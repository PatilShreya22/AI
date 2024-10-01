#For two quadrants
def vacuum_cleaner_simulation():
    
    current_room = input("Enter current room either A or B: ").upper()
    room_A = int(input("Is Room A dirty? (yes:1/no:0): "))
    room_B = int(input("Is Room B dirty? (yes:1/no:0): "))

    cost = 0

    def display_rooms():
        print(f"Room A: {'Clean' if room_A == 0 else 'Dirty'}")
        print(f"Room B: {'Clean' if room_B == 0 else 'Dirty'}")
    
    print("\nInitial status of rooms:")
    display_rooms()
    print()
    
    
    while room_A == 1 or room_B == 1:
        if current_room == 'A' and room_A == 1:
            print("Cleaning Room A...")
            room_A = 0  
            cost += 1  
        elif current_room == 'B' and room_B == 1:
            print("Cleaning Room B...")
            room_B = 0  
            cost += 1  
        else:
            current_room = 'B' if current_room == 'A' else 'A'
            print(f"Moving to Room {current_room}...")
        print("Current status:")
        display_rooms()
    
    print(f"\nBoth rooms are now clean! Total cost: {cost}")


vacuum_cleaner_simulation()



#For four quadrants
def vacuum_cleaner_simulation():
    current_room = input("Enter current room (A, B, C, or D): ").upper()
    room_A = int(input("Is Room A dirty? (yes:1/no:0): "))
    room_B = int(input("Is Room B dirty? (yes:1/no:0): "))
    room_C = int(input("Is Room C dirty? (yes:1/no:0): "))
    room_D = int(input("Is Room D dirty? (yes:1/no:0): "))

    cost = 0
    count=2
    def display_rooms():
        print(f"Room A: {'Clean' if room_A == 0 else 'Dirty'}")
        print(f"Room B: {'Clean' if room_B == 0 else 'Dirty'}")
        print(f"Room C: {'Clean' if room_C == 0 else 'Dirty'}")
        print(f"Room D: {'Clean' if room_D == 0 else 'Dirty'}")
    
    print("\nInitial status of rooms:")
    display_rooms()
    print()
    
    
    while room_A == 1 or room_B == 1 or room_C == 1 or room_D == 1:
        if count==0:
          print("Vacuum is recharging")
          count=2
        else:
          if current_room == 'A' and room_A == 1:
              print("Cleaning Room A...")
              room_A = 0  
              cost += 1 
              count-=1 
          elif current_room == 'B' and room_B == 1:
              print("Cleaning Room B...")
              room_B = 0  
              cost += 1 
              count-=1  
          elif current_room == 'C' and room_C == 1:
              print("Cleaning Room C...")
              room_C = 0  
              cost += 1  
              count-=1 
          elif current_room == 'D' and room_D == 1:
              print("Cleaning Room D...")
              room_D = 0  
              cost += 1  
              count-=1 
          else:
              if current_room == 'A':
                  current_room = 'B'
              elif current_room == 'B':
                  current_room = 'C'
              elif current_room == 'C':
                  current_room = 'D'
              else:
                  current_room = 'A'
              print(f"Moving to Room {current_room}...")
        
    print("\nCurrent status:")
    display_rooms()
    print(f"\nAll rooms are now clean! Total cost: {cost}")

vacuum_cleaner_simulation()
