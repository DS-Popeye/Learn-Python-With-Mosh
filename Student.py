
n = 3
for i in range(n):
    Tried = i+1
    print(f" You Tried {Tried} Times ")
    Guess_Number = int(input(' Guess the Number: '))
    if (Guess_Number == 9):
        print("You Yon!")
        break
    else:
        print("You Failed")
    if(Tried == 3):
        print("Time is up")
