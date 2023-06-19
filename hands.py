import cards as cr
import poker as pl
import player as pr
from itertools import combinations

def cards_in_play(player):
    hand = [card for card in player.hand]
    comm_cards = [card for card in poker_class.table_cards]
    return cards_class.cards - (hand + comm_cards)

def opp_starts(player):
    return list(combinations(cards_in_play(player), 2))

def potential_table(comm_cards):
    if len(comm_cards) == 3:
        new = list(combinations(cards_class.cards, 2))
        for new_table_cards in new:
            new_table_cards = list(new_table_cards)
            new_table_cards + comm_cards
        return new
    if len(comm_cards) == 4:
        new = list(combinations(cards_class.cards, 1))
        for new_table_cards in new:
            new_table_cards = list(new_table_cards)
            new_table_cards + comm_cards
        return new


if __name__ == "__main__":
    cards_class = cr.Deck()
    poker_class = pl.Poker()
    player1 = pr.Player("Rico")
    opp_starts()