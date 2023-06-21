import cards as deck
import player as pl
import evaluate
import effective_hand_strength
import algorithm_preflop

class Poker:
    def __init__(self):
        self.players = []
        self.deck = deck.Deck()
        self.table_cards = []
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
            del player
            return True
        return False

    def deal_hand(self, num_cards=2):
        for player in self.players:
            for card in range(num_cards):
                player.update_hand(self.deck.deal())

    def deal_table_cards(self, num_cards):
        for card in range(num_cards):
            self.table_cards.append(self.deck.deal())

    def move(self, player, action=None):
        while len(self.players) > 1:
            if not action:
                action = input("How do you want to play\n")
                while action != "fold" and action != "raise" and action != "check":
                    action = input("Wrong input! How do you want to play\n")
            if action == "fold":
                self.remove_player(player)
            elif action == "check":
                self.update_pot(self.current_bet)
            elif action == "raise":
                self.current_bet += 10
                self.update_pot(self.current_bet)
            return True
        return False

    def pre_flop(self):
        self.update_pot(self.small_blind)
        self.update_pot(self.big_blind)
        self.deal_hand()
        for player in self.players:
            self.move(player)

    def flop(self):
        self.deal_table_cards(3)
        for player in self.players:
            self.move(player)

    def turn(self):
        self.deal_table_cards(1)
        for player in self.players:
            self.move(player)

    def river(self):
        self.deal_table_cards(1)
        for player in self.players:
            self.move(player)

    def evaluate_win(self):
        player_scores = {}
        for player in self.players:
            score = evaluate.rank(player.hand, self.table_cards)
            player_scores.update({player : score})

        top_scorers = []
        for key, value in player_scores.items():
            if player_scores[key] == max(player_scores.values()):
                top_scorers.append(key)

        if len(top_scorers) == 1:
            top_scorers[0].update_money(self.pot)
            return top_scorers[0]
        for top_scorer in top_scorers:
            top_scorer.update_money(self.pot)
        return top_scorers


    def play(self):
        self.deck.reset()
        self.deck.shuffle()
        self.pre_flop()
        self.flop()
        self.turn()
        self.river()
        print(self.evaluate_win())
        return self.evaluate_win()

if __name__ == "__main__":
    player1 = pl.Player("Rico")
    player2 = pl.Player("Luffy")
    game = Poker()
    game.add_player(player1)
    game.add_player(player2)
    game.play()

