import cards

def royal_flush(suits, values):
    """
        Function that returns boolean if list values corresponds
        of the following values and suits contains of one suit

        Args:
        suits (list): list of attributes (suit) of class Card
        values (list): list of attributes (value) of class Card

        Returns:
        bool: Returns boolean according to statement truth
    """
    return flush(suits) and set(values) == {10, 11, 12, 13, 14}

def straight_flush(suits, values):
    """
        Function that returns True if list values corresponds
        of the five values in a row and suits contains of one suit

        Args:
        suits (list): list of attributes (suit) of class Card
        values (list): list of attributes (value) of class Card

        Returns:
        bool: Returns boolean according to statement truth
    """
    return flush(suits) and straight(values)

def four_of_a_kind(values):
    """
        Function that returns boolean according t if list values corresponds
        of four of the same elements

        Args:
        values (list): list of attributes (value) of class Card

        Returns:
        bool: Returns boolean according to statement truth
    """
    return any(values.count(value) == 4 for value in values)


def full_house(values):
    """
        Function that returns boolean according to if list values corresponds
        of the following values

        Args:
        values (list): list of attributes (value) of class Card

        Returns:
        bool: Returns boolean according to statement truth
    """
    return three_of_a_kind(values) and pair(values)

def flush(suits):
    """
        Function that returns boolean according to if list suits corresponds
        of one suit

        Args:
        suits (list): list of attributes (suit) of class Card

        Returns:
        bool: Returns boolean according to statement truth
    """
    return any(suits.count(suit) == len(suits) for suit in suits)

def straight(values):
    """
        Function that returns boolean according to if list values corresponds
        of five values in row

        Args:
        values (list): list of attributes (value) of class Card

        Returns:
        bool: Returns boolean according to statement truth
    """
    return max(values) - min(values) == 4

def three_of_a_kind(values):
    """
        Function that returns boolean according to if list values corresponds
        of three same values

        Args:
        values (list): list of attributes (value) of class Card

        Returns:
        bool: Returns boolean according to statement truth
    """
    return any(values.count(value) == 3 for value in values)

def two_pair(values):
    """
        Function that returns boolean according to if list values corresponds
        of two same values twice

        Args:
        values (list): list of attributes (value) of class Card

        Returns:
        bool: Returns boolean according to statement truth
    """
    return sum(values.count(value) == 2 for value in values) == 4

def pair(values):
    """
        Function that returns boolean according to if list values corresponds
        of two same values

        Args:
        values (list): list of attributes (value) of class Card

        Returns:
        bool: Returns boolean according to statement truth
    """
    return any(values.count(value) == 2 for value in values)

def rank(hand, comm_cards):
    """
        Function that calculates what sort of hand is being held and the ranking
        of that hand incase there will be a tie

        Args:
        hand (list): list of members of class Card in possesion of a player
        comm_cards (list): list of members of class Card that are community cards

        Returns:
        tuple: Returns tuple with first element being hand ranking
        from one to ten and second element being hand ranking in that rank
    """
    full_hand = hand + comm_cards
    # make a list of the values and rankings of the full hand
    # (community cards and player hand) so the hand ranking can be calculated
    values = list(card.ranking for card in full_hand)
    suits = list(card.suit for card in full_hand)
    # calculate the sort hand and that hand's ranking
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
    """
        Function that calculates scores of players hands and returns the
        player with the highest ranking hand

        Args:
        players (list): list of members of class Player
        comm_cards (list): list of members of class Card that are community cards

        Returns:
        class: Returns player with highest ranking hand
    """
    # for each player remember their score
    scores = {}
    for player in players:
        scores.update({player : rank(player.hand, comm_cards)})
    # get the highest score and see what player has that score, return the player
    highest_score = max(scores.values())
    for key in scores.keys():
        if scores[key] == highest_score:
            return key