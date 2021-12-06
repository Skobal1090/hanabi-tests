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
playerColorKnowledge=[]
playerRankKnowledge=[]
handSize = 5
debugMode = True

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
        return "Red"
    elif(color==1):
        return "Yellow"
    elif(color==2):
        return "Blue"
    elif(color==3):
        return "Green"
    else:
        return "White"

def getColorInfo(info):
    if(info == -1):
        return "Unknown"
    elif(info == 0):
        return "Red"
    elif(info == 1):
        return "Yellow"
    elif(info == 2):
        return "Blue"
    elif(info == 3):
        return "Green"
    else:
        return "White"

def getRankInfo(info):
    if(info == 0):
        return "Unknown"
    return str(info)

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

def initGame(numPlayers):
    dealHands(numPlayers)
    for i in range(numPlayers):
        playerColorKnowledge.append([-1] * handSize)
        playerRankKnowledge.append([0] * handSize)

def printPlayerKnowledge(currentPlayer, numbered):
    global debugMode
    playerKnownColors = playerColorKnowledge[currentPlayer]
    playerKnownRanks = playerRankKnowledge[currentPlayer]
    for i in range(handSize):
        textOutput = f"{i+1}. " if numbered else ""
        if(playerKnownColors[i] == -1 and playerKnownRanks[i] == 0):
            textOutput += "Unknown"
            if debugMode:
                textOutput += f" ({getFormattedCardText(playerHands[currentPlayer][i])})"
        elif(playerKnownColors[i] == -1):
            textOutput += f"{getColorInfo(playerKnownColors[i])} {getRankInfo(playerKnownRanks[i])}"
        else:
            textOutput += getColoredTextStr(f"{getColorInfo(playerKnownColors[i])} {getRankInfo(playerKnownRanks[i])}", getColorInternal(playerHands[currentPlayer][i]))
            if debugMode:
                textOutput += f" ({getFormattedCardText(playerHands[currentPlayer][i])})"
        printFormattedColoredText(textOutput)
    print()

def printHand(handNum):
    for i in range(len(handNum)):
        printColoredText(f"{getFormattedCardText(handNum[i])}")
        print()

def getFormattedCardText(card):
    return getColoredTextStr(f"{getColor(card)} {getRank(card)} ({card})", getColorInternal(card))

def getColoredTextStr(text, colorStr):
    return f"\033[{colorStr}m{text}\033[0m"

def printFormattedColoredText(coloredText):
    os.system(f"Echo {coloredText}")

def printColoredText(text, color):
    os.system(f"Echo {getColoredTextStr(text, color)}")

def printPlayerInfo(currentPlayer):
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

    print("\nWhat you know about your hand: ")
    printPlayerKnowledge(currentPlayer, False)

def getPlayerInput():
    global debugMode
    action = input("What would you like to do? ")
    while(action.lower()== "h" or action.lower() == "help" or action.lower() == "e" or action.lower() == "debug"):
        if(action.lower() == "h" or action.lower() == "help"):
            printHelpMenu()
        elif(action.lower() == "e" or action.lower() == "debug"):
            if debugMode:
                print("Debug mode disabled!")
                debugMode = False
            else:
                print("Debug mode enabled")
                debugMode = True

        action = input("What would you like to do? ")
    return action

def printHelpMenu():
    print("Available Actions:")
    print("- Give a (H)int to a player (x remaining)")
    print("- (D)iscard a card and gain a hint")
    print("- (P)lay a card")
    print("- (Q)uit")
    print("- D(e)bug mode")

def processPlayerAction(action):
    if(action.lower() == "q" or action.lower() == "quit"):
        gameOver = True
    elif(action.lower() == "p" or action.lower() == "play"):
        print("placeholder")
    elif(action.lower() == "d" or action.lower() == "discard"):
        printPlayerKnowledge(currentPlayer, True)
        card = int(input("Which card would you like to discard?"))
    elif(action.lower() == "h" or action.lower() == "hint"):
        print("placeholder")

os.system("cls")
numPlayers = int(input("How many people are playing? "))
gameOver = False
currentPlayer = 0
action = ""

initGame(numPlayers)

while(gameOver == False and action != "q"):
    os.system("cls")
    printPlayerInfo(currentPlayer)

    action = getPlayerInput()
    processPlayerAction(action)
    currentPlayer = (currentPlayer + 1) % numPlayers
