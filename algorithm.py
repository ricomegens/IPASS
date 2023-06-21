import effective_hand_strength
from itertools import combinations
import poker

class Node:
    def __init__(self, value):
        self.value = value
        self.chance_node = None
        self.node_after_chance = None
        self.l_edge = None
        self.r_edge = None

    def node_r(self, player):
        alg = algorithm_flop.EHS(player)
        value = alg.ehs
        return value

    def node_l(self, player):
        alg = effective_hand_strength.EHS(player)
        value = alg.ehs
        value -= potOdd()
        return abs(value)

class Move:
    def __init__(self, move, value):
        self.move = move
        self.value = value

class Tree:
    # players is variable but still hard coded to 2 players
    def __init__(self, players):
        self.players = players

    def make_tree(self):
        potential_starts = Node(len(list(combinations(poker_class.deck, 2))))
        is_max_turn = Node(None)
        potential_starts.node_after_chance = is_max_turn

        fold1_1 = Node(Node.node_l(self.players[0]))
        play_1_1 = Node(Node.node_r(self.players[0]))
        is_max_turn.l_edge = fold1_1
        is_max_turn.r_edge = play_1_1

        fold2_1 = Node(Node.node_l(self.players[1]))
        play2_1 = Node(Node.node_r(self.players[1]))
        play_1_1.l_edge = fold2_1
        play_1_1.r_edge = play2_1

        potential_flops = Node(len(list(combinations(poker_class.deck, 3))))
        play2_1.chance_node = potential_flops
        is_max_turn1 = Node(None)
        potential_flops.node_after_chance = is_max_turn1

        fold1_2 = Node(Node.node_l(self.players[0]))
        play1_2 = Node(Node.node_r(self.players[0]))
        is_max_turn1.r_edge = play1_2
        is_max_turn1.l_edge = fold1_2

        fold2_2 = Node(Node.node_l(self.players[1]))
        play2_2 = Node(Node.node_r(self.players[1]))
        play1_2.r_edge = play2_2
        play1_2.l_edge = fold2_2

        potential_turns = Node(len(list(combinations(poker_class.deck, 2))))
        play1_2.chance_node = potential_turns
        is_max_turn2 = Node(None)
        potential_turns.node_after_chance = is_max_turn2

        fold1_3 = Node(Node.node_l(self.players[0]))
        play1_3 = Node(Node.node_r(self.players[0]))
        is_max_turn2.r_edge = play1_3
        is_max_turn2.l_edge = fold1_3

        fold2_3 = Node(Node.node_l(self.players[1]))
        play2_3 = Node(Node.node_r(self.players[1]))
        play1_3.r_edge = play2_3
        play1_3.l_edge = fold2_3

        potential_river = Node(len(list(combinations(poker_class.deck, 1))))
        play2_3.chance_node = potential_river
        is_max_turn3 = Node(None)
        potential_river.node_after_chance = is_max_turn3

        fold1_4 = Node(Node.node_l(self.players[0]))
        play1_4 = Node(Node.node_r(self.players[0]))
        is_max_turn3.r_edge = play1_4
        is_max_turn3.l_edge = fold1_4

        fold2_4 = Node(Node.node_l(self.players[1]))
        play2_4 = Node(Node.node_r(self.players[1]))
        play1_4.r_edge = play2_4
        play1_4.l_edge = fold2_4

def expectiminimax(node):
    if node.l_edge is None and node.r_edge is None \
            and node.chance_node is None and node.node_after_chance is not None:
        return node.value

    fold = node.l_edge
    play = node.r_edge

    if fold > play:
        return Move("fold", fold)

    else:
        return Move("play", play)

def potOdd():
    return poker_class.current_bet / (poker_class.pot + poker_class.current_bet)


if __name__ == "__main__":
    poker_class = poker.Poker()
    game_tree = Tree(["Rico", "Luffy"])
