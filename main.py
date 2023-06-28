import cards
import gui
import algorithm

def main():
    """
        Function that starts a graphical user interface of a poker game
    """
    screen = gui.GUI()
    screen.run()

def information(hand, comm_cards):
    """
        Function that returns information with how to move according to player hand and
        community cards.

        Args:
        hand (list): list of members of class Card that belong to own hand
        comm_cards (list): list of members of class Card that are community cards

        Returns:
        tuple: Returns tupple with first index chance, second hands that you are ahead,
        thirds hands you are tied to and third hands you lose to.
    """
    # check what cards are known and remove them from deck
    known_cards = hand + comm_cards
    deck = cards.deck()
    for known_card in known_cards:
        for card in deck:
            if known_card.suit == card.suit and known_card.value == card.value:
                deck.remove(card)
    # run algorithm
    return algorithm.expectiminimax(hand, comm_cards, deck)

if __name__ == "__main__":
    main()
