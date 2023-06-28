from classes.poker import Poker
from classes.player import Player
import unittest

class TestPoker(unittest.TestCase):
    def testPot(self):
        game = Poker()
        self.assertEqual(game.pot, 0)
    def testUpdatePot(self):
        game = Poker()
        game.update_pot(20)
        self.assertEqual(game.pot, 20)
    def testResetPot(self):
        game = Poker()
        game.update_pot(20)
        self.assertEqual(game.pot, 20)
        game.reset_pot()
        self.assertEqual(game.pot, 0)
    def testPlayers(self):
        game = Poker()
        self.assertEqual(game.players, [])
    def testAddPlayer(self):
        game = Poker()
        player1 = Player("Rico")
        game.add_player(player1)
        self.assertEqual(game.players, [player1])
    def testRemovePlayer(self):
        game = Poker()
        player1 = Player("Rico")
        game.add_player(player1)
        self.assertEqual(game.players, [player1])
        game.remove_player(player1)
        self.assertEqual(game.players, [])
    def testDealHand(self):
        game = Poker()
        game.create_deck()
        player1 = Player("Rico")
        game.add_player(player1)
        game.deal_hand()
        self.assertEqual(len(player1.hand), 2)
    def testResetHand(self):
        game = Poker()
        game.create_deck()
        player1 = Player("Rico")
        game.add_player(player1)
        game.deal_hand()
        self.assertEqual(len(player1.hand), 2)
        game.reset_hand()
        self.assertEqual(len(player1.hand), 0)
    def testCommCards(self):
        game = Poker()
        self.assertEqual(game.comm_cards, [])
    def testDealCommCards(self):
        game = Poker()
        game.create_deck()
        game.deal_comm_cards(2)
        self.assertEqual(len(game.comm_cards), 2)
    def testResetCommCards(self):
        game = Poker()
        game.create_deck()
        game.deal_comm_cards(2)
        self.assertEqual(len(game.comm_cards), 2)
        game.reset_comm_cards()
        self.assertEqual(len(game.comm_cards), 0)
    def testCreateDeck(self):
        game = Poker()
        game.create_deck()
        self.assertEqual(len(game.deck), 52)