import cards
import player as pl


class Poker:
    def __init__(self):
        self.players = []
        self.deck = []
        self.comm_cards = []
        self.small_blind = 10
        self.big_blind = 20
        self.current_bet = self.big_blind
        self.pot = 0

    def update_pot(self, value):
        self.pot += value

    def reset_pot(self):
        self.pot = 0

    def add_player(self, player):
        if player not in self.players:
            self.players.append(player)
            return True
        else:
            return False

    def remove_player(self, player):
        if player in self.players:
            self.players.remove(player)
            return True
        return False

    def deal_hand(self, num_cards=2):
        for player in self.players:
            for card in range(num_cards):
                player.update_hand(self.deck.pop())

    def reset_hand(self):
        for player in self.players:
            player.reset_hand()

    def create_deck(self):
        self.deck = cards.shuffled_deck(cards.deck())

    def deal_comm_cards(self, num_cards):
        for card in range(num_cards):
            self.comm_cards.append(self.deck.pop())

    def reset_comm_cards(self):
        self.comm_cards.clear()

    def move(self, player, action=None):
        if not action:
            action = input("How do you want to play\n")
            while action != "fold" and action != "raise" and action != "check":
                action = input("Wrong input! How do you want to play\n")
        if action == "fold":
            self.remove_player(player)
        elif action == "check":
            player.update_money(-self.current_bet)
            self.update_pot(self.current_bet)
        elif action == "raise":
            self.current_bet += 10
            player.update_money(-self.current_bet)
            self.update_pot(self.current_bet)

    def give_away_pot(self, players):
        for player in players:
            cut = self.pot / len(players)
            player.update_money(cut)
        self.reset_pot()


if __name__ == "__main__":
    player1 = pl.Player("Rico")
    player2 = pl.Player("Luffy")
    game = Poker()
    game.add_player(player1)
    game.add_player(player2)

