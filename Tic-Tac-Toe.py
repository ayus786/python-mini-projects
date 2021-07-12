
import os
import time
Win = 1
Draw = -1
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '] 
Running=0
Game = Running


def DrawBoard():    
    print(" %c | %c | %c " % (board[1],board[2],board[3]))   
    print("━━━|━━━|━━━")    
    print(" %c | %c | %c " % (board[4],board[5],board[6]))    
    print("━━━|━━━|━━━")    
    print(" %c | %c | %c " % (board[7],board[8],board[9]))    
     

def CheckWin():    
    global Game    
    #Horizontal winning condition    
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):    
        Game = Win    
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):    
        Game = Win    
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):    
        Game = Win    
    #Vertical Winning Condition    
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):    
        Game = Win    
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):    
        Game = Win    
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):    
        Game=Win    
    #Diagonal Winning Condition    
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):    
        Game = Win    
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):    
        Game=Win    
    #Match Tie or Draw Condition    
    elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):
        Game=Draw    
    else:            
        Game=Running 
print("Player 1 [X] --- Player 2 [O]\n")  
print("Please Wait...")
time.sleep(1)
os.system("cls")
DrawBoard()
i=1
while Game==Running:
    y=int(input("Enter any number between 1-9 : "))
    if(y<1 or y>9):
        print("Enter valid position")
        continue
    if(board[y]==' '):
        if(i%2):
            print("Player 1's chance")
            board[y]='X'
        else:
            print("Player 2's chance")
            board[y]='O'
        os.system("cls")
        DrawBoard()
        CheckWin()
        if(Game==Draw):
            print("Oops its Draw")
        elif(Game==Win):
            if(i%2):
                print("Hurrah!, Player 1 Won the game")
            else:
                print("Hurrah!, Player 2 Won the game")
            break
        else:
            i+=1
    else:
        print("try something else, its already filled")