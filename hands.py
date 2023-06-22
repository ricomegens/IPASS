import cards as cr
import poker as pl
from itertools import combinations
def cards_in_play(own_cards, comm_cards, deck):
    hand = [card for card in own_cards]
    community = [card for card in comm_cards]
    known = hand + community
    for card in known:
        if card in deck:
            deck.remove(card)
    return deck

def opp_starts(own_cards, comm_cards, deck):
    combis = list(combinations(cards_in_play(own_cards, comm_cards, deck), 2))
    combi = [list(combi) for combi in combis]
    return combi

def potential_full_table(own_cards, comm_cards, deck):
    table = 5
    known = len(comm_cards)
    amount_of_cards_to_come = 5 - known
    cards_to_come = list(combinations(cards_in_play(own_cards, comm_cards, deck), amount_of_cards_to_come))
    potential_full_tables = []
    for new_comm_cards in cards_to_come:
        new_comm_cards = list(new_comm_cards)
        potential_full_tables.append(list(new_comm_cards + comm_cards))
    return potential_full_tables


if __name__ == "__main__":
    poker_class = pl.Poker()
    a = cr.Deck()
    a.reset()
    dk = a.cards
    player_hand = [dk[30], dk[8]]
    community = [dk[12], dk[49], dk[21]]
    print(len(opp_starts(player_hand, community, dk)))