import pygame
import random

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600

BOARD_WIDTH = 200
BOARD_HEIGHT = 400
BLOCK_SIZE = 20

#board_x_start = int((WINDOW_WIDTH-BOARD_WIDTH)/2)
board_x_start = 50
board_x_end = int((board_x_start + BOARD_WIDTH))
#board_y_start = int((WINDOW_HEIGHT-BOARD_HEIGHT)/2)
board_y_start = 150
board_y_end = int((board_y_start + BOARD_HEIGHT))


BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
GREEN = (0, 255, 0)
RED = (255, 0 , 0)
TEAL  = (0, 255, 255)
YELLOW =  (255, 255, 0)
ORANGE = (255, 165, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
SILVER = (192,192,192)


# SHAPE FORMATS

S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]


Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]


TETROMINOS = [S, Z, I, O, J, L, T]
TETROMINOS_COLORS = [GREEN, RED, TEAL, YELLOW, ORANGE, BLUE, PURPLE]

class Piece():
    def __init__(self, x, y, tetromino):
        self.x = x
        self.y = y
        self.tetromino = tetromino
        self.color = TETROMINOS_COLORS[TETROMINOS.index(tetromino)]
        self.rotation = 0



def create_grid(locked_positions = {}):
    '''
    DESCRIPTION: create a grid in which we will keep track of all the positions that new pieces cannot move to

    INPUT(s): locked_positions (Dictionary): A dictionary where a (x,y) key will correspond to a color value associated with
                                           a given tetromino

    RETURN: grid (2D array): 2D array which corresponds to the current tetris game grid

    NOTES: row == the conventional notion of "y" as rows move in the y direction and
          col == the conventional notion of "x" as cols move in the x direction hence
          when representing an (x,y) cooridnates as an xy postion on the gameplay grid we use col as x and row as y
          but when accessing the physical python gameplay grid structure we access as grid[row][col]
         _ _ _
        | | | |
        |_|_|_|
        | | | |
        |_|_|_|
        |x| | |
        |_|_|_|

        For example row 3 col 1 is the same as x=1, y=3 (if y is more positive as we move down )
    '''

    grid = [[(0,0,0) for _ in range(int(BOARD_WIDTH/BLOCK_SIZE))] for _ in range(int(BOARD_HEIGHT/BLOCK_SIZE))]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if (col, row) in locked_positions:
                grid[row][col] = locked_positions[(col, row)]
    return grid



def draw_grid(screen):
    '''
    DESCRIPTION: Draws empty game board to screen

    INPUT(s): screen (pygame surface): surface on which game will be played

    RETURN: NONE
    '''

    #comment in for grid lines on game board
    for x in range(board_x_start, board_x_end, BLOCK_SIZE):
        for y in range(board_y_start, board_y_end, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, (211,211,211), rect,1 )
    #end grid lines code

    pygame.draw.rect(screen, SILVER, (board_x_start, board_y_start, BOARD_WIDTH, BOARD_HEIGHT), 2)
    return


def draw_pieces(screen, grid):
    '''
    DESCRIPTION: draw tetromino pieces onto user screen

    INPUT(s): screen (pygame surface): surface on which game will be played
              grid   (2D array)      : 2D array which corresponds to the current tetris game grid

    RETURN: NONE
    '''

    for x in range(len(grid)):
        for y in range(len(grid[x])):
            pygame.draw.rect(screen, grid[x][y], (board_x_start + (BLOCK_SIZE*y),board_y_start + (BLOCK_SIZE*x), BLOCK_SIZE, BLOCK_SIZE))
    return


def get_shape():
    '''
    DESCRIPTION: Get random tetromino piece

    INPUT(s): NONE

    RETURN: NONE
    '''
    #return Piece(2, -1, random.choice(TETROMINOS))
    return Piece(2, -1, TETROMINOS[2])



def convert_shape_format(shape):
    '''
    DESCRIPTION: Convert passed tetromino into format that can be used as a reference for where a piece is located
                 on the tetris grid

    INPUT(s): shape (Piece): contains information relating to the passed tetromino (position, rotation, color)

    RETURN: positions (list): A list containing the (x, y) cooridnates of the current tetromino with respect to
                              its location on the the game grid

    NOTES:  Recall one tetromino is a list as follows
                          '.....',
                          '......',
                          '..00..',
                          '.00...',
                          '.....'
            we then interate through each row and column. A '0' indicates a block that corresponds to this piece
            plus the pieces (x,y) position should be placed at this repective location in the game grid. (So one piece of the
            block would be placed at (2+x, 2+y) where x and y correspond to the current positon of the piece on the game grid)
    '''

    positions = []
    format = shape.tetromino[shape.rotation % len(shape.tetromino)]



    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))

    #used to account for any offset (may not be necessary the way I initialized a tetrominos x,y position)
    for i, pos in enumerate(positions):
        positions[i] = (pos[0], pos[1])
    return positions


def valid_space(shape, grid):
    '''
    DESCRIPTION: Determine if a the passed shape is in a valid position on the game grid

    INPUT(s): shape (Piece)    : contains information relating to the passed tetromino (position, rotation, color)
              grid  (2D array) : 2D array which corresponds to the current tetris game grid

    RETURN: Boolean value based on if the shape is in a valid postion on the game board
            (FALSE if position is not valid
             TRUE  if position is valid)
    '''
    accepted_pos = [[(j,i) for j in range(int(BOARD_WIDTH/BLOCK_SIZE)) if grid[i][j] == (0,0,0)] for i in range(int(BOARD_HEIGHT/BLOCK_SIZE))]
    accepted_pos = [j for sub in accepted_pos for j in sub]

    formatted = convert_shape_format(shape)
    for pos in formatted:
        if pos not in accepted_pos:
            if pos[1] > -1:
                return False
    return True


def check_lost(positions):
    '''
    DESCRIPTION: check to see if game grid indicates a player has lost

    INPUT(s): positions (list): A list containing the (x, y) cooridnates of the current tetromino with respect to
                              its location on the the game grid

    RETURN: Boolean value indicating the status of the game
            (if TRUE than user has lost the game, if FALSE the game continues)

    NOTES: Function check to see if any of the (x,y) cooridnates in position go above the game grid boundary
           (touch the top of the tetris game grid)
    '''
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False

def draw_game_stats(screen, next_piece, level, lines, score):
    '''
    DESCRIPTION: Draws relevant game stats on the user screen
                 (next piece, current level, number of lines cleared, and current score)

    INPUT(s): screen (pygame surface): surface on which game will be played
              next_piece (Piece): contains information relating to the next tetromino that will fall (position, rotation, color)
                                  (really just want the shape so the user can see what the next tetromino will be)
              level (int) : integer indicating the current level
              lines (int) : integer indicating the number of lines cleared
              score (int) : integer indicating the score

    RETURN: NONE
    '''

    font = pygame.font.SysFont('couriernew', 15)
    next_piece_title = font.render('Next Piece', 1, SILVER)
    level_title = font.render('Level', 1, SILVER)
    lines_title = font.render('Lines', 1, SILVER)
    score_title = font.render('Score', 1, SILVER)
    level = font.render(str(level), 1, SILVER)
    lines = font.render(str(lines), 1, SILVER)
    score = font.render(str(score), 1, SILVER)

    sx = board_x_end + 35
    sy = board_y_start + 35

    format = next_piece.tetromino[next_piece.rotation % len(next_piece.tetromino)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(screen, next_piece.color, (sx+j*BLOCK_SIZE, sy+i*BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE),0)

    pygame.draw.rect(screen, SILVER, (sx, sy-10, 100, 100), 2)

    screen.blit(next_piece_title, (sx , sy - 30))
    screen.blit(level_title, (sx , sy + 110))
    screen.blit(lines_title, (sx , sy + 160))
    screen.blit(score_title, (sx , sy + 210))
    screen.blit(level, (sx , sy + 130))
    screen.blit(lines, (sx , sy + 180))
    screen.blit(score, (sx , sy + 230))
    return

# TODO: FIX BUG
def clear_rows(grid, locked_positions):
    '''
    DESCRIPTION: Clear all "filled" rows (in accordance to the rules of tetris)

    INPUT(s): locked_positions (Dictionary): A dictionary where a (x,y) key will correspond to a color value associated with
                                           a given tetromino
              grid (2D array): 2D array which corresponds to the current tetris game grid

    RETURN: inc (int): An integer indicating how many rows were cleared

    NOTES: If a row is full then there will be no empty squares within that row (meaning (0,0,0) or the black color will not be present)
           Through this we can iterate through every row in the grid and delete all colored blocks in a given row IF no empty squares exist in that row
           This is just done by deleting the those blocks from locked_positions. Now if we delete a block via "del" it means it no longer exists which, however,
           what really needs to happen is all the blocks above the deleted block need to shift down by one (or by how many rows were suceessviely deleted). This is
           where the "inc" variable come in as it will be used to tell how many rows we should shift the current game pieces down by. We should note a few things:

           1. We iterate from the bottom of the game grid to the top of the game grid (visually from the bottom of the screen to the top). We do this so that
              while shifting blocks down we don't overwite any blocks (This is why the for loop are iterating backwards)
           2. Also recall rows will increment from the top of the game grid to the bottom of the game grid (ie row 0 is at the top of the screen and row 20 will be at the bottom of the screen).
           3. The shift list is a list of tuples that contains the current row index cleared along with the the current total count of rows cleared. Take the examples below (where . is empty space and 0 is block)

                0|....|      0|....|    In this case everything between rows 5 and 7 should move down by 1, but everything above row 5 should move down by 2
                1|....|      1|....|
                2|.00.|      2|....|
                3|.00.|  =>  3|....|
                4|.000|      4|.00.|
                5|0000|      5|.00.|
                6|.000|      6|.000|
                7|0000|      7|.000|

    '''

    inc = 0
    shift = []
    for i in range(len(grid)-1, -1, -1):
        row = grid[i]
        if (0,0,0) not in row:
            inc += 1
            ind = i
            shift.append((ind,inc))
            for j in range(len(row)):
                try:
                    del locked_positions[(j, i)]
                except:
                    print("Could not delete Row!")
                    continue




    if inc > 0:
        full_row_idx, shift_val = shift.pop(0)
        for key in sorted(list(locked_positions), key=lambda x: x[1]) [::-1]:
            x, y = key

            #if the current y locked postion is less than index of the next cleared row (so visually the locked position is above the row that was cleared on the game board)
            #we need to update the amount of row the locked postion should be shifted down by
            if (len(shift) != 0):
                if y < shift[0][0]:
                    full_row_idx, shift_val = shift.pop(0)

            if y < full_row_idx:
                new_key  = (x, y+shift_val)
                locked_positions[new_key] = locked_positions.pop(key)



    """
    if inc > 0:
        for key in sorted(list(locked_positions), key=lambda x: x[1]) [::-1]:
            x, y = key
            if y < ind:
                new_key  = (x, y+inc)
                locked_positions[new_key] = locked_positions.pop(key)
    """

    return inc


def main(screen):
    '''
    DESCRIPTION: Where the main game loop resides. All game play activity happens here.

    INPUT(s): screen (pygame surface): surface on which game will be played

    RETURN: NONE
    '''

    locked_positions = {}
    grid = create_grid(locked_positions)
    current_piece = get_shape()
    next_piece = get_shape()
    run = True
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 1
    change_piece = False
    level = 1
    score = 0
    current_lines_cleared = 0
    total_lines_cleared = 0

    while run:
        screen.fill(BLACK)
        grid = create_grid(locked_positions)

        fall_time += clock.get_rawtime()
        clock.tick()


        #Determine how fast the blocks should fall on the screeen
        if fall_time / 1000 > fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not(valid_space(current_piece, grid)) or current_piece.y >= BOARD_HEIGHT/BLOCK_SIZE: #tells us when the current piece has hit the bottom of the playable game grid
                current_piece.y -= 1
                change_piece = True
        #End Fall time

        #Get keyboard strokes and determine what moving block should do with respect to key stroke
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.x += 1

                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.x -= 1

                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.y -= 1

                if event.key == pygame.K_UP:
                    current_piece.rotation += 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.rotation -= 1
        #End keyoard strokes


        shape_pos = convert_shape_format(current_piece) #convert the tetrimono into a something that can be put into a python grid

        #color the grid respective of the current piece
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

        draw_pieces(screen=screen, grid=grid)
        draw_grid(screen=screen)


        #determine what to do once current pieces touches another piece or the bottom of the grid
        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color #update locked_positions because that piece is now locked in place and cannot move unless the row can be cleared
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False        #dont' execite this code until the next piece touches another pience
            current_lines_cleared = clear_rows(grid=grid, locked_positions=locked_positions)
            total_lines_cleared += current_lines_cleared
            if total_lines_cleared % 10 == 0 and current_lines_cleared > 0: #update speed based on score
                fall_speed -= .075
                level += 1
        else:
            current_lines_cleared = 0


        #calculate game score
        if current_lines_cleared == 1:
            score += 40 * (level + 1)
        if current_lines_cleared == 2:
            score += 100 * (level + 1)
        if current_lines_cleared == 3:
            score += 300 * (level + 1)
        if current_lines_cleared == 4:
            score += 1200 * (level + 1)

        draw_game_stats(screen=screen, next_piece=next_piece, level=level, lines=total_lines_cleared, score=score)
        pygame.display.update()

        #check if the game lost condition is triggered
        if check_lost(locked_positions):
            run = False


def main_menu(screen):
    '''
    DESCRIPTION: Get random tetromino piece

    INPUT(s): NONE

    RETURN: NONE
    '''
    main(screen)





if __name__ == '__main__':
    try:
        pygame.init()
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Tetris")
        main_menu(screen)

    except KeyboardInterrupt:
        print("Ctrl-C Exit!")
