#################################################################################################
## -FILENAME: utils.py                                               -LAST EDITED: 11/26/2020
##
## -DESCRIPTION: holds utiltiy useful functions for this repository
##
## -NOTES: ALL CAPTIALIZED VARAIBLES ARE CONSTANTS FOUND IN SETTINGS.PY
##
## -CREATOR: Hebron Taylor                                             -DATE CREATED: 11/26/2020
#################################################################################################

import math
import random
from settings import *
'''
[[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
[(0, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 255, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255)],
[(255, 0, 0), (255, 0, 0), (0, 0, 0), (255, 165, 0), (0, 0, 0), (0, 0, 0), (0, 255, 255), (0, 0, 255), (0, 0, 255), (0, 0, 0)],
[(255, 0, 0), (0, 255, 0), (0, 255, 0), (255, 165, 0), (255, 165, 0), (255, 165, 0), (0, 255, 255), (0, 0, 0), (0, 0, 255), (0, 0, 0)],
[(0, 255, 0), (0, 255, 0), (0, 255, 255), (0, 255, 255), (0, 255, 255), (0, 255, 255), (0, 255, 255), (0, 0, 0), (0, 0, 255), (0, 0, 255)]]
'''


#locked_positions = {(1, 18): (0, 255, 0), (2, 18): (0, 255, 0), (0, 19): (0, 255, 0), (1, 19): (0, 255, 0), (4, 18): (0, 0, 255), (2, 19): (0, 0, 255), (3, 19): (0, 0, 255), (4, 19): (0, 0, 255), (0, 17): (0, 255, 255), (1, 17): (0, 255, 255), (2, 17): (0, 255, 255), (3, 17): (0, 255, 255), (5, 16): (0, 255, 255), (5, 17): (0, 255, 255), (5, 18): (0, 255, 255), (5, 19): (0, 255, 255), (6, 18): (255, 165, 0), (6, 19): (255, 165, 0), (7, 19): (255, 165, 0), (8, 19): (255, 165, 0), (6, 14): (0, 255, 0), (7, 14): (0, 255, 0), (5, 15): (0, 255, 0), (6, 15): (0, 255, 0), (1, 14): (255, 0, 0), (0, 15): (255, 0, 0), (1, 15): (255, 0, 0), (0, 16): (255, 0, 0)}

pic = {(1, 18): (0, 255, 0), (2, 18): (0, 255, 0), (0, 19): (0, 255, 0), (1, 19): (0, 255, 0), (1, 15): (128, 0, 128), (0, 16): (128, 0, 128), (1, 16): (128, 0, 128), (1, 17): (128, 0, 128), (1, 14): (0, 255, 255), (2, 14): (0, 255, 255), (3, 14): (0, 255, 255), (4, 14): (0, 255, 255), (6, 17): (255, 165, 0), (6, 18): (255, 165, 0), (5, 19): (255, 165, 0), (6, 19): (255, 165, 0), (5, 14): (0, 255, 0), (5, 15): (0, 255, 0), (6, 15): (0, 255, 0), (6, 16): (0, 255, 0), (8, 17): (255, 165, 0), (8, 18): (255, 165, 0), (7, 19): (255, 165, 0), (8, 19): (255, 165, 0), (8, 15): (255, 0, 0), (7, 16): (255, 0, 0), (8, 16): (255, 0, 0), (7, 17): (255, 0, 0)}

pic2 = {(1, 18): (128, 0, 128), (0, 19): (128, 0, 128), (1, 19): (128, 0, 128), (2, 19): (128, 0, 128), (8, 16): (0, 255, 255), (8, 17): (0, 255, 255), (8, 18): (0, 255, 255), (8, 19): (0, 255, 255), (7, 14): (128, 0, 128), (8, 14): (128, 0, 128), (9, 14): (128, 0, 128), (8, 15): (128, 0, 128)}

pic3 = {(0, 18): (255, 165, 0), (0, 19): (255, 165, 0), (1, 19): (255, 165, 0), (2, 19): (255, 165, 0), (4, 17): (0, 255, 0), (4, 18): (0, 255, 0), (5, 18): (0, 255, 0), (5, 19): (0, 255, 0), (9, 16): (0, 255, 255), (9, 17): (0, 255, 255), (9, 18): (0, 255, 255), (9, 19): (0, 255, 255), (7, 17): (255, 165, 0), (7, 18): (255, 165, 0), (6, 19): (255, 165, 0), (7, 19): (255, 165, 0), (5, 14): (255, 0, 0), (4, 15): (255, 0, 0), (5, 15): (255, 0, 0), (4, 16): (255, 0, 0)}

def get_aggregate_height(locked_positions):
    aggregate_height = 0
    sorted_pos = sorted(list(locked_positions), key=lambda x: (x[0], x[1]))  #sort locked_positions by coloumn, then by row (recall that the lower the row is the higher on the game board the piece )
    seen = set()
    aggregate_height = sum([((BOARD_HEIGHT/BLOCK_SIZE)-b) for a, b in sorted_pos if not (a in seen or seen.add(a))]) #cute way of adding up the tallest block in each column
    return aggregate_height



def get_holes(locked_positions):
    num_holes = 0
    sorted_pos = sorted(list(locked_positions), key=lambda x: (x[0], x[1]))  #sort locked_positions by coloumn, then by row (recall that the lower the row is the higher on the game board the piece )
    print(sorted_pos)
    for i, (col, row) in enumerate(sorted_pos):
        if i == len(sorted_pos)-1:
            break
        if sorted_pos[i+1][0] == col:
            num_holes += (sorted_pos[i+1][1]-row-1)
            print(col, row, "\t", sorted_pos[i+1][0],  sorted_pos[i+1][1], "\t", num_holes )
        elif sorted_pos[i+1][0] != col and row != (BOARD_HEIGHT/BLOCK_SIZE)-1:
            num_holes += int((BOARD_HEIGHT/BLOCK_SIZE)-row-1)
            print(col, row, "\t", sorted_pos[i+1][0],  sorted_pos[i+1][1], "\t", num_holes )



    #print(sorted_pos)
    pass



def get_completed_lines():
    pass


def get_bumpiness(locked_positions):
    bumpiness = 0
    sorted_pos = sorted(list(locked_positions), key=lambda x: (x[0], x[1]))  #sort locked_positions by coloumn, then by row (recall that the lower the row is the higher on the game board the piece )

    seen = set()
    top_most_pieces = [(a,b) for a, b in sorted_pos if not (a in seen or seen.add(a))]

    top_most_pieces_idx = 0
    for i in range(int(BOARD_WIDTH/BLOCK_SIZE)-1):
        top_most_cols, top_most_rows = zip(*top_most_pieces)
        if i in top_most_cols and i+1 in top_most_cols:
            bumpiness += abs(top_most_pieces[top_most_pieces_idx][1] - top_most_pieces[top_most_pieces_idx+1][1])
            top_most_pieces_idx+=1
            #print(i, i+1, bumpiness)
        elif (i in top_most_cols and i+1 not in top_most_cols) or (i not in top_most_cols and i+1 in top_most_cols):
            bumpiness += int((BOARD_HEIGHT/BLOCK_SIZE)-top_most_pieces[top_most_pieces_idx][1])
            if (i in top_most_cols and i+1 not in top_most_cols): top_most_pieces_idx+=1
            #print(i, i+1,bumpiness)

    #print(bumpiness)
    return bumpiness


get_bumpiness(pic3)
print(get_aggregate_height(pic3))
#get_holes(lp)
