import customtkinter
import algorithm
import algorithm_preflop
import evaluate
import player
import poker


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
        customtkinter.set_appearance_mode("red")

        self.button()
        self.hand()
        self.opp_hand()
        self.tip_window()
        self.comm_cards()
        self.winner()

    def button(self):
        self.phases = self.reset().copy()
        self.button = customtkinter.CTkButton(self.window, text="Next", command=self.update)
        self.button.pack(pady=10)

    def comm_cards(self):
        self.frame = customtkinter.CTkFrame(self.window, width=360, height=100, fg_color="green", border_color="black", border_width=5)
        self.frame.pack(pady=20)
        self.info = customtkinter.CTkLabel(self.frame, text="Community cards", bg_color="green", text_color="black")
        self.info.place(x=120,y=10)
        self.comm = customtkinter.CTkLabel(self.frame, text="", bg_color="green", text_color="black")
        self.comm.place(x=120, y=50)


    def update(self):
        if len(self.phases) == 0:
            self.reset()
        elif len(self.phases) == 1:
            self.win.configure(text="Winner: " + self.phases.pop(0)(self.game.players, self.game.comm_cards).name)
        else:
            self.comm.configure(text=self.phases.pop(0)()[0])

    def hand(self):
        text = ""
        for card in self.player1.hand:
            text += card.suit + card.value + "\n"
        self.hand_player1 = customtkinter.CTkLabel(self.window, text="My hand\n" + text, text_color="black")
        self.hand_player1.place(x=30,y=210)

    def opp_hand(self):
        self.hand_player2 = customtkinter.CTkLabel(self.window, text="Opponent hand\n?\n?", text_color="black")
        self.hand_player2.place(x=490, y=210)
    def pre_flop(self):
        alg_player1 = algorithm.Expectiminimax(self.player1, self.game.comm_cards)
        player1_move = alg_player1.expectiminimax()
        odds = alg_player1.ehs[0]
        ahead = alg_player1.ehs[1]
        tied = alg_player1.ehs[2]
        behind = alg_player1.ehs[3]
        self.game.move(self.player1, player1_move)
        self.game.move(self.player2, algorithm.Expectiminimax(self.player2, self.game.comm_cards).expectiminimax())
        return self.tips(odds, ahead, tied, behind)

    def flop(self):
        self.game.deal_comm_cards(3)
        alg_player1 = algorithm.Expectiminimax(self.player1, self.game.comm_cards)
        player1_move = alg_player1.expectiminimax()
        odds = alg_player1.ehs[0]
        ahead = alg_player1.ehs[1]
        tied = alg_player1.ehs[2]
        behind = alg_player1.ehs[3]
        self.game.move(self.player1, player1_move)
        self.game.move(self.player2, algorithm.Expectiminimax(self.player2, self.game.comm_cards).expectiminimax())
        text = ""
        for card in self.game.comm_cards:
            text += card.suit + card.value + "   "
        return text, self.tips(odds, ahead, tied, behind)

    def turn(self):
        self.game.deal_comm_cards(1)
        alg_player1 = algorithm.Expectiminimax(self.player1, self.game.comm_cards)
        player1_move = alg_player1.expectiminimax()
        odds = alg_player1.ehs[0]
        ahead = alg_player1.ehs[1]
        tied = alg_player1.ehs[2]
        behind = alg_player1.ehs[3]
        player2_move = algorithm.Expectiminimax(self.player2, self.game.comm_cards).expectiminimax()
        text = ""
        for card in self.game.comm_cards:
            text += card.suit + card.value + "   "
        return text, self.tips(odds, ahead, tied, behind)

    def river(self):
        self.game.deal_comm_cards(1)
        alg_player1 = algorithm.Expectiminimax(self.player1, self.game.comm_cards)
        player1_move = alg_player1.expectiminimax()
        odds = alg_player1.hs[0]
        ahead = alg_player1.hs[1]
        tied = alg_player1.hs[2]
        behind = alg_player1.hs[3]
        player2_move = algorithm.Expectiminimax(self.player2, self.game.comm_cards).expectiminimax()
        text = ""
        for card in self.game.comm_cards:
            text += card.suit + card.value + "   "
        return text, self.tips(odds, ahead, tied, behind)

    def tip_window(self):
        self.tip_frame = customtkinter.CTkFrame(self.window,width=450, height=100, fg_color="white", border_color="black", border_width=5)
        self.tip_frame.pack()
        self.tip = customtkinter.CTkLabel(self.tip_frame, text="")
        self.odd = customtkinter.CTkLabel(self.tip_frame, text="")
        self.move = customtkinter.CTkLabel(self.tip_frame, text="")
        self.tip.place(x=30, y=10)
        self.odd.place(x=30, y=30)
        self.move.place(x=30, y=50)

    def tips(self, odds, ahead, tied, behind):
        tip = f"Your current hand beats {ahead} hands, ties with {tied}, loses to {behind}"
        chance = f"This makes your effective hand strength {odds}"
        if odds > 0.8:
            move = f"You stand very strong, adviced to raise"
        elif odds > 0.5:
            move = f"You stand stronger than your opponent, adviced to play"
        else:
            pot_odd = self.game.current_bet / (self.game.pot + self.game.current_bet)
            move = f"Unwise to play as you stand weaker than your opponent," \
                   f" but if\n hand strength is higher" \
                   f" than pot odd: {pot_odd:.2f} , you could play"
        self.tip.configure(text=tip)
        self.odd.configure(text=chance)
        self.move.configure(text=move)


    def winner(self):
        self.win = customtkinter.CTkLabel(self.window, text="", text_color="black")
        self.win.pack()

    def reset(self):
        return [self.pre_flop, self.flop, self.turn, self.river, evaluate.game_evaluate]

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    screen = GUI()
    screen.run()