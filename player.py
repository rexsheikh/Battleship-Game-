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
        self.fleet = [self.destroyer]
        self.board_map = {
            'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,
            'n':13,'o':14,'p':15,'q':16,'r':17, 's':18,'t':19,
            'A':2,'B':4,'C':6,'D':8,'E':10,'F':12,'G':14,'H':16,'I':18,'J':20,'K':22,'L':24,'M':26,'N':28,'O':30,'P':32,
            'Q':34,'R':36,'S':38,'T':40
        }
        # ,self.submarine,self.battleship,self.battleship2,self.aircraft_carrier]

    def place_craft(self):
        for craft in self.fleet:
            self.user_x_input= str(input(f"Enter coordinates to place {craft.name} with length {craft.length}. eg:aA/aB: "))
            
            # self.board.change_board(self.start_x,self.start_y,'X')
            # self.board.change_board(self.end_x,self.end_y,'Y')

    # def parse_input(self,input):
    #     self.to_list = input.split('/')

    # uppercase letters minus 63 give proper board orientation
    # lowercase letters minus 97 give proper board orientation
#     sample_input = 'aA/aB'
# print(ord(sample_input[0]-97))

    def check_overlap(self):
        pass 

    def check_diagonal(self):
        pass 

