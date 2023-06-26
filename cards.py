import random

class Card:
    def __init__(self, suit, value, ranking):
        self.suit = suit
        self.value = value
        self.ranking = ranking

def deck():
    suits = {"h", "d", "c", "s"}
    values = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"}
    full_deck = []
    for suit in suits:
        ranking = 2
        for value in values:
            full_deck.append(Card(suit, value, ranking))
            ranking += 1
    random.shuffle(full_deck)
    return full_deck



if __name__ == "__main__":
    print(deck())