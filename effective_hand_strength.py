import player
import poker
import cards_to_come
import cards
import evaluate

class EHS:
    def __init__(self, hand, comm_cards, deck):
        self.hand = hand
        self.comm_cards = comm_cards
        self.deck = deck

    def effective_hand_strength(self):
        hp = self.hand_potential()
        return hp[2] \
                   * (1 - hp[1])\
                   + (1 - hp[2]) \
                   * hp[0]

    def hand_potential(self):
        HP = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Hand potential array, initialize to 0
        HPTotal = [0, 0, 0]  # Initialize to 0
        ourrank = evaluate.rank(self.hand, self.comm_cards)

        all_opp_starts = cards_to_come.opp_starts(self.hand, self.comm_cards, self.deck)
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

            remaing_cards = cards_to_come.cards_left(self.hand, oppcards, self.comm_cards, self.deck)
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
        return Ppot, Npot, hand_strength

if __name__ == "__main__":
    dk = cards.deck()
    player_hand = [dk[14], dk[23]]
    player2_hand = [dk[37], dk[38]]
    community = [dk[13], dk[21], dk[40]]
    ehs1 = EHS(player_hand, community, dk)
    ehs2 = EHS(player2_hand, community, dk)
    print(ehs1.effective_hand_strength())
    print(ehs2.effective_hand_strength())