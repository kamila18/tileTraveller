
x = 1
y = 1

while x != 3 or y != 1:
    north = True 
    south = True 
    west = True
    east = True
    #check borders
    if y == 3:
        north = False
    if y == 1:
        south = False 
    if x == 1:
        west = False 
    if x == 3:
        east = False
    #check walls
    if y == 1:
        east = False
        west = False
    elif x == 2 and y == 2:
        north = False
        east = False
    elif x == 3 and y == 2:
        west = False
    elif x == 2 and y == 3:
        south = False
    #moving player
    print("You can travel: ", end ="")
    if north: 
        print("(N)orth", end ="")
        if east or south or west:
            print(" or ", end ="")
    if east:
        print("(E)ast", end ="")
        if south or west: 
            print(" or ", end="")
    if south: 
        print("(S)outh", end="")
        if west:
            print(" or ", end="")
    if west:
        print("(W)est", end="")
    print(".")

    direction = ""
    while True:
        direction = input("Direction: ").upper()
        if direction == "N" and north:
            y += 1
            break
        elif direction == "E" and east:
            x += 1
            break 
        elif direction == "S" and south:
            y -= 1
            break 
        elif direction == "W" and west:
            x -= 1
            break 
        print("Not a valid direction!")
print("Victory!")

    

