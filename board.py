class Board:
    def __init__(self):
        self.dot = u'\u25CC'
        self.container = []
        self.key_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t']
        self.board = self.generate_board()

    def generate_board(self):
        for i in range(20):
            self.column = []
            for j in range(21):
                self.column.append(self.dot)
                self.column.append(' ')
            self.container.append(self.column)
        for k in range(20):
            self.container[k][0] = self.key_list[k]
        return self.container

    def change_board(self,x,y,z):
        self.container[x][y] = z

    def display_board(self):
        print(('  ')+ (' ').join(self.key_list).upper())
        for k in self.container:
            print(''.join(k))



