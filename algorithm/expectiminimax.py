from algorithm import evaluate, cardsCalculator


def hand_strength(hand, comm_cards, deck):
    """
        Function that calculates and returns how your hand stands in the game with
        a number representing between 0 and 1 and the amount of hands you beat, lose
        or tie againsts.

        Args:
        hand (list): list of members of class Card that belong to own hand
        comm_cards (list): list of members of class Card that are community cards
        deck (list): list with members of class that represent cards in play

        Returns:
        float: Returns strength of player's hand
        int: Returns amount of hands we are ahead from
        int: Returns amount of hands we are tied with
        int: Returns amount of hands we are behind
    """
    ahead = tied = behind = 0
    ourrank = evaluate.rank(hand, comm_cards)

    # calculate every possible opponent hand
    all_possible_oppcards = cardsCalculator.opp_starts(hand, comm_cards, deck)
    for opp_start in all_possible_oppcards:
        # while you loop through these hand, check how your hand stand against their possible hand
        opprank = evaluate.rank(opp_start, comm_cards)
        if ourrank > opprank:
            ahead += 1
        elif ourrank == opprank:
            tied += 1
        else:
            behind += 1

    handstrength = (ahead + tied / 2) / (ahead + tied + behind)
    return handstrength, ahead, tied, behind

def effective_hand_strength(hand, comm_cards, deck):
    """
        Function that calculates and returns how your hand stands in the game with
        a number representing between 0 and 1 and the amount of hands you beat, lose
        or tie againsts. This calculation is made in regard to more community cards
        to be revealed.

        Args:
        hand (list): list of members of class Card that belong to own hand
        comm_cards (list): list of members of class Card that are community cards
        deck (list): list with members of class that represent cards in play

        Returns:
        float: Returns strength of player's hand with more community cards yet to come
        int: Returns amount of hands we are ahead from
        int: Returns amount of hands we are tied with
        int: Returns amount of hands we are behind
    """
    HP = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Hand potential array, initialize to 0
    HPTotal = [0, 0, 0]  # Initialize to 0
    ourrank = evaluate.rank(hand, comm_cards)
    # calculate every possible opponent hand
    all_opp_starts = cardsCalculator.opp_starts(hand, comm_cards, deck)
    for oppcards in all_opp_starts:
        # while you loop through these hand, check how your hand stand against their possible hand
        opprank = evaluate.rank(oppcards, comm_cards)
        if ourrank[0] > opprank[0]:
            index = 0  # ahead
        elif ourrank[0] == opprank[0]:
            if ourrank[1] > opprank[1]:
                index = 0
            elif ourrank[1] == opprank[1]:
                index = 1
            else:
                index = 2
        else:
            index = 2  # behind
        HPTotal[index] += 1

        # check what cards can still come in to play and if your best with these cards
        # will beat their best
        remaing_cards = cardsCalculator.cards_left(hand, oppcards, comm_cards, deck)
        ourbest = evaluate.rank(hand, remaing_cards)
        oppbest = evaluate.rank(oppcards, remaing_cards)
        if ourbest[0] > oppbest[0]:
            HP[index][0] += 1  # ahead
        elif ourbest[0] == oppbest[0]:
            if ourbest[1] > oppbest[1]:
                HP[index][0] += 1
            elif ourbest[1] == oppbest[1]:
                HP[index][1] += 1
            else:
                HP[index][2] += 1
        else:
            HP[index][2] += 1  # behind

    handstrength = hand_strength(hand, comm_cards, deck)
    # calculate the possibilty that while we are ahead now, what is the chance we fall behind
    Ppot = (HP[2][0] + HP[2][1] / 2 + HP[1][0] / 2) / (HPTotal[2] + HPTotal[1])
    # calculate the possibilty that while we are behind now, what is the chance of getting ahead
    Npot = (HP[0][2] + HP[1][2] / 2 + HP[0][1] / 2) / (HPTotal[0] + HPTotal[1])
    result = handstrength[0] * (1 - Npot) + (1 - handstrength[0]) * Ppot
    situations_win = 0
    situations_lose = 0
    situations_tie = 0
    for future in HP:
        situations_win += future[0]
        situations_tie += future[1]
        situations_lose += future[2]
    return result, situations_win, situations_tie, situations_lose

def own_hand_calculator(hand, comm_cards, deck):
    """
            Function that calculates and returns how your hand stands in the game with
            a number representing between 0 and 1 and the amount of hands you beat, lose
            or tie againsts.

            Args:
            hand (list): list of members of class Card that belong to own hand
            comm_cards (list): list of members of class Card that are community cards
            deck (list): list with members of class that represent cards in play

            Returns:
            float: Returns strength of player's hand
            int: Returns amount of hands we are ahead from
            int: Returns amount of hands we are tied with
            int: Returns amount of hands we are behind
        """
    ahead = tied = behind = 0

    # calculate every possible opponent hand
    all_possible_oppcards = cardsCalculator.opp_starts(hand, comm_cards, deck)
    for opp_start in all_possible_oppcards:
        all_possible_board_combis = cardsCalculator.potential_full_table(hand, opp_start, comm_cards, deck)
        # print(len(all_possible_board_combis))
        for possible_board_combi in all_possible_board_combis:
            whole_potential_board = comm_cards + possible_board_combi
            opprank = evaluate.rank(opp_start, whole_potential_board)
            ourrank = evaluate.rank(hand, whole_potential_board)
            if ourrank > opprank:
                ahead += 1
            elif ourrank == opprank:
                tied += 1
            else:
                behind += 1

    handstrength = (ahead + tied / 2) / (ahead + tied + behind)
    return handstrength, ahead, tied, behind

def expectiminimax(hand, comm_cards, deck):
    """
        Function that checks if hand strength or effective hand strength is to be calculated
        and returns action to be made by player based on odds.

        Args:
        hand (list): list of members of class Card that belong to own hand
        comm_cards (list): list of members of class Card that are community cards
        deck (list): list with members of class that represent cards in play

        Returns:
        string: Returns action to be done by player
    """
    if len(comm_cards) == 5:
        chance = hand_strength(hand, comm_cards, deck)
    else:
        chance = effective_hand_strength(hand, comm_cards, deck)
    if chance[0] > 0.8:
        return "raise", chance[0], chance[1], chance[2], chance[3]
    elif chance[0] > 0.5:
        return "check", chance[0], chance[1], chance[2], chance[3]
    else:
        return "fold", chance[0], chance[1], chance[2], chance[3]