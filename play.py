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

    def calculate_hands(self, player, table):
        all_cards = player.hand + table
        values = [card.ranking() for card in all_cards]
        suits = [card.suit for card in all_cards]

        if self.royal_flush(values, suits):
            return 10
        elif self.straight_flush(values, suits):
            return 9
        elif self.four_of_a_kind(values):
            return 8
        elif self.full_house(values):
            return 7
        elif self.flush(suits):
            return 6
        elif self.straight(values, suits):
            return 5
        elif self.three_of_a_kind(values):
            return 4
        elif self.two_pair(values):
            return 3
        elif self.pair(values):
            return 2
        else:
            return 1

    def royal_flush(self, values, suits):
        return self.flush(suits) and set(values) == {10, 11, 12, 13, 14}

    def straight_flush(self, values, suits):
        return self.flush(suits) and max(values) - min(values) == 4

    def four_of_a_kind(self, values):
        return any(values.count(value) == 4 for value in values)

    def full_house(self, values):
        return self.is_three_of_a_kind(values) and self.is_pair(values)

    def flush(self, suits):
        if (suits.count(suit) == 1 for suit in suits):
            return True
        return False

    def straight(self, values, suits):
        return max(values) - min(values) == 4 and any(suits.count(suit) >= 2 for suit in suits)

    def three_of_a_kind(self, values):
        return any(values.count(value) == 3 for value in values)

    def two_pair(self, values):
        return sum(values.count(value) == 2 for value in values) == 4

    def pair(self, values):
        return any(values.count(value) == 2 for value in values)

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