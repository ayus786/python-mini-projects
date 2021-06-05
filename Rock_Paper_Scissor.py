import random
choices = ["ROCK", "PAPER", "SCISSORS"]

while True:
    x=input("Rock, Paper, Scissors?").capitalize()
    AI = random.choice(choices)
    if AI==x:
        print("Tie!")
        p = input("IF YOU WANT TO PLAY MORE PRESS Y ELSE N?")
        if(p=='Y'):
            continue
        else:
            break
    elif(AI=="ROCK"):
        if(x=="PAPER"):
            print("Hurrah! PAPER CAPTURED THE ROCK, YOU WIN")
        else:
            print("YOU LOSE! ,FEEL SORRY FOR YOU")
        p = input("IF YOU WANT TO PLAY MORE PRESS Y ELSE N?")
        if(p=='Y'):
            continue
        else:
            break
    elif(AI=="PAPER"):
        if(x=="SCISSORS"):
            print("Hurrah! SCISSORS CUT THE PAPER, YOU WIN")
        else:
            print("YOU LOSE! ,FEEL SORRY FOR YOU")
        p = input("IF YOU WANT TO PLAY MORE PRESS Y ELSE N?")
        if(p=='Y'):
            continue
        else:
            break
    elif(AI=="SCISSORS"):
        if(x=="ROCK"):
            print("Hurrah! ROCK SMASHES THE SCISSORS, YOU WIN")
        else:
            print("YOU LOSE! ,FEEL SORRY FOR YOU")
        p = input("IF YOU WANT TO PLAY MORE PRESS Y ELSE N?")
        if(p=='Y'):
            continue
        else:
            break
print("NICE TO PLAY WITH YOU,HAVE A GOOD DAY")