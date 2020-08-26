# All the global var required

boardValue = [
                " ", " ", " ",
                " ", " ", " ",
                " ", " ", " ",
              ]
player_1 = ""
player_2 = ""

checkNum = set()

def win(player): #("X" or "O") take ip and display which player won and then kill prog
       displayBoard()
       if player == player_1:
              print("Playr_1 WON!!!")

       else:
              print("Player_2 WON!!")
              
       input("Press Enter to exit")
       exit()
       
       
# checking diagnols 
def diag(player): #("X" or "O")
       if player == boardValue[0] == boardValue[4] == boardValue[8]:
              win(player)

       elif player == boardValue[2] == boardValue[4] == boardValue[6]:
              win(player)

# check row
def row(player): #("X" or "O")
       if player == boardValue[0] == boardValue[1] == boardValue[2]:
              win(player)
       elif player == boardValue[3] == boardValue[4] == boardValue[5]:
              win(player)
       elif player == boardValue[6] == boardValue[7] == boardValue[8]:
              win(player)

# check col
def col(player): #("X" or "O")
       if player == boardValue[0] == boardValue[3] == boardValue[6]:
              win(player)
       elif player == boardValue[1] == boardValue[4] == boardValue[7]:
              win(player)
       elif player == boardValue[2] == boardValue[5] == boardValue[8]:
              win(player)

# check win player = "x" or "o"
def checkWin(player):
       diag(player)
       row(player)
       col(player)
       return 

#will display the current board
def displayBoard():             #board

    #1 5th and 9th pos
    print("\t\t1   |2  |3   ")

    #2 out of 9 places 2nd 5th and 8th place is will show
    print("\t\t  "+boardValue[0]+" | "+boardValue[1]+" | "+boardValue[2])

    # 3 line -----------------
    print("\t\t____|___|____")

    # 4  repeting line 1
    print("\t\t4   |5  |6   ")

    # 5 repeat line 2
    print("\t\t  " + boardValue[3] + " | " + boardValue[4] + " | " + boardValue[5])

    # 6 repeat line 3
    print("\t\t____|___|____")

    # 7 repeat line 1
    print("\t\t7   |8  |9   ")

    # 8 repeat line 2
    print("\t\t  "+boardValue[6]+" | "+boardValue[7]+" | "+boardValue[8])

    # 9 repeat line 1
    print("\t\t    |   |    ")


# player_1 will choose his sign and player_2 automatically choose another sign
def chooseSign():
       global player_1, player_2
       while True:
              player_1 = input("Player 1 Choose your sign \"X\" or \"O\" :")
              player_1 = player_1.upper()

              if player_1=="X":
                     player_2 = "O"
                     break

              if player_1=="O":
                     player_2 = "X"
                     break

              print("Enter valid i/p")

       print("Player_1 selected %s" %player_1)
       print("\n\tPlayer_1 is \'%s\'\n\tPlayer_2 is \'%s\' " %(player_1, player_2))

#this fun required 2 arguments ("playerIP- eg X or O", int-to check which player turn)
def playerIP(playerIP,i): 
       while True:
                try:
                       if i%2==0:
                              n = int(input("Player_1 Turn\nEnter num in range 1 to 9: "))
                       else:
                              n = int(input("Player_2 Turn\nEnter num in range 1 to 9: "))
                               
                       if n in range(1,10):
                              if n not in checkNum:
                                     checkNum.add(n)
                                     boardValue[n-1] = playerIP
                                     break
                              else:
                                     print("place already taken!!!!!!\nreentered value")
                       else:
                              continue
                except:
                       print("Enter intiger")
                       continue

# this fun will check player turn
# dont call in main fun
def checkPlayerTurn(i):
       if i%2==0:
              playerIP(player_1,i)  
              if i>=5:
                     print("before check win")
                     if checkWin(player_1):      #1
                            return "Player_1 WIN!!!!"
       else:
              playerIP(player_2,i)
              if i>=5:
                     if checkWin(player_2):
                            return "Player_2 WIN!!!!"
       

def startGame():
    input("Press Enter to start Game.....")
    # loop will run total 9 time as boards has 9 blocks
    for i in range(9):
           win = checkPlayerTurn(i)     
           print("win=",win)
           displayBoard()
           
              
    else:
           print("its a TIE !!!!")
