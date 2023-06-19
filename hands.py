import cards as cr
import poker as pl
import player as pr
import combinations from itertools

def cards_out_of_play(player):
    hand = [card for card in player.hand]
    comm_cards = [card for card in poker_class.table_cards]
    return hand + comm_cards

def opp_starts(player):
    all_starts = list(combinations(cards_class.cards, 2))
    hand = [card for card in player.hand]
    comm_cards = [card for card in poker_class.table_cards]
    to_remove = hand + comm_cards
    for card in to_remove:
        for start in all_starts:
            if card in start:
                    all_starts.remove(start)

if __name__ == "__main__":
    cards_class = cr.Deck()
    poker_class = pl.Poker()
    player1 = pr.Player("Rico")
    opp_starts()