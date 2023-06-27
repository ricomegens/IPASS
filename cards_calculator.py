from itertools import combinations
import cards

def opp_starts(own_cards, comm_cards):
    known = own_cards + comm_cards
    deck = cards.deck()
    for card in known:
        if card in deck:
            deck.remove(card)
    combis = list(combinations(deck, 2))
    combi = [list(combi) for combi in combis]
    return combi

# def potential_full_table(own_cards, opp_cards, comm_cards, deck):
#     amount_of_cards_to_come = 5 - len(comm_cards)
#     known_cards = own_cards + comm_cards
#     for card in known_cards:
#         if card in deck:
#             deck.remove(card)
#     deck_copy = deck.copy()
#     for card in opp_cards:
#         if card in deck:
#             deck_copy.remove(card)
#     cards_to_come = list(combinations(deck_copy, amount_of_cards_to_come))
#     combis = [list(card) for card in cards_to_come]
#     return combis

def cards_left(own_cards, opp_cards, comm_cards):
    known_cards = own_cards + comm_cards
    deck = cards.deck()
    for card in known_cards:
        if card in deck:
            deck.remove(card)
    deck_copy = deck.copy()
    for card in opp_cards:
        if card in deck:
            deck_copy.remove(card)
    return deck_copy

if __name__ == "__main__":
    dk = cards.deck()
    player_hand = [dk[30], dk[8]]
    community = [dk[12], dk[49], dk[21]]
    opp = opp_starts(player_hand, community, dk)
    print(len(potential_full_table(player_hand, opp[0], community, dk)))