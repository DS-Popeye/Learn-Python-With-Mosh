#This is a car game.
print("Write help to show Button")
Direction = ''
while Direction.upper() != "QUIT":
    Direction = input(">").lower()
    if Direction == "start":
        print('Start The Game')
    elif(Direction == 'stop'):
        print('Stop The car')
    elif(Direction == 'help'):
        print("start - to start the car \nstop = stop the car \nquite - to exit")
    elif(Direction == 'quit'):
        break
    else:
        print("I don't Understand")


