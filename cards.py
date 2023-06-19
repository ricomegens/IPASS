import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def ranking(self):
        if len(self.value) == 1:
            return int(self.value)
        elif self.value == "Ace":
            return 14
        elif self.value == "Jack":
            return 10
        elif self.value == "Queen":
            return 11
        elif self.value == "King":
            return 12

class Deck:
    def __init__(self):
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        self.cards = [Card(suit, value) for suit in self.suits for value in self.values]

    def reset(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        self.cards = [(suit, value, ranking) for suit in suits for value in values for ranking in range(1, 15)]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None


