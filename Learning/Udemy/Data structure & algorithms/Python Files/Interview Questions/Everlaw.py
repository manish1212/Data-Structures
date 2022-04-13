# Chess Game

class chessGame:
    def accept_input(self):
        self.print_board()
        print("\n")
        print('current player',self.current_player)
        # color = input('current player enter color : ')

        # color = int(color)
        try:
            row, col = input('enter move : ').split(',')
            row = int(row)
            col = int(col)
        except:
            print("enter valid input")
            self.accept_input()

        correct_color = self.is_present(self.current_player, row, col)
        # if current block consist current player's color
        if correct_color:
            if self.cache == [] or self.cache != [row, col]:
                self.cache = []
                self.perform_moves(self.current_player, row, col)
            else:
                print("Opps can't move the same piece",end='\n')
                self.accept_input()
        else:
            print("No piece here, try again',end=",'\n')
            self.accept_input()

    def perform_moves(self, color, row, col):
        # if color ==1 - > move downwards
        if color == 1:
            if col == 0:
                if self.board[row+1][col] == 0 and self.board[row+1][col+1]!=2:
                    self.board[row][col] = 0
                    self.board[row+1][col] = 1 # move forward
                    self.current_player = 2 # change player
                elif self.board[row+1][col+1]==2:
                    self.board[row][col] = 0
                    self.board[row+1][col+1] = 1 # move right diagonally
                    self.cache = [row+1, col+1] # cant perform the same move
                else:
                    print("Opps invalid move, try another moving another piece!","\n")
                    self.accept_input()

            elif col == len(self.board)-1:
                if self.board[row+1][col] == 0 and self.board[row+1][col-1] != 2:
                    self.board[row][col] = 0
                    self.board[row+1][col] = 1 # move forward
                    self.current_player = 2 # change player
                elif self.board[row+1][col-1]==2:
                    self.board[row][col] = 0
                    self.board[row+1][col-1] = 1 # move left diagonally
                    self.cache = [row+1, col-1] # cant perform the same move
                else:
                    print("Opps invalid move, try another moving another piece!","\n")
                    self.accept_input()

            elif col > 0 and col < len(self.board)-1:
                if self.board[row+1][col] == 0 and (self.board[row+1][col+1]!=2 and self.board[row+1][col-1]!=2) :
                    self.board[row][col] = 0
                    self.board[row+1][col] = 1 # move forward
                    self.current_player = 2 # change player
                elif self.board[row+1][col-1]==2:
                    self.board[row][col] = 0
                    self.board[row+1][col-1] = 1 # move left diagonally
                    self.cache = [row+1, col-1] # cant perform the same move
                elif self.board[row+1][col+1]==2:
                    self.board[row][col] = 0
                    self.board[row+1][col+1] = 1 # move right diagonally
                    self.cache = [row+1, col+1] # cant perform the same move
                else:
                    print("Opps invalid move, try another moving another piece!")
                    self.accept_input()

            if 1 in self.board[len(self.board)-1]:
                print("1 (white) Wins")
                return
        
        # if color ==2 - > move upwards
        elif color == 2:
            if col == 0:
                if self.board[row-1][col] == 0 and self.board[row-1][col+1]!=1:
                    self.board[row][col] = 0
                    self.board[row-1][col] = 2 # move forward
                    self.current_player = 1 # change player
                elif self.board[row-1][col+1]==1:
                    self.board[row][col] = 0
                    self.board[row-1][col+1] = 2 # move right diagonally
                    self.cache = [row-1, col+1] # cant perform the same move
                else:
                    print("Opps invalid move, try another moving another piece!","\n")
                    self.accept_input()

            elif col == len(self.board)-1:
                print('black last col -->')
                if self.board[row-1][col] == 0 and self.board[row-1][col-1]!=1:
                    self.board[row][col] = 0
                    self.board[row-1][col] = 2 # move forward
                    self.current_player = 1 # change player
                elif self.board[row-1][col-1]==1:
                    self.board[row][col] = 0
                    self.board[row-1][col-1] = 2 # move left diagonally
                    self.cache = [row-1, col-1] # cant perform the same move
                else:
                    print("Opps invalid move, try another moving another piece!","\n")
                    self.accept_input()

            elif col > 0 and col < len(self.board)-1:
                if self.board[row-1][col]==0 and (self.board[row-1][col-1]!=1 and self.board[row-1][col+1]!=1):
                    self.board[row][col] = 0
                    self.board[row-1][col] = 2 # move forward
                    self.current_player = 1 # change player
                elif self.board[row-1][col-1]==1:
                    self.board[row][col] = 0
                    self.board[row-1][col-1] = 2 # move left diagonally
                    self.cache = [row-1, col-1] # cant perform the same move
                elif self.board[row-1][col+1]==1:
                    self.board[row][col] = 0
                    self.board[row-1][col+1] = 2 # move right diagonally
                    self.cache = [row-1, col+1] # cant perform the same move
                else:
                    print("Opps invalid move, try another moving another piece!","\n")
                    self.accept_input()

            if 2 in self.board[0]:
                print("2 (black) Wins")
                return
        self.accept_input()      
        
    def is_present(self, color, row, col):
        if row>=len(self.board) or col>=len(self.board):
            return False
        current_block = self.board[row][col]
        return color is current_block
        
    def print_board(self):        
        for i in range(len(self.board)):
            print(self.board[i],end='\n')

    def __init__(self):        
        self.cache = [] # stores current block when diagonal move is performed
        self.current_player = 1 
        # 1 represents 'white'
        # 2 represents 'black'

        # create a board
        r,c = 8,8
        self.board = []
        for i in range(r):
            rows = []
            block = 0
            if i == 1:
                block = 1 # 'white'
            elif i == 6:
                block = 2 # 'black'
            for j in range(c):
                rows.append(block)
            self.board.append(rows)
        self.accept_input()
        

game = chessGame()

