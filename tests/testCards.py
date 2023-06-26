from cards import Card
import unittest

class TestCards:
    def testSuit(self):
        card1 = Card("s", "a", 14)
        self.assertEqual(card1.suit, f"s")
    def testValue(self):
        card1 = Card("s", "a", 14)
        self.assertEqual(card1.value, f"a")
    def testRanking(self):
        card1 = Card("s", "a", 14)
        self.assertEqual(card1.ranking, f"{14}")


if __name__ == "__main__":
    unittest.main()