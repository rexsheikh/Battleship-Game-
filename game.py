#the board is actually 40 by 40. with 0,2,4 (all evens) representing spaces. 
#each ship is itself a watercraft. build out the watercraft properties to include health 
# and placement functions 
    #for the placement functions : check for diagonals and non-overlapping
    #this could happen in the game logic potentially 

#to do
    #. player craft placement. resulting board print. 
    #. use ord() function to turn letters to numbers. 
        # uppercase letters minus 63 give proper board orientation
        # lowercase letters minus 97 give proper board orientation
    #. attack function for each player. 
    #. hit miss information to update individual player boards inside game logic 
    #. print overall craft destroyed for each player 


from player import Player

class Game():
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
 

    def run_game(self):
        pass

    def diag_check(self):
        pass

    def overlap_check(self):
        pass 








