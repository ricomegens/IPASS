import player
import poker
import hands
import evaluate

class EHS:
    def __init__(self, hand, comm_cards, deck):
        self.hand = hand
        self.comm_cards = comm_cards
        self.deck = deck

    def effective_hand_strength(self):
        return self.hand_strength() \
                   * (1 - self.hand_potential()[1])\
                   + (1 - self.hand_strength()) \
                   * self.hand_potential()[0]

    def hand_strength(self):
        ahead = tied = behind = 0
        ourrank = evaluate.rank(self.hand, self.comm_cards)
        for oppcards in hands.opp_starts(self.hand, self.comm_cards, self.deck):
            opprank = evaluate.rank(oppcards, self.comm_cards)
            if ourrank > opprank:
                ahead += 1
            elif ourrank == opprank:
                tied += 1
            else:
                behind += 1

        handstrength = (ahead + tied / 2) / (ahead + tied + behind)
        return handstrength

    def hand_potential(self):
        HP = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Hand potential array, initialize to 0
        HPTotal = [0, 0, 0]  # Initialize to 0
        ourrank = evaluate.rank(self.hand, self.comm_cards)

        for oppcards in hands.opp_starts(self.hand, self.comm_cards, self.deck):
            opprank = evaluate.rank(oppcards, self.comm_cards)
            if ourrank > opprank:
                index = 0  # ahead
            elif ourrank == opprank:
                index = 1  # tied
            else:
                index = 2  # behind
            HPTotal[index] += 1

            for future_board_cards in hands.potential_full_table(self.comm_cards, self.hand, self.deck):
                ourbest = evaluate.rank(self.hand, future_board_cards)
                oppbest = evaluate.rank(oppcards, future_board_cards)
                if ourbest > oppbest:
                    HP[index][0] += 1  # ahead
                elif ourbest == oppbest:
                    HP[index][1] += 1  # tied
                else:
                    HP[index][2] += 1  # behind

        Ppot = (HP[2][0] + HP[2][1] / 2 + HP[1][0] / 2) / (HPTotal[2] + HPTotal[1])
        Npot = (HP[0][2] + HP[1][2] / 2 + HP[0][1] / 2) / (HPTotal[0] + HPTotal[1])

        return Ppot, Npot


if __name__ == "__main__":
    player1 = player.Player("Rico")
    player2 = player.Player("Luffy")
    game = poker.Poker([player1, player2])
    dk = game.create_deck()
    player_hand = [dk[0], dk[4]]
    community = [dk[13], dk[21], dk[40]]
    ehs = EHS(player_hand, community, dk)
    print(ehs.effective_hand_strength())