import poker
from player import Player
import unittest

class TestPoker(unittest.TestCase):
    def testPot(self):
        self.assertEqual(game.pot, 0)
    def testUpdatePot(self):
        game.update_pot(20)
        self.assertEqual(game.pot, 20)
    def testResetPot(self):
        game.update_pot(20)
        self.assertEqual(game.pot, 20)
        game.reset_pot()
        self.assertEqual(game.pot, 0)
    def testPlayers(self):
        self.assertEqual(game.players, [player1, player2])
    def testAddPlayer(self):
        player3 = Player("Test")
        game.add_player(player3)
        self.assertEqual(game.players, [player1, player2, player3])
    def testRemovePlayer(self):
        game.remove_player(player2)
        self.assertEqual(game.players, [player1])
    def testDealHand(self):
        game.deal_hand()
        self.assertEqual(len(player1.hand), 2)
    def testResetHand(self):
        game.deal_hand()
        self.assertEqual(len(player1.hand), 2)
        game.reset_hand()
        self.assertEqual(len(player1.hand), 0)
    def testCommCards(self):
        self.assertEqual(game.comm_cards, [])
    def testDealCommCards(self):
        game.deal_comm_cards(2)
        self.assertEqual(len(game.comm_cards), 2)
    def testResetCommCards(self):
        game.deal_comm_cards(2)
        self.assertEqual(len(game.comm_cards), 2)
        game.reset_comm_cards()
        self.assertEqual(len(game.comm_cards), 0)
    def testCreateDeck(self):
        game.create_deck()
        self.assertEqual(len(game.deck), 52)

if __name__ == "__main__":
    player1 = Player("Rico")
    player2 = Player("Luffy")
    game = poker.Poker([player1, player2])