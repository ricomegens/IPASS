from player import Player
from cards import Card
import unittest

class TestPlayer:
    def testMoney(self):
        player1 = Player("Rico")
        self.assertEqual(player1.money == 0)
    def testName(self):
        player1 = Player("Rico")
        self.assertEqual(player1.name == "Rico")
    def testUpdateMoney(self):
        player1 = Player("Rico")
        player1.update_money(20)
        self.assertEqual(player1.money == 20)
    def testUpdateHand(self):
        player1 = Player("Rico")
        card1 = Card("s", "A", 14)
        player1.update_hand(card1)
        self.assertEqual(player1.hand == [card1])
    def testClearHand(self):
        player1 = Player("Rico")
        card1 = Card("s", "A", 14)
        player1.update_hand(card1)
        self.assertEqual(player1.hand == [card1])
        player1.reset_hand()
        self.assertEqual(player1.hand == [])

if __name__ == "__main__":
    unittest.main()