import random

class Card:
    def __init__(self, suit, value, ranking):
        self.suit = suit
        self.value = value
        self.ranking = ranking

def deck():
    """
        Function that creates class object, adds them to a list and
        returns a list of classes object

        Returns:
        list: Returns list with members of class Card
    """
    suits = {"h", "d", "c", "s"}
    values = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"}
    full_deck = []
    for suit in suits:
        # for each value that we go up in the list, add 1 to the ranking and create a Card object with
        # corresponding suit, value and ranking that we can add to a list
        ranking = 2
        for value in values:
            full_deck.append(Card(suit, value, ranking))
            ranking += 1
    return full_deck

def shuffled_deck(deck):
    """
        Function that shuffles argument

        Args:
        deck (list): list with members of class that represent cards in play

        Returns:
        list: Returns list with members of class Card that is shuffled
    """
    # Shuffle the list and return it
    random.shuffle(deck)
    return deck