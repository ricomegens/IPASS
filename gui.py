import customtkinter

import algorithm_preflop
import player
import poker
import effective_hand_strength

class GUI():
    def __init__(self):
        self.player1 = player.Player("Rico")
        self.player2 = player.Player("Luffy")
        self.game = poker.Poker()
        self.game.add_player(self.player1)
        self.game.add_player(self.player2)
        self.game.create_deck()
        self.game.deal_hand()

        self.window = customtkinter.CTk()
        self.window.title = "Poker simulation"
        self.window.geometry("600x400")

        self.hand()
        self.next = [self.flop(), self.turn(), self.river()]
        self.comm_cards()


    def comm_cards(self):
        self.comm = customtkinter.CTkLabel(self.window, text="")
        self.comm.pack()

        self.next_phase = customtkinter.CTkButton(self.window, text="Next", command=self.update_comm_cards)
        self.next_phase.pack()

    def update_comm_cards(self):
        if self.next[0]:

        if len(self.next) == 0:
            self.evaluation()
        else:
            self.comm.configure(text=self.next.pop(0))

    def hand(self):
        text = ""
        for card in self.player1.hand:
            text += card.suit + card.value + "   "
        self.hand_player1 = customtkinter.CTkLabel(self.window, text=text)
        self.hand_player1.pack()

    def tips_pre_flop(self):
        text = "There are 169 srt of beginning hands after substracting all starting hands from wheter they are suited" \
               "or not as this does not yet matter"
        alg = algorithm_preflop.suit()
        if alg > 0.5:
            tip = f"you starting hand beats {alg} hands, more than half so it is wise to play"
        else:
            tip = f"you starting hand beats {alg} hands, less than half so it is not wise to play"
        return text, tip

    def flop(self):
        self.game.deal_comm_cards(3)
        text = ""
        for card in self.game.comm_cards:
            text += card.suit + card.value + "   "
        return text

    def tips_flop(self):
        text = "There are 169 srt of beginning hands after substracting all starting hands from wheter they are suited" \
               "or not as this does not yet matter"
        alg = algorithm_preflop.suit()
        if alg > 0.5:
            tip = f"you starting hand beats {alg} hands, more than half so it is wise to play"
        else:
            tip = f"you starting hand beats {alg} hands, less than half so it is not wise to play"
        return text, tip

    def turn(self):
        self.game.deal_comm_cards(1)
        text = ""
        for card in self.game.comm_cards:
            text += card.suit + card.value + "   "
        return text

    def tips_turn(self):
        text = "There are 169 srt of beginning hands after substracting all starting hands from wheter they are suited" \
               "or not as this does not yet matter"
        alg = algorithm_preflop.suit()
        if alg > 0.5:
            tip = f"you starting hand beats {alg} hands, more than half so it is wise to play"
        else:
            tip = f"you starting hand beats {alg} hands, less than half so it is not wise to play"
        return text, tip

    def river(self):
        self.game.deal_comm_cards(1)
        text = ""
        for card in self.game.comm_cards:
            text += card.suit + card.value + "   "
        return text

    def evaluation(self):
        if len(self.game.evaluation()) == 2:
            text = "tie"
        else:
            text = self.game.evaluation()
        a = customtkinter.CTkLabel(self.window, text=text)
        a.pack()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    screen = GUI()
    screen.run()