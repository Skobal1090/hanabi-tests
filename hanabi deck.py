import random

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
        print(getColor(handNum[i]) + str(getRank(handNum[i])) + " (" +str(handNum[i])+ ")")

dealHands(4)
for i in range(playerHands):
    printHand(i)
