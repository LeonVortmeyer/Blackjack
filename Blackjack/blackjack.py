#Leon Vortmeyer 10.31.2021

from Game import Game

#blackjack.py is the executable file to start and run a blackjack game from the terminal

if __name__ == "__main__":
    """The executable file for terminal blackjack."""

    #A game.start_game() method was defined in the Game module to allow users to give names to their human players,
    #and easily instantiate a game with some helpful prompting from the command line.
    

    #A game may also be started with the .__init__() (Game()) method, which defaults to 1 human player, 1 computer player,
    #and the dealer. But we recommend playing with Game.start_game()

    
    #newgame = Game.start_game()

    newgame = Game()
    newgame.play()

