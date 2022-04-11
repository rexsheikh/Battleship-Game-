
from player import Player
import time 

class Game():
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
 

    def test(self):
        print(self.player1.board)
        print(self.player2.board)

    def run_game(self): 
        self.welcome_message()
        self.player1.game_board.display_board()
        print("Player 1, place your craft!")
        self.player1.place_craft()
        print("Player 2, place your craft!")
        self.player2.place_craft()
        self.player1_fleet_health = self.player1.fleet_health(self.player1.fleet)
        self.player2_fleet_health = self.player2.fleet_health(self.player2.fleet)
        while(self.player1_fleet_health > 0 and self.player2_fleet_health > 0):
            self.player2.attack(self.player1.game_board.board,self.player1.fleet)
            self.player1.attack(self.player2.game_board.board,self.player2.fleet)
        if self.player1_fleet_health ==  0:
            print("Player 2 wins!")
        else:
            print("Player 1 wins!")

    def welcome_message(self):
        print("*********** WELCOME TO BATTLESHIP ***********")
        # time.sleep(1)
        print("INSTRUCTIONS: enter coordinates according to the board map separated by a slash")
        # time.sleep(2)
        print("Example: aA/aB for destroyer (length 2)\nbA/bC for submarine (length 3) and so on")
        # time.sleep(2)
        print("Elements in the fleet cannot overlap and they cannot be placed diagonally")
        # time.sleep(3)
        print("you will see your board in detail but will only see hits and misses for your opponent's board.")
        # time.sleep(3)
    









