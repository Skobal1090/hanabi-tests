import random
import os

#normRank -> actual value
#0 <-1
#1 <-1
#2 <-1
#3 <-2
#4 <-2
#5 <-3
#6 <-3
#7 <-4
#8 <-4
#9 <-5

dealt = []
playerHands=[]
handSize = 5

def getRank(card):
    normRank = card%10
    if(0<=normRank<=2):
        return 1
    elif(normRank<=4):
        return 2
    elif(normRank<=6):
        return 3
    elif(normRank<=8):
        return 4
    else:
        return 5

def getColor(card):
    color = card//10
    if(color==0):
        return "Red "
    elif(color==1):
        return "Yellow "
    elif(color==2):
        return "Blue "
    elif(color==3):
        return "Green "
    else:
        return "White "

def getColorInternal(card):
    color = card//10
    if(color == 0):
        return "91"
    elif(color == 1):
        return "33"
    elif(color==2):
        return "94"
    elif(color==3):
        return "92"
    else:
        return "97"

def dealHand():
    hand = []
    while len(hand)<handSize:
        card = random.randint(0,49)
        if(card not in dealt):
            dealt.append(card)
            hand.append(card)
    return hand

def dealHands(numPlayers):
    for i in range(numPlayers):
        playerHands.append(dealHand())

def printHand(handNum):
    for i in range(len(handNum)):
        os.system(f"Echo \033[{getColorInternal(handNum[i])}m {getColor(handNum[i]) + str(getRank(handNum[i]))} ({str(handNum[i])}) \033[0m")
    print()

def printPlayerInfo():
    print(f"Player {str(currentPlayer+1)}'s Turn: \n")
    playerHandOutput = ""
    for i in range(numPlayers):
        if currentPlayer != i:
            playerHandOutput += '{0:25}'.format(f"Player {i+1}'s Hand:")
    print(playerHandOutput)

for i in range(handSize):
    output = ""
    for j in range(numPlayers):
        if(j != currentPlayer):
            output += '{0:34}'.format(getFormattedCardText(playerHands[j][i]))
    os.system(f"Echo {output}")

numPlayers = input("How many people are playing?")
gameOver = False
playerTurn = 0

dealHands(int(numPlayers))
for i in range(len(playerHands)):
    if playerTurn != i:
        print("Player " + str(i) + "'s hand")
        printHand(playerHands[i])

action = input("What would you like to do?")
