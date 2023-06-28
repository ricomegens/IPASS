from itertools import combinations

def opp_starts(own_cards, comm_cards, deck):
    """
        Function that returns a list off all possible combination of cards the
        opponents player may have

        Args:
        own_cards (list): list with members of class Card that belong to own hand
        comm_cards (list): list with members of class Card that are community cards
        deck (list): list with members of class that we want to remove cards out

        Returns:
        list: Returns list of cards combinations
    """
    known = own_cards + comm_cards
    for card in known:
        if card in deck:
            deck.remove(card)
    combis = list(combinations(deck, 2))
    combi = [list(combi) for combi in combis]
    return combi

def potential_full_table(own_cards, opp_cards, comm_cards, deck):
    """
        Function that returns a list off all possible combination of cards the
        table may get

        Args:
        own_cards (list): list with members of class Card that belong to own hand
        comm_cards (list): list with members of class Card that are community cards
        deck (list): list with members of class that we want to remove cards out

        Returns:
        list: Returns list of cards combinations
    """
    amount_of_cards_to_come = 5 - len(comm_cards)
    known_cards = own_cards + comm_cards
    for card in known_cards:
        if card in deck:
            deck.remove(card)
    deck_copy = deck.copy()
    for card in opp_cards:
        if card in deck:
            deck_copy.remove(card)
    cards_to_come = list(combinations(deck_copy, amount_of_cards_to_come))
    combis = [list(card) for card in cards_to_come]
    return combis

def cards_left(own_cards, opp_cards, comm_cards, deck):
    """
        Function that returns the list of the remaining cards after removing all
        the known cards (your own hand and community cards) and possible opponent hand

        Args:
        own_cards (list): list of members of class Card that belong to own hand
        opp_cards (list): list of members of class Card that the opponent may hold
        comm_cards (list): list of members of class Card that are community cards
        deck (list): list with members of class that we want to remove cards out

        Returns:
        list: Returns list with cards remaining
    """
    # make a list of all the known cards and remove them from the deck
    known_cards = own_cards + comm_cards
    for card in known_cards:
        if card in deck:
            deck.remove(card)
    # copy the deck so when we remove the potential opponent hand's it
    # does not actually remove the cards
    # remove the opponent's hand and return the deck
    deck_copy = deck.copy()
    for card in opp_cards:
        if card in deck:
            deck_copy.remove(card)
    return deck_copy