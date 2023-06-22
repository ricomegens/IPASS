import poker as pl

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.money = 0
        self.poker = pl.Poker()

    def update_money(self, value):
        self.money += value

    def update_hand(self, card):
        self.hand.append(card)

    def reset_hand(self):
        self.hand.clear()

    def check(self):
        self.poker.update_pot(self.poker.current_bet)
        self.update_money(-self.poker.current_bet)
        return

    def fold(self):
        self.poker.remove_player(self)
        self.hand.clear()

    def raise_pot(self, value):
        if type(value) != int or type(value) != float:
            print("Wrong input")
            return False
        self.poker.update_pot(self.poker.current_bet + value)
        self.poker.current_bet += value
        self.update_money(-(self.poker.current_bet + value))
        return

if __name__ == "__main__":
    player1 = Player("Rico")