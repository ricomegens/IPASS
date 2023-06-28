from application import poker_simulation
from application import hand_simulation


def simulation():
    """
        Function that starts a graphical user interface of a poker game
    """
    screen = poker_simulation.GUI()
    screen.run()

def information():
    """
        Function that starts a graphical userface to calculate strength of hand
    """
    screen = hand_simulation.GUI()
    screen.run()

if __name__ == "__main__":
    # here you can decide what to run, information or simulation
    information()
    # simulation()