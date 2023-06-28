import customtkinter
from algorithm import expectiminimax
from classes import cards

class GUI:
    def __init__(self):
        self.window = customtkinter.CTk()
        self.window = customtkinter.CTk()
        self.window.title("Cards known")
        self.window.geometry("400x250")

        self.hand()
        self.button()
        self.comm_cards()

    def button(self):
        """
            Function creates a button user can press if they want to submit their cards
        """
        self.submit = customtkinter.CTkButton(self.window, text="submit", command=self.get_cards)
        self.submit.place(x=120, y=200)

    def comm_cards(self):
        """
            Function that creates entries so player can put in the community cards, if any
            are known
        """
        self.comm_cards_info = customtkinter.CTkLabel(self.window, text="Submit community cards")
        self.comm_cards_info.place(x=130, y=90)
        self.comm_card1 = customtkinter.CTkEntry(self.window, width=50)
        self.comm_card2 = customtkinter.CTkEntry(self.window, width=50)
        self.comm_card1.place(x=50, y=140)
        self.comm_card2.place(x=110, y=140)
        self.comm_card3 = customtkinter.CTkEntry(self.window, width=50)
        self.comm_card4 = customtkinter.CTkEntry(self.window, width=50)
        self.comm_card3.place(x=170, y=140)
        self.comm_card4.place(x=230, y=140)
        self.comm_card5 = customtkinter.CTkEntry(self.window, width=50)
        self.comm_card5.place(x=290, y=140)

    def hand(self):
        """
            Function that entry boxes so player can put in their hands with label
            as example how to do it.
        """
        self.info = customtkinter.CTkLabel(self.window, text="If your card was hearts jack, type hJ\n"
                                                             "If your card was diamonds 5, type d5")
        self.info.pack()
        self.hand_info = customtkinter.CTkLabel(self.window, text="Submit hand")
        self.hand_info.pack()
        self.hand_card1 = customtkinter.CTkEntry(self.window, width=80)
        self.hand_card2 = customtkinter.CTkEntry(self.window, width=80)
        self.hand_card1.place(x=200,y=60)
        self.hand_card2.place(x=110, y=60)

    def get_cards(self):
        """
            Function that gets info from the user, converts this to a member of class
            Card and then calculates the strength of hand to start it in another window.
            Also catches error for not correctly putting in player's hand.
        """
        hand1 = self.hand_card1.get()
        hand2 = self.hand_card2.get()
        comm1 = self.comm_card1.get()
        comm2 = self.comm_card2.get()
        comm3 = self.comm_card3.get()
        comm4 = self.comm_card4.get()
        comm5 = self.comm_card5.get()
        hand = [hand1, hand2]
        actual_hand = []
        comm_cards = [comm1, comm2, comm3, comm4, comm5]
        actual_comm_cards = []
        deck = cards.deck()
        # compare imput to a member of class attribute, if same add the member to a list
        for card in deck:
            for phoney_card in hand:
                if card.suit == phoney_card[0] and card.value == phoney_card[1:]:
                    actual_hand.append(card)
            for phoney_comm_card in comm_cards:
                # community cards can be empty so check if there is an actual input first
                if len(phoney_comm_card) >= 2:
                    if card.suit == phoney_comm_card[0] and card.value == phoney_comm_card[1:]:
                        actual_comm_cards.append(card)
        # if no actual hand was given, return an error
        if len(actual_hand) != 2:
            self.window.destroy()
            self.new_window = customtkinter.CTk()
            self.new_window.title("Error")
            self.error = customtkinter.CTkLabel(self.new_window, text="Wrong input")
            self.error.pack()
            self.new_window.mainloop()
            return
        info = expectiminimax.expectiminimax(actual_hand, actual_comm_cards, deck)
        self.ranking(info)

    def ranking(self, info):
        """
            Function that deletes old userface and creates a new one with
            information of the strength of user's hand
        """
        self.window.destroy()
        self.rank = customtkinter.CTk()
        self.rank.title("Hand Ranking")
        self.rank.geometry("400x150")
        move = info[0]
        chance = info[1]
        ahead = info[2]
        tied = info[3]
        behind = info[4]
        self.move = customtkinter.CTkLabel(self.rank, text=f"The move you should make: {move}")
        self.move.pack()
        self.chance = customtkinter.CTkLabel(self.rank, text=f"Your odds from 0-1: {chance}")
        self.chance.pack()
        self.ahead = customtkinter.CTkLabel(self.rank, text=f"The amount of hands your ahead: {ahead}")
        self.ahead.pack()
        self.tied = customtkinter.CTkLabel(self.rank, text=f"The amount of hands your tied with: {tied}")
        self.tied.pack()
        self.behind = customtkinter.CTkLabel(self.rank, text=f"The amount of hands your behind: {behind}")
        self.behind.pack()
        self.rank.mainloop()

    def run(self):
        """
            Function meant for running GUI.
        """
        self.window.mainloop()