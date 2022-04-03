import math, random

class Deck:
    def __init__(self):
        self.currentDeck = list(range(0,52))

    def dealCard(self):
        print(math.floor(random.random() * 52))

class Player:
    def __init__(self, name):
        self.name = name
        self.currentHand = []

    def printCurrentHand(self):
        print(self.name, "'s current hand is - ")

deck = Deck()
player = Player('Test')

while True:
    play = input('What is your play: (H)it or (S)tand?')
    if play.lower() == 'h':
        # deal a card
        deck.dealCard()
        player.printCurrentHand()
    elif play.lower() == 's':
        # reveal dealers hand and settle the bet
        print('Your hand is - ')
        print("The dealer's hand is - ")

        # evaluate winner
        print ('The winner is -')
        break
