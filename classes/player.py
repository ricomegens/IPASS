class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.money = 0

    def update_money(self, value):
        """
            Function that adds value to member attribute money.
        """
        self.money += value

    def update_hand(self, card):
        """
            Function that appends member of class Card to member's attribute hand.
        """
        self.hand.append(card)

    def reset_hand(self):
        """
            Function that clears member's hand.
        """
        self.hand.clear()