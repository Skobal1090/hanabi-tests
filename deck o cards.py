import random
import os

def getRank(card):
    normRank=card%13
    if(normRank==0):
        return "A"
    elif(0<normRank<=9):
        return str(normRank+1)
    elif(normRank==10):
        return "J"
    elif(normRank==11):
        return "Q"
    elif(normRank==12):
        return "K"

def getSuit(card):
    normSuit=card//13
    if(normSuit==0):
        return " of Spades"
    elif(normSuit==1):
        return " of Clubs"
    elif(normSuit==2):
        return " of Hearts"
    elif(normSuit==3):
        return " of Diamonds"

dealtCards = []
handSize = 5
hands = []
numHands = 4

def dealHand():
    hand = []
    while len(hand)<handSize:
        card=random.randint(0,51)
        if(card not in dealtCards):
            dealtCards.append(card)
            hand.append(card)
    return hand

def printHand(hand):
    for i in range(len(hand)):
        print(getRank(hand[i]) + getSuit(hand[i]) + " (" +str(hand[i])+ ")")

for i in range(numHands):
    hands.append(dealHand())

printHand(hands[2])
