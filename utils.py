#################################################################################################
## -FILENAME: utils.py                                               -LAST EDITED: 11/26/2020
##
## -DESCRIPTION: holds utiltiy useful functions for this repository
##
## -NOTES: ALL CAPTIALIZED VARAIBLES ARE CONSTANTS FOUND IN SETTINGS.PY
##
## -CREATOR: Hebron Taylor                                             -DATE CREATED: 11/26/2020
#################################################################################################

import random
from settings import *



pic = {(1, 18): (0, 255, 0), (2, 18): (0, 255, 0), (0, 19): (0, 255, 0), (1, 19): (0, 255, 0), (1, 15): (128, 0, 128), (0, 16): (128, 0, 128), (1, 16): (128, 0, 128), (1, 17): (128, 0, 128), (1, 14): (0, 255, 255), (2, 14): (0, 255, 255), (3, 14): (0, 255, 255), (4, 14): (0, 255, 255), (6, 17): (255, 165, 0), (6, 18): (255, 165, 0), (5, 19): (255, 165, 0), (6, 19): (255, 165, 0), (5, 14): (0, 255, 0), (5, 15): (0, 255, 0), (6, 15): (0, 255, 0), (6, 16): (0, 255, 0), (8, 17): (255, 165, 0), (8, 18): (255, 165, 0), (7, 19): (255, 165, 0), (8, 19): (255, 165, 0), (8, 15): (255, 0, 0), (7, 16): (255, 0, 0), (8, 16): (255, 0, 0), (7, 17): (255, 0, 0)}

pic2 = {(1, 18): (128, 0, 128), (0, 19): (128, 0, 128), (1, 19): (128, 0, 128), (2, 19): (128, 0, 128), (8, 16): (0, 255, 255), (8, 17): (0, 255, 255), (8, 18): (0, 255, 255), (8, 19): (0, 255, 255), (7, 14): (128, 0, 128), (8, 14): (128, 0, 128), (9, 14): (128, 0, 128), (8, 15): (128, 0, 128)}

pic3 = {(0, 18): (255, 165, 0), (0, 19): (255, 165, 0), (1, 19): (255, 165, 0), (2, 19): (255, 165, 0), (4, 17): (0, 255, 0), (4, 18): (0, 255, 0), (5, 18): (0, 255, 0), (5, 19): (0, 255, 0), (9, 16): (0, 255, 255), (9, 17): (0, 255, 255), (9, 18): (0, 255, 255), (9, 19): (0, 255, 255), (7, 17): (255, 165, 0), (7, 18): (255, 165, 0), (6, 19): (255, 165, 0), (7, 19): (255, 165, 0), (5, 14): (255, 0, 0), (4, 15): (255, 0, 0), (5, 15): (255, 0, 0), (4, 16): (255, 0, 0)}


pic4 = {(1, 18): (0, 255, 0), (2, 18): (0, 255, 0), (0, 19): (0, 255, 0), (1, 19): (0, 255, 0), (2, 15): (255, 0, 0), (1, 16): (255, 0, 0), (2, 16): (255, 0, 0), (1, 17): (255, 0, 0), (1, 14): (0, 255, 0), (2, 14): (0, 255, 0), (0, 15): (0, 255, 0), (1, 15): (0, 255, 0), (4, 17): (0, 0, 255), (4, 18): (0, 0, 255), (4, 19): (0, 0, 255), (5, 19): (0, 0, 255), (3, 15): (255, 255, 0), (4, 15): (255, 255, 0), (3, 16): (255, 255, 0), (4, 16): (255, 255, 0), (4, 14): (0, 255, 255), (5, 14): (0, 255, 255), (6, 14): (0, 255, 255), (7, 14): (0, 255, 255), (8, 16): (0, 255, 255), (8, 17): (0, 255, 255), (8, 18): (0, 255, 255), (8, 19): (0, 255, 255), (8, 13): (255, 165, 0), (9, 13): (255, 165, 0), (8, 14): (255, 165, 0), (8, 15): (255, 165, 0)}


def get_aggregate_height(locked_positions):
    '''
    DESCRIPTION: Get cumulative height of each coloumn on the tetris game board

    INPUT(s): locked_positions (Dictionary): A dictionary where a (x,y) key will correspond to a color value associated with
                                           a given tetromino
              grid (2D array): 2D array which corresponds to the current tetris game grid

    RETURN: aggregate_height (int): cumulative height of each coloumn
    '''
    aggregate_height = 0
    sorted_pos = sorted(list(locked_positions), key=lambda x: (x[0], x[1]))                                          #sort locked_positions by coloumn, then by row (recall that the lower the row is the higher on the game board the piece )
    seen = set()
    aggregate_height = sum([((BOARD_HEIGHT/BLOCK_SIZE)-b) for a, b in sorted_pos if not (a in seen or seen.add(a))]) #cute way of adding up the tallest block in each column
    return aggregate_height



def get_holes(locked_positions):
    '''
    DESCRIPTION: Get all "holes" on the tetris game board

    INPUT(s): locked_positions (Dictionary): A dictionary where a (x,y) key will correspond to a color value associated with
                                           a given tetromino
              grid (2D array): 2D array which corresponds to the current tetris game grid

    RETURN: num_holes (int): number of unplayable positions on the board

    NOTES: A hole is defined as an empty space such that there is at least one tile in the same column above it (this doesn't mean that
           the empty space must be completly surrounded by tetrominos).
    '''
    num_holes = 0
    sorted_pos = sorted(list(locked_positions), key=lambda x: (x[0], x[1]))                         #sort locked_positions by coloumn, then by row (recall that the lower the row is the higher on the game board the piece )
    #print(sorted_pos)
    for i, (col, row) in enumerate(sorted_pos):
        if i != len(sorted_pos)-1:
            if sorted_pos[i+1][0] == col:                                                           #if the next element in locked_positions is in same column as the column of the current element in locked_positions
                num_holes += (sorted_pos[i+1][1]-row-1)                                             #take the difference of the coloumns to count the number of empyty spaces between them
                #print(col, row, "\t", sorted_pos[i+1][0],  sorted_pos[i+1][1], "\t", num_holes )
            elif sorted_pos[i+1][0] != col and row != (BOARD_HEIGHT/BLOCK_SIZE)-1:                  #if there is an element in locked_positions that has unique column number (ie on the board only one piece is in a given coloumn)
                num_holes += int((BOARD_HEIGHT/BLOCK_SIZE)-row-1)                                   #just substract its row value from the max row value of the board
                #print(col, row, "\t", sorted_pos[i+1][0],  sorted_pos[i+1][1], "\t", num_holes )
        else:
            if row != (BOARD_HEIGHT/BLOCK_SIZE)-1:                                                  #Check to see if the last element in locked_positions is above the max row avlue of the board
                num_holes += int((BOARD_HEIGHT/BLOCK_SIZE)-row-1)                                   #substract its row value from the max row value of the board
                #print(col, row, "\t", "\t", num_holes )

    return num_holes




def get_completed_lines(locked_positions):
    '''
    DESCRIPTION: Determines if locked_positions contains any completed rows

    INPUT(s): locked_positions (Dictionary): A dictionary where a (x,y) key will correspond to a color value associated with
                                           a given tetromino
              grid (2D array): 2D array which corresponds to the current tetris game grid

    RETURN: num_completed_lines (int): number of completed lines


    '''
    num_completed_lines = 0
    sorted_pos = sorted(list(locked_positions), key=lambda x: (x[1], x[0]))                         #sort locked_positions by row, then by col (recall that the lower the row is the higher on the game board the piece )
    #print(sorted_pos)

    pieces_in_curr_row = 0
    prev_row = sorted_pos[0][1]
    new_row = True
    for (col, row) in sorted_pos:

        if col == 0:
            pieces_in_curr_row = 1
        elif pieces_in_curr_row == col and prev_row == row:
            pieces_in_curr_row += 1
        else:
            pieces_in_curr_row = 0
        #print(col, row, pieces_in_curr_row)

        if pieces_in_curr_row == int(BOARD_WIDTH/BLOCK_SIZE):                   #if we reach 9 pieces in a row then we have cleared a row
            num_completed_lines += 1
            pieces_in_curr_row = 0

        prev_row = row

    #print(pieces_in_curr_row)
    return num_completed_lines


def get_bumpiness(locked_positions):
    '''
    DESCRIPTION: Get cumulative height difference between adjacent columns

    INPUT(s): locked_positions (Dictionary): A dictionary where a (x,y) key will correspond to a color value associated with
                                           a given tetromino
              grid (2D array): 2D array which corresponds to the current tetris game grid

    RETURN: bumpiness (int): cumulative height difference between adjacent columns
    '''
    bumpiness = 0
    sorted_pos = sorted(list(locked_positions), key=lambda x: (x[0], x[1]))                                             #sort locked_positions by coloumn, then by row (recall that the lower the row is the higher on the game board the piece )

    seen = set()
    top_most_pieces = [(a,b) for a, b in sorted_pos if not (a in seen or seen.add(a))]                                  #we use only the top most pieces of each column to find the height difference between each coloumn (recall how sorted_pos was sorted)
                                                                                                                        #we are only keeping the one element form each column which is the top most element
    top_most_pieces_idx = 0                                                                                             #use this index to increment our accesses top_most_pieces since it is possible that not all columns have pieces in them
    top_most_cols, top_most_rows = zip(*top_most_pieces)
    for i in range(int(BOARD_WIDTH/BLOCK_SIZE)-1):                                                                      #iterate though all 9 columns
        if i in top_most_cols and i+1 in top_most_cols:                                                                 #if the current column and the the next column exist in top_most_cols
            bumpiness += abs(top_most_pieces[top_most_pieces_idx][1] - top_most_pieces[top_most_pieces_idx+1][1])       #take there difference
            top_most_pieces_idx+=1                                                                                      #increment to the next element in top_most_pieces
            #print(i, i+1, bumpiness)
        elif (i in top_most_cols and i+1 not in top_most_cols) or (i not in top_most_cols and i+1 in top_most_cols):    #if the current column is in top_most_cols and the next column isn't (or the opposite)
            bumpiness += int((BOARD_HEIGHT/BLOCK_SIZE)-top_most_pieces[top_most_pieces_idx][1])                         #This means that we have a empty column so substract the max height from it
            if (i in top_most_cols and i+1 not in top_most_cols): top_most_pieces_idx+=1                                #increment to the next element in top_most_pieces only if i exisits in the top_most_pieces
            #print(i, i+1,bumpiness)

    #print(bumpiness)
    return bumpiness


'''
lp  20.0    [(4, 16), (3, 17), (4, 17), (5, 17)]
	 Height:  10.0  Holes:  2  Bump:  8
ec  125.0    [(1, 2), (0, 3), (1, 3), (2, 3)]
	 Height:  56.0  Holes:  48  Bump:  21
ec  138.0    [(2, 2), (1, 3), (2, 3), (3, 3)]
	 Height:  55.0  Holes:  47  Bump:  36
ec  138.0    [(6, 2), (5, 3), (6, 3), (7, 3)]
	 Height:  55.0  Holes:  47  Bump:  36
ec  142.0    [(7, 2), (6, 3), (7, 3), (8, 3)]
	 Height:  56.0  Holes:  48  Bump:  38
ec  127.0    [(8, 2), (7, 3), (8, 3), (9, 3)]
	 Height:  56.0  Holes:  48  Bump:  23
lp  16.0    [(3, 16), (3, 17), (4, 17), (3, 18)]
	 Height:  8.0  Holes:  0  Bump:  8
lp  22.0    [(4, 15), (4, 16), (5, 16), (4, 17)]
	 Height:  10.0  Holes:  2  Bump:  10
lp  20.0    [(5, 16), (5, 17), (6, 17), (5, 18)]
	 Height:  10.0  Holes:  2  Bump:  8
ec  87.0    [(0, 3), (0, 4), (1, 4), (0, 5)]
	 Height:  37.0  Holes:  29  Bump:  21
ec  102.0    [(1, 3), (1, 4), (2, 4), (1, 5)]
	 Height:  37.0  Holes:  29  Bump:  36
ec  98.0    [(2, 3), (2, 4), (3, 4), (2, 5)]
	 Height:  36.0  Holes:  28  Bump:  34
ec  102.0    [(6, 3), (6, 4), (7, 4), (6, 5)]
	 Height:  37.0  Holes:  29  Bump:  36
ec  104.0    [(7, 3), (7, 4), (8, 4), (7, 5)]
	 Height:  37.0  Holes:  29  Bump:  38
ec  88.0    [(8, 3), (8, 4), (9, 4), (8, 5)]
	 Height:  37.0  Holes:  29  Bump:  22
lp  18.0    [(2, 17), (3, 17), (4, 17), (3, 18)]
	 Height:  10.0  Holes:  2  Bump:  6
lp  24.0    [(3, 16), (4, 16), (5, 16), (4, 17)]
	 Height:  12.0  Holes:  4  Bump:  8
lp  18.0    [(4, 17), (5, 17), (6, 17), (5, 18)]
	 Height:  10.0  Holes:  2  Bump:  6
ec  128.0    [(0, 2), (1, 2), (2, 2), (1, 3)]
	 Height:  58.0  Holes:  50  Bump:  20
ec  142.0    [(1, 2), (2, 2), (3, 2), (2, 3)]
	 Height:  57.0  Holes:  49  Bump:  36
ec  142.0    [(5, 2), (6, 2), (7, 2), (6, 3)]
	 Height:  57.0  Holes:  49  Bump:  36
ec  146.0    [(6, 2), (7, 2), (8, 2), (7, 3)]
	 Height:  58.0  Holes:  50  Bump:  38
ec  130.0    [(7, 2), (8, 2), (9, 2), (8, 3)]
	 Height:  58.0  Holes:  50  Bump:  22
lp  20.0    [(3, 16), (2, 17), (3, 17), (3, 18)]
	 Height:  10.0  Holes:  2  Bump:  8
lp  22.0    [(4, 15), (3, 16), (4, 16), (4, 17)]
	 Height:  10.0  Holes:  2  Bump:  10
lp  16.0    [(5, 16), (4, 17), (5, 17), (5, 18)]
	 Height:  8.0  Holes:  0  Bump:  8
ec  88.0    [(1, 3), (0, 4), (1, 4), (1, 5)]
	 Height:  37.0  Holes:  29  Bump:  22
ec  102.0    [(2, 3), (1, 4), (2, 4), (2, 5)]
	 Height:  37.0  Holes:  29  Bump:  36
ec  98.0    [(6, 3), (5, 4), (6, 4), (6, 5)]
	 Height:  36.0  Holes:  28  Bump:  34
ec  102.0    [(7, 3), (6, 4), (7, 4), (7, 5)]
	 Height:  37.0  Holes:  29  Bump:  36
ec  104.0    [(8, 3), (7, 4), (8, 4), (8, 5)]
	 Height:  37.0  Holes:  29  Bump:  38
ec  87.0    [(9, 3), (8, 4), (9, 4), (9, 5)]
	 Height:  37.0  Holes:  29  Bump:  21
Best Score:  16.0 1 [(3, 16), (3, 17), (4, 17), (3, 18)]

'''

#test = {(3, 19): (128, 0, 128), (4, 19): (128, 0, 128), (5, 19): (128, 0, 128), (4, 18): (128, 0, 128)}

#print(get_holes(locked_positions=test))
