import poker as pl

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.money = 0
        self.hand_rank = None
        self.poker = pl.Poker()

    def update_hand(self, cards):
        for card in cards:
            self.hand.append(card)

    def check(self):
        self.poker.update_pot(self.poker.current_bet)
        self.money -= self.poker.current_bet
        return

    def fold(self):
        del self.hand
        self.poker.remove_player(self)
        return

    def raise_pot(self):
        quantity = input("How much do you want to raise: ")
        while quantity != int:
            print("Wrong input")
            quantity = input("How much do you want to raise: ")
        self.poker.update_pot(self.poker.current_bet + quantity)
        self.poker.current_bet += quantity
        self.money -= self.poker.current_bet
        return

    def update_money(self, value):
        self.money += value
