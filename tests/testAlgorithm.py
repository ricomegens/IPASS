import unittest
from classes import cards


class TestAlgorithm(unittest.TestCase):
    def testHandStrength(self):
        deck = cards.deck()
        hand = [deck[5], deck[40]]
        comm_cards = [deck[20], deck[13], deck[15], deck[30], deck[1]]
        self.assertEqual(algorithm.hand_strength(hand, comm_cards, deck), (0.5494949494949495, 513, 62, 415))
    def testEffectiveHandStrength3(self):
        deck = cards.deck()
        hand = [deck[5], deck[40]]
        comm_cards = [deck[20], deck[13], deck[15]]
        self.assertEqual(algorithm.effective_hand_strength(hand, comm_cards, deck), (0.2899262652442087, 310, 9, 762))
    def testEffectiveHandStrength4(self):
        deck = cards.deck()
        hand = [deck[5], deck[40]]
        comm_cards = [deck[20], deck[13], deck[15], deck[45]]
        self.assertEqual(algorithm.effective_hand_strength(hand, comm_cards, deck), (0.3439957568199085, 353, 9, 673))
    def testFoldExpectiMiniMax3(self):
        deck = cards.deck()
        hand = [deck[5], deck[40]]
        comm_cards = [deck[20], deck[13], deck[15]]
        self.assertEqual(algorithm.expectiminimax(hand, comm_cards, deck), "fold")
    def testFoldExpectiMiniMax4(self):
        deck = cards.deck()
        hand = [deck[5], deck[40]]
        comm_cards = [deck[20], deck[13], deck[15], deck[45]]
        self.assertEqual(algorithm.expectiminimax(hand, comm_cards, deck), "fold")
    def testFoldExpectiMiniMax5(self):
        deck = cards.deck()
        hand = [deck[5], deck[40]]
        comm_cards = [deck[20], deck[13], deck[15], deck[45], deck[50]]
        self.assertEqual(algorithm.expectiminimax(hand, comm_cards, deck), "fold")
    def testCheckExpectiMiniMax3(self):
        deck = cards.deck()
        hand = [deck[5], deck[22]]
        comm_cards = [deck[20], deck[21], deck[15]]
        self.assertEqual(algorithm.expectiminimax(hand, comm_cards, deck), "check")
    def testCheckExpectiMiniMax4(self):
        deck = cards.deck()
        hand = [deck[5], deck[22]]
        comm_cards = [deck[20], deck[21], deck[15], deck[45]]
        self.assertEqual(algorithm.expectiminimax(hand, comm_cards, deck), "check")
    def testCheckExpectiMiniMax(self):
        deck = cards.deck()
        hand = [deck[5], deck[22]]
        comm_cards = [deck[20], deck[21], deck[15], deck[1]]
        self.assertEqual(algorithm.expectiminimax(hand, comm_cards, deck), "check")
    def testRaiseExpectiMiniMax3(self):
        deck = cards.deck()
        hand = [deck[37], deck[38]]
        comm_cards = [deck[20], deck[21], deck[17]]
        self.assertEqual(algorithm.expectiminimax(hand, comm_cards, deck), "raise")
    def testRaiseExpectiMiniMax4(self):
        deck = cards.deck()
        hand = [deck[37], deck[38]]
        comm_cards = [deck[20], deck[21], deck[17], deck[39]]
        self.assertEqual(algorithm.expectiminimax(hand, comm_cards, deck), "raise")
    def testRaiseExpectiMiniMax5(self):
        deck = cards.deck()
        hand = [deck[37], deck[38]]
        comm_cards = [deck[51], deck[21], deck[17], deck[39], deck[36]]
        self.assertEqual(algorithm.expectiminimax(hand, comm_cards, deck), "raise")

if __name__ == "__main__":
    unittest.main()