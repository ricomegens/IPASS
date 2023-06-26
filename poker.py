import cards
import player as pl
import evaluate

class Poker:
    def __init__(self, players):
        self.players = players
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
        self.players.append(player)
        return True

    def remove_player(self, player):
        if player in self.players:
            self.players.remove(player)
            return True
        return False

    def deal_hand(self, num_cards=2):
        for player in self.players:
            for card in range(num_cards):
                player.update_hand(self.deck.deal())

    def reset_hand(self):
        for player in self.players:
            player.reset_hand()

    def create_deck(self):
        return cards.deck()

    def deal_comm_cards(self, num_cards):
        for card in range(num_cards):
            self.comm_cards.append(self.deck.deal())

    def reset_comm_cards(self):
        self.comm_cards.clear()

    def move(self, player, action=None):
        while len(self.players) > 1:
            if not action:
                print('test')
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
            return True
        return False

    def pre_flop(self):
        self.update_pot(self.small_blind)
        self.update_pot(self.big_blind)
        self.deal_hand()
        for player in self.players:
            self.move(player, "check")

    def flop(self):
        self.deal_comm_cards(3)
        for player in self.players:
            self.move(player, action="check")

    def turn(self):
        self.deal_comm_cards(1)
        for player in self.players:
            self.move(player, action="check")

    def river(self):
        self.deal_comm_cards(1)
        for player in self.players:
            self.move(player, action="check")

    def evaluate_game(self):
        player_scores = {}
        for player in self.players:
            score = evaluate.rank(player.hand, self.comm_cards)
            player_scores.update({player : score})
        print(player_scores)
        top_scorers = []
        for key, value in player_scores.items():
            if player_scores[key] == max(player_scores.values()):
                top_scorers.append(key)
        return top_scorers

    def give_away_pot(self):
        winners = self.evaluate_game()
        if len(winners) == 1:
            winners[0].update_money(self.pot)
        else:
            amount_of_winners = len(winners)
            share = self.pot / amount_of_winners
            for winner in winners:
                winner.update_money(share)
        self.reset_pot()
        return winners

    def play(self):
        self.create_deck()
        self.pre_flop()
        self.flop()
        self.turn()
        self.give_away_pot()
        self.reset_hand()
        self.reset_table_cards()

if __name__ == "__main__":
    player1 = pl.Player("Rico")
    player2 = pl.Player("Luffy")
    game = Poker([player1, player2])
    for i in range(20):
        game.play()

