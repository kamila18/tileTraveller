#In the start we assume that the user can move in every direction
#The we go on to check if the user is located by any border, if so then the user is not 
# able to move in the direction of the border
#Then we go to check if the user is located by a wall, if so then we eliminate the direction of the wall 
#Next up we go to printing the statements for each move 
#At the end we do the maths, here is when the user moves between the tiles. 
#The user is able to move freely between the borders as long as he doesn't encounter any wall or a border
#If the user wants to go in the direction of a border/wall then the output "Not a valid direction" prints out 
#The game goes on until the user goes on the tile 3,1
#One the user gets to that tile the output is "Victory!"

#n = x + 0, y + 1
#s = x + 0, y - 1
#e = x + 1, y + 0
#w = x - 1, y + 0

x = 1
y = 1

while x != 3 or y != 1:
    n = True
    s = True
    w = True
    e = True
    #check borders
    if y == 3:
        n = False
    elif y == 1:
        s = False
    elif x == 1: 
        w = False
    elif x == 3:
        e = False

    #check walls
    if y == 1:
        w = False
        e = False
    if x == 2 and y == 2:
        e = False
        n = False
    if x == 3 and y == 2:
        w = False
    if x == 2 and y == 3:
        s = False 

    #move
    print("You can travel: ", end ="")
    if n:
        print("(N)orth", end ="")
        if e or s or w:
            print(" or ", end ="")
    if e: 
        print("(E)ast", end ="")
        if s or w:
            print(" or ", end="")
    if s: 
        print("(S)outh", end="")
        if w:
            print(" or ", end="")
    if w:
        print("(W)est", end="")
    
    print(".")
    
    direction =""
    while True:
        direction = input("Direction: ").upper()
        if direction == "N" and n:
            y += 1
            break
        elif direction == "E" and e:
            x += 1
            break
        elif direction == "S" and s:
            y -= 1
            break
        elif direction == "W" and w:
            x -= 1
            break 
        print("Not a valid direction!")
    
print("Victory!")

