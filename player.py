from watercraft import Watercraft
from destroyer import Destroyer
from submarine import Submarine
from battleship import Battleship
from aircraft_carrier import Aircraft_carrier
from board import Board

class Player():
    def __init__(self):
        self.board = Board()
        self.destroyer = Destroyer(2,'destroyer')
        self.submarine = Submarine(3,'submarine')
        self.battleship = Battleship(4,'battleship alpha')
        self.battleship2 = Battleship(4,'battleship bravo')
        self.aircraft_carrier = Aircraft_carrier(5,'aircraft_carrier')
        self.fleet = [self.destroyer,self.submarine,self.battleship,self.battleship2,self.aircraft_carrier] 
        self.board_map = {
            'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,
            'n':13,'o':14,'p':15,'q':16,'r':17, 's':18,'t':19,
            'A':2,'B':4,'C':6,'D':8,'E':10,'F':12,'G':14,'H':16,'I':18,'J':20,'K':22,'L':24,'M':26,'N':28,'O':30,'P':32,
            'Q':34,'R':36,'S':38,'T':40
        }

    def place_craft(self):
        for craft in self.fleet:
            self.user_input= str(input(f"Enter start/end coordinates to place {craft.name} with length {craft.length}: "))
            self.coords = list(self.parse_input(self.user_input))
            self.length_check = self.check_length(self.coords,craft)
            self.orientation_check = self.check_orientation(self.coords)
            self.overlap_check = self.check_overlap(self.coords,self.orientation_check)
            if self.length_check and (self.orientation_check == 'vertical' or self.orientation_check == 'horizontal') and self.overlap_check:
                if self.orientation_check == 'horizontal': 
                    while self.coords[3] >= (self.coords[1] + 2):
                        self.board.board[self.coords[0]][self.coords[1]] = "&"
                        self.board.board[self.coords[2]][self.coords[3]] = "&"
                        self.coords[3] -= 2
                    self.board.display_board()
                elif self.orientation_check == 'vertical': 
                    while self.coords[2] >= self.coords[0]:
                        self.board.board[self.coords[0]][self.coords[1]] = "&"
                        self.board.board[self.coords[2]][self.coords[3]] = "&"
                        self.coords[2] -= 1 
                    self.board.display_board()
            else:
                # while self.length_check or (self.check_orientation == 'vertical' or self.check_orientation == 'horizontal') or self.overlap_check:
                #     self.place_craft(craft)
                pass
            


    def check_length(self,coords,craft):
        if coords[0] == coords[2] and coords[3]/coords[1] != craft.length:  
            print('please enter coordinates of the correct length')
            return False 
        elif coords[1] == coords[3] and (coords[0] + coords[2] + 1) != craft.length:
            print('please enter coordinates of the correct length')
            return False
        else:
            return True 
            


    def check_overlap(self,coords,orientation):
        self.overlap_coords = coords.copy()
        if orientation == "horizontal":
            while self.overlap_coords[2] >= self.overlap_coords[0]:
                if self.board.board[self.overlap_coords[0]][self.overlap_coords[2]] == "&":
                    print('overlap')
                    return False
                self.overlap_coords[2] -= 2
        else:
            while self.overlap_coords[3] >= self.overlap_coords[1]:
                if self.board.board[self.overlap_coords[3]][self.overlap_coords[1]] == "&":
                    print('overlap')
                    return False
                self.overlap_coords[3] -= 1
        return True


    def parse_input(self,user_input):
        self.x1 = self.board_map[user_input[0]] 
        self.y1 = self.board_map[user_input[1]]
        self.x2 = self.board_map[user_input[3]]
        self.y2 = self.board_map[user_input[4]]
        if self.x1 > self.x2:    #swap values if first is greater than second (meaning user input right to left, down to up)
            self.temp = self.x1  #now all checks can be left to right, up to down. 
            self.x1 = self.x2
            self.x2 = self.temp
        if self.y1 > self.y2:
            self.temp = self.y2
            self.y1 = self.y2
            self.y2 = self.temp
        return self.x1, self.y1, self.x2, self.y2

    def check_orientation(self,coords):
        if coords[0] == coords[2]:
            return 'horizontal'
        elif coords[1] == coords[3]:
            return 'vertical'
        else:
            print('please place craft either horizontally or vertically')
            return False

    
    






