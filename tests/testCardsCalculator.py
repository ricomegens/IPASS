from algorithm import cardsCalculator
from classes import cards
import unittest

class TestCardsCalculator(unittest.TestCase):
    def testOppStarts(self):
        deck = cards.deck()
        hand = [deck[5], deck[22]]
        comm_cards = []
        self.assertEqual(len(cardsCalculator.opp_starts(hand, comm_cards, deck)), 1225)
    def testOppStartsCommCards3(self):
        deck = cards.deck()
        hand = [deck[5], deck[22]]
        comm_cards = [deck[20], deck[21], deck[15]]
        self.assertEqual(len(cardsCalculator.opp_starts(hand, comm_cards, deck)), 1081)
    def testOppStartsCommCards4(self):
        deck = cards.deck()
        hand = [deck[5], deck[22]]
        comm_cards = [deck[20], deck[21], deck[15], deck[6]]
        self.assertEqual(len(cardsCalculator.opp_starts(hand, comm_cards, deck)), 1035)
    def testOppStartsCommCards5(self):
        deck = cards.deck()
        hand = [deck[5], deck[22]]
        comm_cards = [deck[20], deck[21], deck[15], deck[6], deck[50]]
        self.assertEqual(len(cardsCalculator.opp_starts(hand, comm_cards, deck)), 990)
    def testPotentialTable(self):
        deck = cards.deck()
        hand = [deck[5], deck[22]]
        comm_cards = []
        opp_start = cardsCalculator.opp_starts(hand, comm_cards, deck)[0]
        self.assertEqual(len(cardsCalculator.potential_full_table(hand, opp_start, comm_cards, deck)), 1712304)
    def testPotentialTableCommCards3(self):
        deck = cards.deck()
        hand = [deck[5], deck[22]]
        comm_cards = [deck[20], deck[21], deck[15]]
        opp_start = cardsCalculator.opp_starts(hand, comm_cards, deck)[0]
        self.assertEqual(len(cardsCalculator.potential_full_table(hand, opp_start, comm_cards, deck)), 990)
    def testPotentialTableCommCards4(self):
        deck = cards.deck()
        hand = [deck[5], deck[22]]
        comm_cards = [deck[20], deck[21], deck[15], deck[6]]
        opp_start = cardsCalculator.opp_starts(hand, comm_cards, deck)[0]
        self.assertEqual(len(cardsCalculator.potential_full_table(hand, opp_start, comm_cards, deck)), 44)
    def testCardsLeft(self):
        deck = cards.deck()
        hand = [deck[5], deck[22]]
        comm_cards = []
        opp_start = cardsCalculator.opp_starts(hand, comm_cards, deck)[0]
        self.assertEqual(len(cardsCalculator.cards_left(hand, opp_start, comm_cards, deck)), 48)
    def testCardsLeftCommCards3(self):
        deck = cards.deck()
        hand = [deck[5], deck[22]]
        comm_cards = [deck[20], deck[21], deck[15]]
        opp_start = cardsCalculator.opp_starts(hand, comm_cards, deck)[0]
        self.assertEqual(len(cardsCalculator.cards_left(hand, opp_start, comm_cards, deck)), 45)
    def testCardsLeftCommCards4(self):
        deck = cards.deck()
        hand = [deck[5], deck[22]]
        comm_cards = [deck[20], deck[21], deck[15], deck[6]]
        opp_start = cardsCalculator.opp_starts(hand, comm_cards, deck)[0]
        self.assertEqual(len(cardsCalculator.cards_left(hand, opp_start, comm_cards, deck)), 44)
    def testCardsLeftCommCards4(self):
        deck = cards.deck()
        hand = [deck[5], deck[22]]
        comm_cards = [deck[20], deck[21], deck[15], deck[6], deck[1]]
        opp_start = cardsCalculator.opp_starts(hand, comm_cards, deck)[0]
        self.assertEqual(len(cardsCalculator.cards_left(hand, opp_start, comm_cards, deck)), 43)

if __name__ == "__main__":
    unittest.main()