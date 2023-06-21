import random

class Card:
    def __init__(self, suit, value, ranking):
        self.suit = suit
        self.value = value
        self.ranking = ranking

class Deck:
    def __init__(self):
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.cards = []

    def reset(self):
        for suit in self.suits:
            ranking = 2
            for value in self.values:
                self.cards.append(Card(suit, value, ranking))
                ranking += 1

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None

if __name__ == "__main__":
    deck = Deck()
    print(len(deck.cards))
    deck.reset()
    print(len(deck.cards))
    deck.deal()
    print(len(deck.cards))