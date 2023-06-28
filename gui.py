import customtkinter
import algorithm
import evaluate
import poker
import player


class GUI():
    def __init__(self):
        self.players()
        self.game = poker.Poker()

        self.window = customtkinter.CTk()
        self.window.title("Poker simulation")
        self.window.geometry("600x400")
        customtkinter.set_appearance_mode("light")

        self.opp_hand()
        self.hand()
        self.phases = [self.pre_flop,self.move_player1, self.move_player2, self.flop, self.move_player1, self.move_player2 , self.turn, self.move_player1, self.move_player2, self.river, self.move_player1, self.move_player2, self.evaluate_win]
        self.index = 0
        self.button()
        self.tip_window()
        self.comm_cards()
        self.winner()
        self.own_move()
        self.opponent_move()

    def button(self):
        self.button = customtkinter.CTkButton(self.window, text="Next", command=self.next_phase)
        self.button.pack(pady=10)

    def next_phase(self):
        self.phases[self.index]()
        self.index = (self.index + 1) % len(self.phases)

    def players(self):
        self.player1 = player.Player("Rico")
        self.player2 = player.Player("Luffy")

    def deal_hand(self):
        self.game.deal_hand()
        text = "My hand\n"
        for card in self.player1.hand:
            text += card.suit + card.value + "\n"
        self.hand_player1.configure(text=text)
        self.hand_player2.configure(text="Opponent hand\n??\n??")

    def hand(self):
        self.hand_player1 = customtkinter.CTkLabel(self.window, text="My hand\n", text_color="black")
        self.hand_player1.place(x=30,y=210)

    def opp_hand(self):
        self.hand_player2 = customtkinter.CTkLabel(self.window, text="Opponent hand\n", text_color="black")
        self.hand_player2.place(x=490, y=210)

    def pre_flop(self):
        self.win.configure(text="")
        self.opp_choice_made.configure(text="")
        self.choice_made.configure(text="")
        self.game.add_player(self.player1)
        self.game.add_player(self.player2)
        self.game.reset_hand()
        self.game.reset_comm_cards()
        self.hand_player1.configure(text="My hand\n")
        self.hand_player2.configure(text="Opponent hand\n")
        self.choice_made.configure(text="")
        self.comm.configure(text="")
        self.game.create_deck()
        self.deal_hand()
        self.tips()


    def comm_cards(self):
        self.frame = customtkinter.CTkFrame(self.window, width=360, height=100, fg_color="green", border_color="black", border_width=5)
        self.frame.pack(pady=20)
        self.info = customtkinter.CTkLabel(self.frame, text="Community cards", bg_color="green", text_color="black")
        self.info.place(x=120,y=10)
        self.comm = customtkinter.CTkLabel(self.frame, text="", bg_color="green", text_color="black")
        self.comm.place(x=120, y=50)

    def flop(self):
        self.game.deal_comm_cards(3)
        text = ""
        for card in self.game.comm_cards:
            text += card.suit + card.value + "   "
        self.comm.configure(text=text)
        self.opp_choice_made.configure(text="")
        self.choice_made.configure(text="")
        self.tips()

    def turn(self):
        self.game.deal_comm_cards(1)
        text = ""
        for card in self.game.comm_cards:
            text += card.suit + card.value + "   "
        self.comm.configure(text=text)
        self.opp_choice_made.configure(text="")
        self.choice_made.configure(text="")
        self.tips()

    def river(self):
        self.game.deal_comm_cards(1)
        text = ""
        for card in self.game.comm_cards:
            text += card.suit + card.value + "   "
        self.comm.configure(text=text)
        self.opp_choice_made.configure(text="")
        self.choice_made.configure(text="")
        self.tips()

    def tip_window(self):
        self.tip_frame = customtkinter.CTkFrame(self.window,width=450, height=100, fg_color="white", border_color="black", border_width=5)
        self.tip_frame.pack()
        self.tip = customtkinter.CTkLabel(self.tip_frame, text="")
        self.odd = customtkinter.CTkLabel(self.tip_frame, text="")
        self.move = customtkinter.CTkLabel(self.tip_frame, text="")
        self.tip.place(x=30, y=10)
        self.odd.place(x=30, y=30)
        self.move.place(x=30, y=50)

    def tips(self):
        alg = algorithm.expectiminimax(self.player1.hand, self.game.comm_cards, self.game.deck)
        ahead = alg[2]
        tied = alg[3]
        odds = alg[1]
        behind = alg[3]
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

    def own_move(self):
        self.choice = customtkinter.CTkLabel(self.window, text="Move you made:")
        self.choice.place(x=100, y=300)
        self.choice_made = customtkinter.CTkLabel(self.window, text="")
        self.choice_made.place(x=130, y=320)

    def opponent_move(self):
        self.opp_choice = customtkinter.CTkLabel(self.window, text="Move opponent made:")
        self.opp_choice.place(x=400, y=300)
        self.opp_choice_made = customtkinter.CTkLabel(self.window, text="")
        self.opp_choice_made.place(x=435, y=320)

    def move_player1(self):
        correct_move = algorithm.expectiminimax(self.player1.hand, self.game.comm_cards, self.game.deck)[0]
        self.game.move(self.player1, correct_move)
        self.choice_made.configure(text=correct_move)
        if correct_move == "fold":
            self.win.configure(text="Player 1 folded!\nWinner\n"+self.player2.name)
            self.index=-1

    def move_player2(self):
        correct_move = algorithm.expectiminimax(self.player2.hand, self.game.comm_cards, self.game.deck)[0]
        self.game.move(self.player2, correct_move)
        self.opp_choice_made.configure(text=correct_move)
        if correct_move == "fold":
            self.win.configure(text="Player 2 folded!\nWinner\n"+self.player1.name)
            self.index=-1

    def winner(self):
        self.win = customtkinter.CTkLabel(self.window, text="", text_color="black")
        self.win.pack()

    def evaluate_win(self):
        winner = evaluate.game_evaluate(self.game.players, self.game.comm_cards)
        self.win.configure(text="Winner\n" + winner.name)
        self.index = -1

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    screen = GUI()
    screen.run()