from itertools import combinations

def royal_flush(values, suits):
    return flush(suits) and set(values) == {10, 11, 12, 13, 14}

def straight_flush(values, suits):
    return flush(suits) and max(values) - min(values) == 4

def four_of_a_kind(values):
    return any(values.count(value) == 4 for value in values)

def full_house(values):
    return three_of_a_kind(values) and pair(values)

def flush(suits):
    if (suits.count(suit) == 1 for suit in suits):
        return True
    return False

def straight(values, suits):
    return max(values) - min(values) == 4 and any(suits.count(suit) >= 2 for suit in suits)

def three_of_a_kind(values):
    return any(values.count(value) == 3 for value in values)

def two_pair(values):
    return sum(values.count(value) == 2 for value in values) == 4

def pair(values):
    return any(values.count(value) == 2 for value in values)

def rank(player, comm_cards):
    all_cards = player.hand + comm_cards
    all_possible_hands = list(combinations(all_cards, 5))
    for hand in all_possible_hands:
        values, suits = list(card.value for card in hand), list(card.suit for card in hand)
        if royal_flush(values, suits):
            return 10
        elif straight_flush(values, suits):
            return 9
        elif four_of_a_kind(values):
            return 8
        elif full_house(values):
            return 7
        elif flush(suits):
            return 6
        elif straight(values, suits):
            return 5
        elif three_of_a_kind(values):
            return 4
        elif two_pair(values):
            return 3
        elif pair(values):
            return 2
    return 1

if __name__ == "__main__":
    print()