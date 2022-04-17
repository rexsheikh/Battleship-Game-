    # def place_craft(self):
    #     for craft in self.fleet:
    #         user_input = print(f"Enter coordinates to place {craft.name} with length {craft.length}. eg:aA/aB")
    #         self.board.change_board

    # def parse_input(self,input):
    #     self.to_list = input.split('/')
    # uppercase letters minus 63 give proper board orientation
    # lowercase letters minus 97 give proper board orientation


from random import sample
from board import Board
from player import Player




test = 'cat'


for i in range(0,len(test)):
    if "t" in test:
        print('true')