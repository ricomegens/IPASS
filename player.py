class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.money = 0

    def update_money(self, value):
        """
            Function that returns True if addition succesfull.
        """
        self.money += value

    def update_hand(self, card):
        """
            Function that returns True if object added to list.
        """
        self.hand.append(card)

    def reset_hand(self):
        """
            Function that returns True if list was cleared.
        """
        self.hand.clear()

if __name__ == "__main__":
    player1 = Player("Rico")