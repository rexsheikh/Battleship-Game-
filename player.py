from watercraft import Watercraft
from destroyer import Destroyer
from submarine import Submarine
from battleship import Battleship
from aircraft_carrier import Aircraft_carrier
from board import Board

class Player():
    def __init__(self):
        self.game_board = Board()
        self.attack_board = Board()
        self.destroyer = Destroyer(2,'destroyer',2)
        self.submarine = Submarine(3,'submarine',3)
        self.battleship = Battleship(4,'battleship alpha',4)
        self.battleship2 = Battleship(4,'battleship bravo',4)
        self.aircraft_carrier = Aircraft_carrier(5,'aircraft_carrier',5)
        self.fleet = [self.destroyer] #,self.submarine,self.battleship,self.battleship2,self.aircraft_carrier] 
        self.board_map = {
            'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,
            'n':13,'o':14,'p':15,'q':16,'r':17, 's':18,'t':19,
            'A':2,'B':4,'C':6,'D':8,'E':10,'F':12,'G':14,'H':16,'I':18,'J':20,'K':22,'L':24,'M':26,'N':28,'O':30,'P':32,
            'Q':34,'R':36,'S':38,'T':40
        }

    def place_craft(self):
        for craft in self.fleet:
            while True:
                self.user_input= str(input(f"Enter start/end coordinates to place {craft.name} with length {craft.length}: "))
                self.x1,self.x2,self.x2,self.y2 = list(self.parse_input(self.user_input))
                self.coords = [self.x1,self.y1,self.x2,self.y2]
                self.length_check = self.check_length(self.x1,self.y1,self.x2,self.y2,craft)
                self.orientation_check = self.check_orientation(self.x1,self.y1,self.x2,self.y2)
                self.overlap_check = self.check_overlap(self.x1,self.y1,self.x2,self.y2,self.orientation_check)
                if self.length_check == True and (self.orientation_check  == 'horizontal' or 'vertical') and self.overlap_check == True:
                    break 
            if self.orientation_check == 'horizontal': 
                while self.y2 >= (self.y1 + 2):
                    self.game_board.board[self.x1][self.y1] = u'\u25D8'
                    self.game_board.board[self.x2][self.y2] = u'\u25D8'
                    craft.coords.extend(self.coords)
                    self.y2 -= 2
                self.game_board.display_board()
            elif self.orientation_check == 'vertical': 
                while self.x2 >= self.x1:
                    self.game_board.board[self.x1][self.y1] = u'\u25D8'
                    self.game_board.board[self.x2][self.y2] = u'\u25D8'
                    craft.coords.extend(self.coords)
                    self.craft_map[craft.name] = craft.coords
                    self.x2 -= 1 
                self.board.display_board()

    def check_length(self,x1,y1,x2,y2,craft):
        if x1 == x2 and y2/y1 != craft.length:  
            print('please enter coordinates of the correct length')
            return False 
        elif y1 == y2 and (x1 + x2+ 1) != craft.length:
            print('please enter coordinates of the correct length')
            return False
        else:
            return True 
            


    def check_overlap(self,x1,y1,x2,y2,orientation):
        self.ox1,self.oy1,self.ox2,self.oy2 = x1,y1,x2,y2
        if orientation == "horizontal":
            while self.oy2 >= (self.oy1):
                if self.game_board.board[self.ox1][self.oy1] == u'\u25D8':
                    print('overlap')
                    return False
                self.oy2 -= 2
        else:
            while self.ox2 >= self.ox1:
                if self.game_board.board[self.ox1][self.oy1] == u'\u25D8':
                    print('overlap')
                    return False
                self.ox2 -= 1
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

    def check_orientation(self,x1,y1,x2,y2,):
        if x1 == x2:
            return 'horizontal'
        elif y1 == y2:
            return 'vertical'
        else:
            print('please place craft either horizontally or vertically')
            return False

    def attack(self,opponent_board,oppenent_fleet):
        self.user_input = input("Enter x and y coordinates to attack: ")
        self.x_attack = self.board_map[self.user_input[0]]
        self.y_attack = self.board_map[self.user_input[1]]
        if opponent_board[self.x_attack][self.y_attack] == u'\u25D8':
            print('***** HIT *****')
            self.attack_board.board[self.x_attack][self.y_attack] == 'X'
            self.attack_board.display_board()
            opponent_board[self.x_attack][self.y_attack] = 'X' 
            for craft in oppenent_fleet:
                self.string_coords = craft.coords.copy()
                ''.join(self.string_coords)
                for i in range(0,len(self.string_coords),2):
                    if self.x_attack in self.string_coords and self.y_attack == i + 1:
                        craft.decrement_health
                        if craft.health == 0:
                            print(f"You sunk the oppenent's {craft.name}!!")
        else:
            print('***** MISS *****')
            self.attack_board[self.x_attack][self.y_attack] == 'O'
            self.attack_board.display_board()

    def display_fleet_health(self,fleet):
        for craft in fleet:
            print(f"{craft.name} Health: {craft.health}\n")

    def fleet_health(self,fleet):
        self.total_health = 0
        for craft in self.fleet:
            self.total_health += craft.health
        return self.total_health



    
    






