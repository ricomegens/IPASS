import cards as cr
import poker as pl
import hands
import evaluate

class EHS:
    def __init__(self, player):
        self.ehs = self.hand_strength(player, poker_class.table_cards) \
                   * (1 - self.hand_potential(player, poker_class.table_cards)[1])\
                   + (1 - self.hand_strength(player, poker_class.table_cards)) \
                   * self.hand_potential(player, poker_class.table_cards)[0]

    def hand_strength(self, player, comm_cards):
        ahead = tied = behind = 0
        ourrank = self.rank(player, comm_cards)
        for oppcards in hands.opp_starts(player):
            opprank = self.rank(oppcards, comm_cards)
            if ourrank > opprank:
                ahead += 1
            elif ourrank == opprank:
                tied += 1
            else:
                behind += 1

        handstrength = (ahead + tied / 2) / (ahead + tied + behind)
        return handstrength

    def hand_potential(self, player, comm_cards):
        HP = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Hand potential array, initialize to 0
        HPTotal = [0, 0, 0]  # Initialize to 0
        ourrank = self.rank(player, comm_cards)

        for oppcards in hands.opp_starts(player):
            opprank = self.rank(oppcards, comm_cards)
            if ourrank > opprank:
                index = 0  # ahead
            elif ourrank == opprank:
                index = 1  # tied
            else:
                index = 2  # behind
            HPTotal[index] += 1

            for future_board_cards in hands.potential_table(comm_cards, player):
                ourbest = self.rank(player, future_board_cards)
                oppbest = self.rank(oppcards, future_board_cards)
                if ourbest > oppbest:
                    HP[index][0] += 1  # ahead
                elif ourbest == oppbest:
                    HP[index][1] += 1  # tied
                else:
                    HP[index][2] += 1  # behind

        Ppot = (HP[2][0] + HP[2][1] / 2 + HP[1][0] / 2) / (HPTotal[2] + HPTotal[1])
        Npot = (HP[0][2] + HP[1][2] / 2 + HP[0][1] / 2) / (HPTotal[0] + HPTotal[1])

        return Ppot, Npot

    def rank(self, player, comm_cards):
        return evaluate.rank(player, comm_cards)

if __name__ == "__main__":
    poker_class = pl.Poker()
    cards_deck = cr.Deck()