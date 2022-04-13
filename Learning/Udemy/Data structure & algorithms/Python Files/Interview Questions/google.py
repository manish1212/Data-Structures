# design & implement the game of "snakes" - given a board of size (n,m)

# - generate a snake of size 1x1 randomly on the board

# - generate a food of size 1x1 randomly on the board

# - snake starts off not moving

# - game starts when when user presses key, continues moving in same direction until next key is pressed

# - ‘u’, ‘d’, ‘l’, ‘r’. (user input is board direction)

# - snake increases in length (by 1) when encountering food.

# - new food is randomly generated on board when old food is gone.

# - snake dies if it encounters self, or edge boundary (off “the board”) (lose)

# - game is over if snake fills entire board (win)

# - game is over if snake dies / win

# - after game over, restart the game.


# input
# m==n
# u,d,l,r

# snake initial - random
# food - random


from collections import defaultdict, deque
import random


# '0,1,2'
# 'h,4,f'
# 'h,h,8'

# {
#     0:'h',
#     1:0,
#     2:0,
#     3:'h',
#     4:0,
#     5:0,
#     6:'h',
#     7:0,
#     8:0
# }
# h = [0,1] #queue
# temp = h[0]
# h[0] = 3
# h[1] = temp
# newh = [3,0]

# h = newh
# h = [3,0]
# h[0] = 6
# prepend in h
# h[6,3,0]

# # move right
# h[6,3,0]
# h[7,6,3]

# # move up
# h[7,6,3]
# h[5,7,6]

# head=0
# up = (head-3)%3 
# down = (head+3)%3
# left = (head-1)%3
# right = (head+1)%3


class snakeGame():
    def __init__(self):
        m,n = 3,3
        self.total = m*n
        self.board = {}
        self.snake = deque()
        for i in range(1,self.total+1):
            self.board[i] = i
        self.allocateSnakeHead()

    def allocateSnakeHead(self):
        head = random.randrange(1,self.total)
        self.snake.appendleft(head)
        self.board[head] = 'S'
        print('snake->', self.snake)
        self.allocateFood()

    def allocateFood(self):
        arr = []
        for i in range(1,self.total+1):
            if i not in self.snake:
                arr.append(i)
        food = random.choice(arr)
        print('food',food)
        self.board[food] = 'F'
        # self.printboard()
 
    def printboard(self):
        for i in range(1,len(self.board)+1):
            print(self.board[i],end=' ')
            if i%3==0:
                print('')    
# 'f,s,3'
# '4,s,6'
# '7,s,s'
    def performAction(self, move):
        print('user input is', move)
        previous_head = self.snake.popleft()
        snake_head = -1
        if move == 'u':
            snake_head = previous_head - 3
            print('--up', snake_head)
        elif move == 'd':
            snake_head = previous_head + 3
            print('--down', snake_head)
        elif move == 'l':
            snake_head = previous_head - 1
            print('--left', snake_head)
        else:
            snake_head = previous_head + 1
            print('--right', snake_head)
        # snake = [5,8,9,6]
        # snake = [2,5,8,9]
        print('snake_head', snake_head)
        print('self.board[snake_head]', self.board[snake_head])
        if snake_head % 3 != 0:
            if self.board[snake_head] == 'F':
                
                self.snake.appendleft(previous_head)
                self.snake.appendleft(snake_head)
                print('previous_head, snake_head', previous_head, snake_head)
                print('after eating the food', self.snake)
                self.allocateFood()
            else:
                self.snake.appendleft(snake_head)
                for i in range(1,len(self.snake)-1):
                    temp = self.snake[i] 
                    if i == 1:
                        self.snake[i] = previous_head 
                    self.snake[i+1] = temp 
        # change board
            self.changeBoard()
            # self.printboard()
            self.getInput()
        else:
            print('game over')
            return
              

    def changeBoard(self):
        for s in self.snake:
            for i in range(1,self.total+1):
                # print('changeboard ->', self.board[i])
                if i == s:
                    self.board[i] = 'S'
                elif self.board[i] != 'F':
                    self.board[i] = i

    def getInput(self):
        self.printboard()
        key = input('enter the move:')

        if key == 'u' or key == 'd' or key == 'l' or key == 'r':
            self.performAction(key)
        else:
            print('############### WRONG KEY #############')
            self.getInput()

s = snakeGame()
s.getInput()



# def createBoard()
# def allocateFood()
# def allocateSnakeHead()
# def userInput()
# def moves()
# def win_lose()




















'''
def input(key):
    row = rand_snake_row
    col = rand_snake_col
    if key == 'u':
        snake_head = [row-1, col]
    elif key =='d':
        snake_head= [row+1, col]
    elif key =='l':
        snake_head = [row, col-1]
    elif key =='r':
        snake_head= [row, col+1]
    else:
        print('wrong input key')
        return
    previous_head = [row, col]
    moves(snake_head, previous_head)
  
def moves(snake_head, previous_head):
  0,0,0
  0,2,2
  0,0,1
  # if crossing the borders
  if snake_head[0] < 0 or snake_head[0] > row or snake_head[1] > col or snake_head[1] > row:
    # snake dies
    return 'Game over'
  row = snake_head[0]
  col = snake_head[1]
  
  prev_row = previous_head[0]
  prev_col = previous_head[1]
  
  if board[row, col]!=1:
    board[row, col] = 2
    if food_eaten >0:
      #
      # for loop to change the previous position
    else:
      board[prev_row, prev_col] = 0
    input() # call for input 
    
  if board[row, col]==1:
    board[row, col] = 2
    snake_size,append([prev_row, prev_col])
    food_eaten+=1
    rand_row, rand_col = getRandom()

#  food = 1
  board[rand_row][rand_col] = 1
  
def getRandom(0, row):
  return random.choice(0,row), random.choice(0,row)

def __init__():
  row, col = 3,3
  board = []
  snake_size = []
  food_eaten = 0
  for i in range(row):
    arr = [0]*col
    board.append(arr)
  
  rand_row, rand_col = getRandom()
  rand_snake_row,rand_snake_row = getRandom()
  
  while rand_snake_row == rand_row and rand_snake_row == rand_col:
    rand_snake_row,rand_snake_row = getRandom()
  
'''


