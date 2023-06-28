from classes.cards import Card
from classes.player import Player
from algorithm import evaluate
import unittest

class TestEvaluate(unittest.TestCase):
    def testRoyalFlush(self):
        suits = ["s", "s", "s", "s", "s"]
        values = [14,13,12,11,10]
        self.assertEqual(evaluate.royal_flush(suits, values), True)
    def testNotRoyalFlush(self):
        suits = ["s", "s", "d", "s", "s"]
        values = [14, 13, 12, 11, 10]
        self.assertEqual(evaluate.royal_flush(suits, values), False)
    def testStraightFlush(self):
        suits = ["s", "s", "s", "s", "s"]
        values = [12, 13, 9, 11, 10]
        self.assertEqual(evaluate.straight_flush(suits, values), True)
    def testNotStraightFlush(self):
        suits = ["s", "d", "s", "s", "s"]
        values = [12, 13, 9, 11, 10]
        self.assertEqual(evaluate.straight_flush(suits, values), False)
    def testFourOfAKind(self):
        values = [2,2,2,2,8]
        self.assertEqual(evaluate.four_of_a_kind(values), True)
    def testNotFourOfAKind(self):
        values = [14, 13, 12, 11, 10]
        self.assertEqual(evaluate.four_of_a_kind(values), False)
    def testFullHouse(self):
        values = [3,3,3, 11, 11]
        self.assertEqual(evaluate.full_house(values), True)
    def testNotFullHouse(self):
        values = [3,3,3, 8, 11]
        self.assertEqual(evaluate.full_house(values), False)
    def testFlush(self):
        suits = ["s", "s", "s", "s", "s"]
        self.assertEqual(evaluate.flush(suits), True)
    def testNotFlush(self):
        suits = ["s", "s", "s", "s", "h"]
        self.assertEqual(evaluate.flush(suits), False)
    def testStraight(self):
        values = [12, 13, 9, 11, 10]
        self.assertEqual(evaluate.straight(values), True)
    def testNotStraight(self):
        values = [12, 3, 9, 11, 10]
        self.assertEqual(evaluate.straight(values), False)
    def testThreeOfAKind(self):
        values = ["A", "A", "A", "3", "7"]
        self.assertEqual(evaluate.three_of_a_kind(values), True)
    def testNotThreeOfAKind(self):
        values = ["A", "J", "A", "3", "7"]
        self.assertEqual(evaluate.three_of_a_kind(values), False)
    def testTwoPair(self):
        values = [12, 12, 11, 11, 9]
        self.assertEqual(evaluate.two_pair(values), True)
    def testNotTwoPair(self):
        values = [12, 12, 9, 11, 10]
        self.assertEqual(evaluate.two_pair(values), False)
    def testPair(self):
        values = [12, 12, "K", 11, 9]
        self.assertEqual(evaluate.pair(values), True)
    def testNotPair(self):
        values = ["2", "A", "8", "9", "Q"]
        self.assertEqual(evaluate.pair(values), False)
    def testRank(self):
        hand = [Card("d","7",7), Card("h","3", 3)]
        comm_cards = [Card("h","7",7), Card("s","3", 3), Card("c", "A", 14)]
        self.assertEqual(evaluate.rank(hand, comm_cards), (3, 20))
    def testGameEvaluate(self):
        player1 = Player("Rico")
        player2 = Player("Luffy")
        hand1 = [Card("d", "7", 7), Card("h", "3", 3)]
        for card in hand1:
            player1.update_hand(card)
        hand2 = [Card("c", "3", 3), Card("d", "3", 3)]
        for card in hand2:
            player2.update_hand(card)
        comm_cards = [Card("h", "7", 7), Card("s", "3", 3), Card("c", "A", 14)]
        self.assertEqual(evaluate.game_evaluate([player1, player2], comm_cards), player2)

if __name__ == "__main__":
    unittest.main()