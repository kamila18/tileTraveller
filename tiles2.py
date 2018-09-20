def directions(x, y):
    north = True
    south = True
    east = True
    west = True

    #check borders
    if y == 3:
        north = False
    elif y == 1:
        south = False
    if x == 1:
        west = False
    elif x == 3:
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
    return north, east, south, west
#returns the directions the player is able to move in from (x,y)


def availableDirections(x, y):
    north, east, south, west = directions(x, y)
    print("You can travel:", end=" ")
    if north:
        print("(N)orth", end="")
        if east or west or south:
            print(" or", end=" ")
    if east:
        print("(E)ast", end="")
        if west or south:
            print(" or", end=" ")
    if south:   
        print("(S)outh", end="")
        if west:
            print(" or", end=" ")
    if west:
        print("(W)est", end="")
    print(".")
#prints out the directions the player can move to from (x,y)

def validInput(x, y):
    north, east, south, west = directions(x, y)
    while True:
        direction = input("Direction: ").upper()
        if direction == "N" and north:
            break
        elif direction == "E" and east:
            break
        elif direction == "S" and south:
            break
        elif direction == "W" and west:
            break
        print("Not a valid direction!")
    return direction
#returns the direction the player can travel to from (x,y)

def movePlayer(x, y, direction):
    if direction == "N":
        y += 1
    elif direction == "E":
        x += 1
    elif direction == "S":
        y -= 1
    elif direction == "W":
        x -= 1
    return x, y
#returns the new position of the player


x, y = 1, 1
while not (x == 3 and y == 1):
    availableDirections(x, y)
    direction = validInput(x, y)
    x, y = movePlayer(x, y, direction)
print("Victory!")