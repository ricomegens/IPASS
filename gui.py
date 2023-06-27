import customtkinter
import algorithm_preflop
import evaluate
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
        customtkinter.set_appearance_mode("dark")

        self.hand()
        self.comm_cards()

        self.phases = [self.flop, self.turn, self.river]
        self.play()


    def comm_cards(self):
        self.frame = customtkinter.CTkFrame(self.window, width=100, height=40, bg_color="green")
        self.frame.place(x=250, y=180)
        self.info = customtkinter.CTkLabel(self.frame, text="Community cards", bg_color="green")
        self.info.pack()
        self.comm = customtkinter.CTkLabel(self.frame, text="", bg_color="green")
        self.comm.pack()


    def update_comm_cards(self):
        if len(self.next) == 0:
            self.reset()
        elif len(self.next) == 1:
            self.win.configure(self.next.pop(0))
        else:
            self.comm.configure(text=self.next.pop(0))

    def hand(self):
        self.frame = customtkinter.CTkFrame(self.window, width=400, height=100, bg_color="red")
        self.frame.place(x=50, y=300)
        text = ""
        for card in self.player1.hand:
            text += card.suit + card.value + "   "
        self.hand_player1 = customtkinter.CTkLabel(self.frame, text="My hand\n" + text)
        self.hand_player1.pack()

    def tips_pre_flop(self):
        return
        # text = "There are 169 sort of beginning hands after substracting all starting hands from whether they are suited" \
        #        "or not as this does not yet matter"
        # alg = algorithm_preflop.rank()
        # if alg > 0.5:
        #     tip = f"you starting hand beats {alg} hands, more than half so it is wise to play"
        # else:
        #     tip = f"you starting hand beats {alg} hands, less than half so it is not wise to play"
        # return text, tip

    def flop(self):
        self.game.deal_comm_cards(3)
        text = ""
        for card in self.game.comm_cards:
            text += card.suit + card.value + "   "
        return text, self.tips()

    def turn(self):
        self.game.deal_comm_cards(1)
        text = ""
        for card in self.game.comm_cards:
            text += card.suit + card.value + "   "
        return text, self.tips()

    def river(self):
        self.game.deal_comm_cards(1)
        text = ""
        for card in self.game.comm_cards:
            text += card.suit + card.value + "   "
        return text, self.tips()

    def tips(self):
        alg = self.move()
        tip = f"Your current hand beats {alg[1]} hands, ties with {alg[2]}, loses to {alg[3]} in the future"
        chance = alg[0]
        odds = f"This makes your effective hand strength {chance}"
        if chance > 0.8:
            move = f"You stand very strong, adviced to raise"
        elif chance > 0.5:
            move = f"You stand stronger than your opponent, adviced to play"
        else:
            pot_odd = self.game.current_bet / (self.game.pot + self.game.current_bet)
            move = f"It is unwise to play as you stand weaker than your opponent, but if your chance {chance} is higher" \
                   f"than {pot_odd}, you could bluff"
        return tip, odds, move


    def winner(self):
        text = f"Winner\n{evaluate.game_evaluate(self.game.players, self.game.comm_cards).name}"
        return text

    def phase(self):
        function = self.current_phases.pop(0)
        print(function())
    def play(self):
        self.current_phases = self.phases.copy()
        self.button = customtkinter.CTkButton(self.window, text="Next", command=self.phase)
        self.button.pack()

    def move(self):
        return effective_hand_strength.EHS(self.player1.hand, self.game.comm_cards).effective_hand_strength()

    def reset(self):
        return

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    screen = GUI()
    screen.run()