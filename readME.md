# About the project
This project was realised by Rico Megens.

# File structure
In the directory tests you will find some tests for the classes that are necessary to run a game of poker. These classes can be found
in their corresponding file. In gui.py I realised the application, which is run in main.py. In evaluate.py I made functions for ranking
player's their hand. The file cards_calculator.py contains various functions to calculate which cards are still in play or what
combination of cards the opponent may have.

# Application
The project application can be run by running main.py. Here you can run the simulation step from step and start or reset a new game after.

# Algorithm
The application works based on an algorithm called expectiminimax. In this algorithm we have 2 players taking turns playing
against one another. These players are called MAX and MIN. In these turns there is some factor of randomness involved. To 
apply this algorithm in my application I have to calculate all the other possible opponent's hands and if so consider the future
board cares to come. This is where the randomness comes into play.

# Running the project
In order to run this project, first install all the packages. To do this run pip install requirements in your command line.
If you wish to create your own simulation alter the main, otherwise run my made simulation made in main.py.