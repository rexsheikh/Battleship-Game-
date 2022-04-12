
from player import Player
import time 
from os import system,name

class Game():
    def __init__(self):
        self.player1 = Player("player 1")
        self.player2 = Player("player 2")

    def run_game(self): 
        # self.welcome_message()
        # self.clear_board()
        self.player1.place_craft()
        # time.sleep(3)
        # self.clear_board()
        self.player2.place_craft()
        # time.sleep(3)
        # self.clear_board()

        self.player1_fleet_health = self.player1.fleet_health(self.player1.fleet)
        print(f"Player 1 fleet health {self.player1_fleet_health}")
        self.player2_fleet_health = self.player2.fleet_health(self.player2.fleet)
        print(f"Player 2 fleet health {self.player2_fleet_health}")
        while(self.player1_fleet_health > 0 and self.player2_fleet_health > 0):
            print(f"***** {self.player1.name}'s turn *****")
            self.player1.attack_board.display_board()
            self.player1.game_board.display_board()
            self.player1.display_fleet_health(self.player1.fleet)
            self.player1.attack(self.player2.game_board.board,self.player2.fleet)

            print(f"***** {self.player2.name}'s turn *****")
            self.player2.attack_board.display_board()
            self.player2.game_board.display_board()
            self.player2.display_fleet_health(self.player2.fleet)
            self.player2.attack(self.player1.game_board.board,self.player2.fleet)



        if self.player1_fleet_health ==  0:
            print("Player 2 wins!")
        else:
            print("Player 1 wins!")

    def welcome_message(self):
        print("*********** WELCOME TO BATTLESHIP ***********")
        # time.sleep(1)
        print("INSTRUCTIONS: The game board will show the player's own fleet as they have placed it on the board\nalong with any damaage sustained to elements in the fleet.")
        # time.sleep(2)
        print("Enter coordinates according to the board map. Example: aA/aB for destroyer (length 2)\nbA/bC for submarine (length 3) and so on")
        # time.sleep(2)
        print("When placing elements, ensure that they do not overlap with other elements in the fleet and they are placed either horizontally or vertically, not diagonally.")
        # time.sleep(3)
 
    def clear_board(self):
        _ = system('clear')
        
    




 




