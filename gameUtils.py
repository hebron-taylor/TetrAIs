#################################################################################################
## -FILENAME: gameUtils.py                                               -LAST EDITED: 11/26/2020
##
## -DESCRIPTION: Contains functions/Classes related to playing tetris
##
## -NOTES: ALL CAPTIALIZED VARAIBLES ARE CONSTANTS FOUND IN SETTINGS.PY
##
## -CREATOR: Hebron Taylor                                             -DATE CREATED: 11/26/2020
#################################################################################################

import pygame

import random

from settings import *

class Piece():
    def __init__(self, x, y, tetromino):
        self.x = x
        self.y = y
        self.tetromino = tetromino
        self.color = TETROMINOS_COLORS[TETROMINOS.index(tetromino)]
        self.rotation = 0


#################################################################################
##############################HELPER FUNCTIONS###################################
#################################################################################

    

#################################################################################

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
#################################################################################

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
#################################################################################

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
                positions.append((shape.x + j - 2, shape.y + i)) #-2 used to account for initialized x position

    #print(positions)

    return positions
#################################################################################

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
#################################################################################

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

    sx = BOARD_X_END + 35
    sy = BOARD_Y_START + 35

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

    #TEMPORARY RENDER THE ROW AND COL NUMBERS
    for i in range(0,20):
        row_title = font.render(str(i), 1, RED)
        screen.blit(row_title, (BOARD_X_END+5, BOARD_Y_START+(i*BLOCK_SIZE) ))

    for i in range(0,10):
        col_title = font.render(str(i), 1, RED)
        screen.blit(col_title, (BOARD_X_START+(i*BLOCK_SIZE)+4, BOARD_Y_END))

    return
#################################################################################

def draw_grid(screen):
    '''
    DESCRIPTION: Draws empty game board to screen

    INPUT(s): screen (pygame surface): surface on which game will be played

    RETURN: NONE
    '''

    #comment in for grid lines on game board
    for x in range(BOARD_X_START, BOARD_X_END, BLOCK_SIZE):
        for y in range(BOARD_Y_START, BOARD_Y_END, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, (211,211,211), rect,1 )
    #end grid lines code

    pygame.draw.rect(screen, SILVER, (BOARD_X_START, BOARD_Y_START, BOARD_WIDTH, BOARD_HEIGHT), 2)
    return
#################################################################################

def draw_pieces(screen, grid):
    '''
    DESCRIPTION: draw tetromino pieces onto user screen

    INPUT(s): screen (pygame surface): surface on which game will be played
              grid   (2D array)      : 2D array which corresponds to the current tetris game grid

    RETURN: NONE
    '''


    for x in range(len(grid)):
        for y in range(len(grid[x])):
            pygame.draw.rect(screen, grid[x][y], (BOARD_X_START + (BLOCK_SIZE*y),BOARD_Y_START + (BLOCK_SIZE*x), BLOCK_SIZE, BLOCK_SIZE))
    return
#################################################################################

def get_shape():
    '''
    DESCRIPTION: Get random tetromino piece

    INPUT(s): NONE

    RETURN: NONE
    '''
    #return Piece(4, 0, random.choice(TETROMINOS))
    #return Piece(2, -1, TETROMINOS[1]) #red zig-zag piece
    #return Piece(2, -1, TETROMINOS[2]) #teal line piece
    #return Piece(2, -1, TETROMINOS[3]) #yellow cube piece
    return Piece(4, 0, TETROMINOS[6]) #purple T piece
#################################################################################

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
#################################################################################
