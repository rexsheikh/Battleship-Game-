
from player import Player
import time 
from os import system,name

class Game():
    def __init__(self):
        self.player1 = Player("player 1")
        self.player2 = Player("player 2")

    def run_game(self): 
        self.begin = self.welcome_message()
        if self.begin != 'yes':
            self.welcome_message()
        self.clear_board()
        self.player1.place_craft()
        self.player1.game_board.display_board()
        time.sleep(3)
        self.clear_board()
        self.player2.place_craft()
        self.player2.game_board.display_board()
        time.sleep(3)
        self.clear_board()

        while(True):
            print(f"***** {self.player1.name}'s turn *****")
            self.player1.attack_board.display_board()
            self.player1.game_board.display_board()
            self.player1.display_fleet_health(self.player1.fleet)
            self.player1.attack(self.player2.game_board.board,self.player2.fleet,self.player2)
            self.player1.sunken_craft_alert(self.player2.fleet)

            if self.player2.fleet_health(self.player2.fleet) == 0:
                print("PLAYER 1 WINS!\n")
                print("Final Attack Board")
                self.player1.attack_board.display_board()
                break
            else:
                time.sleep(2.5)
                self.clear_board

            print(f"***** {self.player2.name}'s turn *****")
            self.player2.attack_board.display_board()
            self.player2.game_board.display_board()
            self.player2.display_fleet_health(self.player2.fleet)
            self.player2.attack(self.player1.game_board.board,self.player1.fleet,self.player1)
            self.player2.sunken_craft_alert(self.player1.fleet)
            time.sleep(2.5)
            self.clear_board()
            if self.player1.fleet_health(self.player1.fleet) == 0:
                print("PLAYER 1 WINS!\n")
                print("Final Attack Board")
                self.player1.attack_board.display_board()
            else:
                time.sleep(2.5)
                self.clear_board

        print('THANK YOU FOR PLAYING')

    def welcome_message(self):
        print('\n')
        print("*********** WELCOME TO BATTLESHIP ***********")
        print("INSTRUCTIONS: The Game Board shows the player's fleet.\nThe Attack Board shows the opponent's with your attempted attacks.\n")
        print("Enter coordinates according to the board map with start and end separated by any character.\nExample: aA/aB (destroyer, length 2)\n")
        print("When placing elements, ensure that they do not overlap with other elements in the fleet and\nthey are placed either horizontally or vertically, not diagonally.")
        self.acknowledge = input("enter yes to acknowledge and begin the game: ").lower()
        return self.acknowledge
 

    def clear_board(self):
        _ = system('clear')

        
    




 




