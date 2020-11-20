# built-In module(s) and Package(s)
import os
from random import shuffle
import time

# shows name of the game at the top
def showGameName():
    print("***********************************")
    print("***                             ***")
    print("***       \033[1mWAR CARD GAME\033[0m         ***")
    print("***                             ***")
    print("***********************************")

# shows description and rules of a game
def showDescAndRule():
    print("\n")
    print("\033[1mDESCRIPTION\033[0m  :: War, or Battle, is a played with two players and a standard 52")
    print("\t\tplaying card deck. In War, cards are ranked Aces high and 2s low.")
    print("\t\tThe objective of the game is to win all of the cards in the deck.")

    print("\n")
    print("\033[1mRULES\033[0m\t     ::\t(1) Each player gets dealt half the deck, 26 cards, and the cards")
    print("\t\tare put face down in a stack in front of the players.")
    print("\n")
    print("\t\t(2) Both players turn their top card face up at the same time. The")
    print("\t\tperson with the higher card wins that draw, and takes both the cards.")
    print("\n")
    print("\t\t(3) If both players draw a card of the same rank, then there's a WAR.")
    print("\t\tThe face up cards are left on the table and each player puts two cards")
    print("\t\tface down on the table, and then puts one card face up. The face up card")
    print("\t\tdetermines who wins the war and gets all 8 cards that are on the table at")
    print("\t\tthis point. If the face up card is again the same rank, then the war goes")
    print("\t\ton, two more face down, one face up etc.")
    print("\n")
    print("\t\t(4) First player to finish all their cards loses the game.")
    print("\n")
    print("\t\t(5) If a player finishes their cards during a war without having enough")
    print("\t\tcards to finish the war then he loses immediately.")

class Player:
    def __init__(self, name):
        self.name = name
        self.playerDeck = []

    def getCard(self):
        return self.playerDeck.pop(0)

    def addCard(self, cardObject):
        if type(cardObject) == list:
            self.playerDeck.extend(cardObject)
        else:
            self.playerDeck.append(cardObject)

    def __str__(self):
        return self.name

class Card:
    def __init__(self, name="", value=0):
        self.name = name
        self.value = value

    def createCardDeck(self):
        cards = []
        for suit in suitList:
            for name in cardList.keys():
                cards.append(Card(name + ' of ' + suit, cardList[name]))
        return cards

    def __str__(self):
        return self.name

def displayRounds():
    # clear the console
    os.system("clear")

    # shows the name of a game at the top
    showGameName()

    # show round number
    print("\n")
    print(f"  ROUND {rounds}  ".center(38, " "))
    print("\n")

    print(f'{playerOne}({len(playerOne.playerDeck)})'.center(len(playerOneTableCard[-1].name), " ") + ' '*8
    + f'{playerTwo}({len(playerTwo.playerDeck)})'.center(len(playerTwoTableCard[-1].name), " "))

    print("\n")
    print(f'{playerOneTableCard[-1]}' + 'VS'.center(8, " ") + f'{playerTwoTableCard[-1]}')
    print("\n")

def checkForEmptyDeck():
    if len(playerOne.playerDeck) == 0:
        print("\n")
        print(f'{playerOne}, out of cards! {playerTwo} wins!!')
        print("\n")
        return True

    elif len(playerTwo.playerDeck) == 0:
        print("\n")
        print(f'{playerTwo}, out of cards! {playerOne} wins!!')
        print("\n")
        return True

    else:
        return False

def checkForWar():
    if playerOneTableCard[-1].value > playerTwoTableCard[-1].value:
        playerOne.addCard(playerOneTableCard)
        playerOne.addCard(playerTwoTableCard)
        #shuffle cards
        shuffle(playerOne.playerDeck)
        print(f"({playerOne} wins this round)".center(38, " "))
        return False

    elif playerTwoTableCard[-1].value > playerOneTableCard[-1].value:
        playerTwo.addCard(playerOneTableCard)
        playerTwo.addCard(playerTwoTableCard)
        #shuffle cards
        shuffle(playerTwo.playerDeck)
        print(f"({playerTwo} wins this round)".center(38, " "))
        return False

    else:
        return True

# global variable(s)
validOption = False
suitList = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
cardList = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
rounds = 1
gameOn = True

os.system("clear")

# shows the name of a game at the top
showGameName()

# shows game description and rules
showDescAndRule()

# put 5 seconds delay
time.sleep(5)

# Looping continue till players choose an option within range [1-4]
while not validOption:
    # clear the console
    os.system("clear")
    # shows the name of a game at the top
    showGameName()
    # Show options for how to player wants to play
    print("\n")
    print(" \033[1mChoose Option\033[0m ".center(32, "*"))
    print("\n")
    print("1. Continue")
    print("2. Exit")
    print("\n")
    # get player choice
    playOption = input("[1-2] : ")
    # Check whether the player's input is a valid option or not
    if playOption.isdigit() and int(playOption) > 0 and int(playOption) < 5:
        playOption = int(playOption)
        validOption = True
        break

# check if choice is 1
if playOption == 1:
    playerOneName = input("\nEnter Player One name : ")
    if len(playerOneName) == 0:
        playerOne = Player("Player One")
    else:
        playerOne = Player(playerOneName)

    playerTwoName = input("\nEnter Player Two name : ")
    if len(playerTwoName) == 0:
        playerTwo = Player("Player Two")
    else:
        playerTwo = Player(playerTwoName)
    #create a deck of cards
    obj = Card()
    deckOfCard = obj.createCardDeck()
    #shuffle cards
    shuffle(deckOfCard)

    #spilt cards between 2 players
    for _ in range(26):
        playerOne.addCard(deckOfCard.pop(0))
        playerTwo.addCard(deckOfCard.pop(0))

    while gameOn:
        playerOneTableCard = []
        playerTwoTableCard = []

        if checkForEmptyDeck():
            gameOn = False
            break

        playerOneTableCard.append(playerOne.playerDeck.pop(0))
        playerTwoTableCard.append(playerTwo.playerDeck.pop(0))

        displayRounds()

        if checkForWar():
            war = True
            while war:
                print("It's a WAR !! Draw 3 cards".center(38, " "))
                time.sleep(2)

                for _ in range(3):
                    if checkForEmptyDeck():
                        gameOn = False
                        war = False
                        break

                    playerOneTableCard.append(playerOne.playerDeck.pop(0))
                    playerTwoTableCard.append(playerTwo.playerDeck.pop(0))
                else:
                    print("\n")
                    print(f'{playerOneTableCard[-1]}' + 'VS'.center(8, " ") + f'{playerTwoTableCard[-1]}')
                    print("\n")

                    time.sleep(2)

                    if not checkForWar():
                        war = False

        rounds += 1
        time.sleep(1.5)

# check if choice is 2
else:
    exit()
