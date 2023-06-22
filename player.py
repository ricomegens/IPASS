import poker as pl

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.money = 0

    def update_money(self, value):
        self.money += value

    def update_hand(self, card):
        self.hand.append(card)

    def reset_hand(self):
        self.hand.clear()

if __name__ == "__main__":
    player1 = Player("Rico")