import cards
import gui
import poker
import player

# in this main function you can simulate on what hand you have
def main():
    player1 = player.Player("Rico")
    player2 = player.Player("Luffy")
    game = poker.Poker([player1, player2])
    screen = gui.GUI(hand)
    screen.run()

if __name__ == "__main__":
    card1 = cards.Card("s", "8", 8)
    card2 = cards.Card("d", "q", 11)
    main([card1, card2])
