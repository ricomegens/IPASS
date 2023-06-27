from itertools import combinations
import cards

def royal_flush(suits, values):
    return flush(suits) and set(values) == {10, 11, 12, 13, 14}

def straight_flush(suits, values):
    return flush(suits) and straight(values)

def four_of_a_kind(values):
    return any(values.count(value) == 4 for value in values)


def full_house(values):
    return three_of_a_kind(values) and pair(values)

def flush(suits):
    return any(suits.count(suit) == len(suits) for suit in suits)

def straight(values):
    return max(values) - min(values) == 4

def three_of_a_kind(values):
    return any(values.count(value) == 3 for value in values)

def two_pair(values):
    return sum(values.count(value) == 2 for value in values) == 4

def pair(values):
    return any(values.count(value) == 2 for value in values)

def rank(hand, comm_cards):
    full_hand = hand + comm_cards
    values = list(card.ranking for card in full_hand)
    suits = list(card.suit for card in full_hand)
    if royal_flush(suits, values):
        return 10
    elif straight_flush(suits, values):
        score = 0
        for i in range(min(values), max(values) + 1):
            score += i
        return 9, score
    elif four_of_a_kind(values):
        for value in values:
            if values.count(value) == 4:
                return 8, value * 4
    elif full_house(values):
        score = 0
        for value in values:
            if values.count(value) == 3 or values.count(value) == 2:
                score += value
        return 7, score
    elif flush(suits):
        return 6, sum(ranking for ranking in values)
    elif straight(values):
        score = 0
        for i in range(min(values), max(values)+1):
            score += i
        return 5, score
    elif three_of_a_kind(values):
        for value in values:
            if values.count(value) == 3:
                return 4, 3 * value
    elif two_pair(values):
        score = 0
        for value in values:
            if values.count(value) == 2:
                score += value
        return 3, score
    elif pair(values):
        for value in values:
            if values.count(value) == 2:
                return 2, value * 2
    else:
        return 1, sum(ranking for ranking in values)

def game_evaluate(players, comm_cards):
    scores = {}
    for player in players:
        scores.update({player : rank(player.hand, comm_cards)})
    print(scores)
    highest_score = max(scores.values())
    print(highest_score)
    for key in scores.keys():
        if key == highest_score:
            return key

if __name__ == "__main__":
    hand = [cards.Card("Spades", "7", 14), cards.Card("Spades", "7", 9)]
    for i in range(5):
        print(rank(hand, [cards.Card("Spades", "ace", 12), cards.Card("Spades", "8", 11), cards.Card("Spades", "8", 10)]))