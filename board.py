#################################################################################################
## -FILENAME: board.py                                               -LAST EDITED: 11/26/2020
##
## -DESCRIPTION: Contains main game code for tetris
##
## -NOTES: ALL CAPTIALIZED VARAIBLES ARE CONSTANTS FOUND IN SETTINGS.PY
##
## -CREATOR: Hebron Taylor                                             -DATE CREATED: 11/26/2020
#################################################################################################

import pygame
import pygame.locals

import sys
import copy
import time
import random

import utils
import gameUtils
from settings import *

pic5_lp = {(1, 18): (128, 0, 128), (0, 19): (128, 0, 128), (1, 19): (128, 0, 128), (2, 19): (128, 0, 128), (3, 18): (128, 0, 128), (4, 18): (128, 0, 128), (5, 18): (128, 0, 128), (4, 19): (128, 0, 128), (1, 15): (128, 0, 128), (0, 16): (128, 0, 128), (1, 16): (128, 0, 128), (1, 17): (128, 0, 128), (4, 15): (128, 0, 128), (3, 16): (128, 0, 128), (4, 16): (128, 0, 128), (4, 17): (128, 0, 128), (4, 14): (128, 0, 128), (5, 14): (128, 0, 128), (6, 14): (128, 0, 128), (5, 15): (128, 0, 128), (8, 17): (128, 0, 128), (8, 18): (128, 0, 128), (9, 18): (128, 0, 128), (8, 19): (128, 0, 128), (8, 14): (128, 0, 128), (7, 15): (128, 0, 128), (8, 15): (128, 0, 128), (8, 16): (128, 0, 128), (7, 12): (128, 0, 128), (8, 12): (128, 0, 128), (9, 12): (128, 0, 128), (8, 13): (128, 0, 128), (1, 12): (128, 0, 128), (0, 13): (128, 0, 128), (1, 13): (128, 0, 128), (1, 14): (128, 0, 128)}

pic5_grid = [[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (128, 0, 128), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (128, 0, 128), (128, 0, 128), (128, 0, 128), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (128, 0, 128), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (128, 0, 128), (128, 0, 128), (128, 0, 128)], [(128, 0, 128), (128, 0, 128), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (128, 0, 128), (0, 0, 0)], [(0, 0, 0), (128, 0, 128), (0, 0, 0), (0, 0, 0), (128, 0, 128), (128, 0, 128), (128, 0, 128), (0, 0, 0), (128, 0, 128), (0, 0, 0)], [(0, 0, 0), (128, 0, 128), (0, 0, 0), (0, 0, 0), (128, 0, 128), (128, 0, 128), (0, 0, 0), (128, 0, 128), (128, 0, 128), (0, 0, 0)], [(128, 0, 128), (128, 0, 128), (0, 0, 0), (128, 0, 128), (128, 0, 128), (0, 0, 0), (0, 0, 0), (0, 0, 0), (128, 0, 128), (0, 0, 0)], [(0, 0, 0), (128, 0, 128), (0, 0, 0), (0, 0, 0), (128, 0, 128), (0, 0, 0), (0, 0, 0), (0, 0, 0), (128, 0, 128), (0, 0, 0)], [(0, 0, 0), (128, 0, 128), (0, 0, 0), (128, 0, 128), (128, 0, 128), (128, 0, 128), (0, 0, 0), (0, 0, 0), (128, 0, 128), (128, 0, 128)], [(128, 0, 128), (128, 0, 128), (128, 0, 128), (0, 0, 0), (128, 0, 128), (0, 0, 0), (0, 0, 0), (0, 0, 0), (128, 0, 128), (0, 0, 0)]]


test=0
# def test(current_piece):
#     print(current_piece.get_height())
#     print(current_piece.get_width())


def optimal_position(locked_positions, grid, current_piece):
    sorted_pos = sorted(list(locked_positions), key=lambda x: (x[0], x[1]))                                          #sort locked_positions by coloumn, then by row (recall that the lower the row is the higher on the game board the piece )

    seen = set()
    top_most_pieces = [(a,b) for a, b in sorted_pos if not (a in seen or seen.add(a))]                                  #we use only the top most pieces of each column to find the height difference between each coloumn (recall how sorted_pos was sorted)
    #print(top_most_pieces)

    #current_piece.x = top_most_pieces[0][0]    #col
    #current_piece.y = top_most_pieces[0][1]     #row
    #print("x: %d, y:%d, rot:%d" % (current_piece.x, current_piece.y, current_piece.rotation))


    #scrub the current piece from the grid (this is temprary)
    # for row in range(len(grid)):
    #     for col in range(len(grid[row])):
    #         if grid[row][col] != (0,0,0) and (col, row) not in locked_positions:
    #             grid[row][col] = (0,0,0)


    #note down any columns that don't have a locked postion
    empty_cols = []
    for i in range(0,10):
        if not any(i in piece for piece in top_most_pieces):
            empty_cols.append(i)


    best_score = sys.maxsize
    best_piece = gameUtils.Piece(0,0,TETROMINOS[0])


    #Iterate through all rotations for the current tetromino
    for i, rotation in enumerate(current_piece.tetromino):
        current_piece.rotation = i
        #print("ROTATION:", i)

        #iterate through all the top most locked postions
        for piece in top_most_pieces:
            #set the current piece x,y, to the first possible valid location above the current locked postions
            current_piece.x = piece[0]
            current_piece.y = piece[1] - len(rotation)

            #create a copy of the locked position to use as a template
            future_locked_postions = copy.deepcopy(locked_positions)

            #See if the x,y, and rotation is a valid position on the tetris grid
            if gameUtils.valid_space(shape=current_piece, grid=grid):
                #print("valid at", (current_piece.x, current_piece.y), gameUtils.convert_shape_format(current_piece))
                shape_pos = gameUtils.convert_shape_format(current_piece)
                for pos in shape_pos:
                    p = (pos[0], pos[1])
                    future_locked_postions[p] = current_piece.color #update locked_positions because that piece is now locked in place and cannot move unless the row can be cleared

                total_score = utils.get_aggregate_height(future_locked_postions) +  utils.get_holes(future_locked_postions) - utils.get_completed_lines(future_locked_postions) + utils.get_bumpiness(future_locked_postions)
                #print("lp ", total_score, "  ", gameUtils.convert_shape_format(current_piece))
                #print("\t Height: ", utils.get_aggregate_height(future_locked_postions), " Holes: ",utils.get_holes(future_locked_postions), " Bump: ", utils.get_bumpiness(future_locked_postions) )
                if(total_score < best_score):
                    best_score =  total_score
                    best_piece = copy.deepcopy(current_piece)

        #iterate any row positions not in locked positions
        for col in empty_cols:
            current_piece.x = col
            current_piece.y = int(BOARD_HEIGHT/BLOCK_SIZE) - len(rotation) - 1

            #create a copy of the locked position to use as a template
            future_locked_postions = copy.deepcopy(locked_positions)

            #See if the x,y, and rotation is a valid position on the tetris grid
            if gameUtils.valid_space(shape=current_piece, grid=grid):
                #print("valid at", (current_piece.x, current_piece.y), gameUtils.convert_shape_format(current_piece))
                shape_pos = gameUtils.convert_shape_format(current_piece)
                for pos in shape_pos:
                    p = (pos[0], pos[1])
                    future_locked_postions[p] = current_piece.color #update locked_positions because that piece is now locked in place and cannot move unless the row can be cleared

                total_score = utils.get_aggregate_height(future_locked_postions) +  utils.get_holes(future_locked_postions) - utils.get_completed_lines(future_locked_postions) + utils.get_bumpiness(future_locked_postions)
                #print("ec ",total_score, "  ", gameUtils.convert_shape_format(current_piece))
                #print("\t Height: ", utils.get_aggregate_height(future_locked_postions), " Holes: ",utils.get_holes(future_locked_postions), " Bump: ", utils.get_bumpiness(future_locked_postions) )
                if(total_score < best_score):
                    best_score = total_score
                    best_piece = copy.deepcopy(current_piece)

                # print(utils.get_aggregate_height(future_locked_postions))
                # print(utils.get_holes(future_locked_postions))
                # print(utils.get_completed_lines(future_locked_postions))
                # print(utils.get_bumpiness(future_locked_postions))


    print("Best Score: ", best_score, best_piece.rotation, gameUtils.convert_shape_format(best_piece))
    return best_piece




def main(screen):
    '''
    DESCRIPTION: Where the main game loop resides. All game play activity happens here.

    INPUT(s): screen (pygame surface): surface on which game will be played

    RETURN: NONE
    '''

    locked_positions = {}
    grid = gameUtils.create_grid(locked_positions)
    current_piece = gameUtils.get_shape()
    next_piece = gameUtils.get_shape()
    run = True
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 1
    change_piece = False
    level = 1
    score = 0
    current_lines_cleared = 0
    total_lines_cleared = 0
    piece_placed = True
    desired_location = gameUtils.Piece(0,0,TETROMINOS[0])

    while run:
        screen.fill(BLACK)
        grid = gameUtils.create_grid(locked_positions)

        fall_time += clock.get_rawtime()
        clock.tick()


        #Determine how fast the blocks should fall on the screeen
        if fall_time / 1000 > fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not(gameUtils.valid_space(current_piece, grid)) or current_piece.y >= BOARD_HEIGHT/BLOCK_SIZE: #tells us when the current piece has hit the bottom of the playable game grid
                current_piece.y -= 1
                change_piece = True
        #End Fall time

        # new_event = pygame.event.Event(pygame.locals.KEYDOWN, key=pygame.locals.K_UP, mod=pygame.locals.KMOD_NONE) #create the event
        # pygame.event.post(new_event)


        if (not piece_placed):

            #First check if the desired location is reachable w/o extra manuevers
            print("Height: %d" %(desired_location.get_height()))
            print("Width: %d " % (desired_location.get_width()))

            if(current_piece.rotation % len(current_piece.tetromino) != desired_location.rotation):
                new_event = pygame.event.Event(pygame.locals.KEYDOWN, key=pygame.locals.K_UP, mod=pygame.locals.KMOD_NONE) #create the event
                pygame.event.post(new_event)
            # if(current_piece.y == desired_location.y):
            #     pass
            elif(current_piece.x < desired_location.x):
                new_event = pygame.event.Event(pygame.locals.KEYDOWN, key=pygame.locals.K_RIGHT, mod=pygame.locals.KMOD_NONE) #create the event
                pygame.event.post(new_event)
            elif(current_piece.x > desired_location.x):
                new_event = pygame.event.Event(pygame.locals.KEYDOWN, key=pygame.locals.K_LEFT, mod=pygame.locals.KMOD_NONE) #create the event
                pygame.event.post(new_event)
            else:
                piece_placed = True


        #Get keyboard strokes and determine what moving block should do with respect to key stroke
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not(gameUtils.valid_space(current_piece, grid)):
                        current_piece.x += 1

                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not(gameUtils.valid_space(current_piece, grid)):
                        current_piece.x -= 1

                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not(gameUtils.valid_space(current_piece, grid)):
                        current_piece.y -= 1

                if event.key == pygame.K_UP:
                    current_piece.rotation += 1
                    if not(gameUtils.valid_space(current_piece, grid)):
                        current_piece.rotation -= 1
        #End keyoard strokes


        shape_pos = gameUtils.convert_shape_format(current_piece) #convert the tetrimono into a something that can be put into a python grid

        #color the grid respective of the current piece
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

        gameUtils.draw_pieces(screen=screen, grid=grid)
        gameUtils.draw_grid(screen=screen)


        #determine what to do once current pieces touches another piece or the bottom of the grid
        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color #update locked_positions because that piece is now locked in place and cannot move unless the row can be cleared
            current_piece = next_piece
            next_piece = gameUtils.get_shape()
            change_piece = False        #dont' execite this code until the next piece touches another pience
            piece_placed = False
            desired_location = optimal_position(locked_positions=copy.deepcopy(locked_positions),grid=grid, current_piece=copy.deepcopy(current_piece))
            current_lines_cleared = gameUtils.clear_rows(grid=grid, locked_positions=locked_positions)
            total_lines_cleared += current_lines_cleared
            if total_lines_cleared % 10 == 0 and current_lines_cleared > 0: #update speed based on score
                fall_speed -= .075
                level += 1
        else:
            current_lines_cleared = 0

        #print('\n\n')
        #print(locked_positions)
        #print(grid)
        #print(current_piece.x, current_piece.y)
        #print('\n\n')

        #calculate game score
        if current_lines_cleared == 1:
            score += 40 * (level + 1)
        if current_lines_cleared == 2:
            score += 100 * (level + 1)
        if current_lines_cleared == 3:
            score += 300 * (level + 1)
        if current_lines_cleared == 4:
            score += 1200 * (level + 1)

        gameUtils.draw_game_stats(screen=screen, next_piece=next_piece, level=level, lines=total_lines_cleared, score=score)
        pygame.display.update()

        #check if the game lost condition is triggered
        if gameUtils.check_lost(locked_positions):
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
        if test:
            optimal_position(locked_positions=pic5_lp,grid=pic5_grid, current_piece=gameUtils.get_shape())
            #test(current_piece=gameUtils.get_shape())
        else:
            pygame.init()
            screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
            pygame.display.set_caption("Tetris")
            main_menu(screen)


    except KeyboardInterrupt:
        print("Ctrl-C Exit!")
