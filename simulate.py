# monte carlo simulation
# https://petrosdemetrakopoulos.medium.com/estimating-the-outcome-of-a-texas-holdem-game-using-monte-carlo-simulation-1be35be29036
import poker
import algorithm
import player
import customtkinter


class GUI:
    def __init__(self):
        self.window = customtkinter.CTk()
        self.window.title = "Poker simulation"
        self.window.geometry("600x400")

        # button
        self.start = customtkinter.CTkButton(master=self.window, text="Start simulation", command=self.simulate())
        self.start.place(x=420, y=30)

        self.own_cards = customtkinter.CTkLabel(self.window, text=self.own_hand())
        self.own_cards.place(x=280, y=330)
        self.comm_cards = customtkinter.CTkLabel(self.window, text=self.comm_cards())
        self.comm_cards.place(x=230, y=200)

    def run(self):
        self.window.mainloop()

    def simulate(self):
        player1 = player.Player("Rico")
        player2 = player.Player("Luffy")
        game = poker.Poker([player1, player2])

    def own_hand(self):
        text = ""
        for card in player1.hand:
            text += card.suit + card.value + "   "
        return text

    def comm_cards(self):
        text = ""
        for card in game.comm_cards:
            text += card.suit + card.value + "   "
        return text
    #
    # def chance_of_win(self, node):
    #     return node.r_edge
    #
    # def chance_of_fold(self, node):
    #     return node.l_edge
    #
    # def amount_better_hands(self):
    #     return
    #
    # def amount_worse_hands(self):
    #     return
    #
    # def amount_tie_hands(self):
    #     return
    #
    # def best_own_hand(self):
    #     return


if __name__ == "__main__":
    player1 = player.Player("Rico")
    player2 = player.Player("Luffy")
    game = poker.Poker([player1, player2])
    GUI().run()
