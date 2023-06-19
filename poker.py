import cards as deck
import player as pl

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

    def add_player(self, player):
        new_player = pl.Player(player)
        self.players.append(new_player)

    def remove_player(self, player):
        if player in self.players:
            self.players.remove(player)
            del player

    def deal_hand(self, num_cards=2):
        for player in self.players:
            for card in range(num_cards):
                player.update_hand(self.deck.deal())

    def deal_table_cards(self, num_cards):
        for card in range(num_cards):
            self.table_cards.append(self.deck.deal())

    def choice(self):
        for player in self.players():
            play = input("What do you want to do: ")
            while play != "fold" or play != "check" or play != "raise":
                if play == "fold":
                    player.fold()
                elif play == "check":
                    player.check()
                elif play == "raise":
                    player.raise_pot()

    def evaluate_hands(self):
        player_scores = {}
        for player in self.players:
            score = self.calculate_hand_score(player.hand)
            player_scores.update({player : score})

        scoring = dict(sorted(player_scores.items(), key=lambda x: x[1], reverse=True))
        winner = next(iter(scoring))
        winner.update(self.pot)
        return

    def pre_flop(self, players):
        for player in players:
            self.add_player(player)
        while len(self.players) < 2:
            print("Not enough players")
            return False
        self.deck.reset()
        self.deck.shuffle()
        self.deal_hand()
        self.choice()
        if len(self.players) > 1:
            return self.flop()
        return self.players[0].update_money(self.pot)

    def flop(self):
        self.deal_table_cards(2)
        self.choice()
        if len(self.players) > 1:
            return self.turn()
        return self.players[0].update_money(self.pot)

    def turn(self):
        self.deal_table_cards(1)
        self.choice()
        if len(self.players) > 1:
            return self.river()
        return self.players[0].update_money(self.pot)

    def river(self):
        self.deal_table_cards(1)
        self.choice()
        self.evaluate_win()
        return