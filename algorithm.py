import cards_to_come
import evaluate

class Expectiminimax:
    def __init__(self, player, comm_cards):
        self.hand = player.hand
        self.comm_cards = comm_cards

    def effective_hand_strength(self):
        HP = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Hand potential array, initialize to 0
        HPTotal = [0, 0, 0]  # Initialize to 0
        ourrank = evaluate.rank(self.hand, self.comm_cards)

        all_opp_starts = cards_to_come.opp_starts(self.hand, self.comm_cards)
        for oppcards in all_opp_starts:
            opprank = evaluate.rank(oppcards, self.comm_cards)
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

            remaing_cards = cards_to_come.cards_left(self.hand, oppcards, self.comm_cards)
            ourbest = evaluate.rank(self.hand, remaing_cards)
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

        hand_strength = (HPTotal[0] + 0.5 * HPTotal[1]) / sum(number for number in HPTotal)
        Ppot = (HP[2][0] + HP[2][1] / 2 + HP[1][0] / 2) / (HPTotal[2] + HPTotal[1])
        Npot = (HP[0][2] + HP[1][2] / 2 + HP[0][1] / 2) / (HPTotal[0] + HPTotal[1])
        result = hand_strength * (1 - Npot) + (1 - hand_strength) * Ppot
        situations_win = 0
        situations_lose = 0
        situations_tie = 0
        for future in HP:
            situations_win += future[0]
            situations_tie += future[1]
            situations_lose += future[2]
        return result, situations_win, situations_tie, situations_lose

    def expectiminimax(self):
        chance = EHS(self.hand, self.comm_cards).effective_hand_strength()[0]
        if chance > 0.8:
            return "raise"
        elif chance > 0.5:
            return "check"
        else:
            return "fold"