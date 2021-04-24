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

import random

import utils
import gameUtils
from settings import *


pic5_lp  = {(1, 18): (0, 255, 0), (2, 18): (0, 255, 0), (0, 19): (0, 255, 0), (1, 19): (0, 255, 0), (3, 19): (0, 255, 255), (4, 19): (0, 255, 255), (5, 19): (0, 255, 255), (6, 19): (0, 255, 255), (7, 18): (255, 165, 0), (7, 19): (255, 165, 0), (8, 19): (255, 165, 0), (9, 19): (255, 165, 0), (7, 17): (255, 0, 0), (8, 17): (255, 0, 0), (8, 18): (255, 0, 0), (9, 18): (255, 0, 0), (7, 16): (255, 165, 0), (8, 16): (255, 165, 0), (9, 16): (255, 165, 0), (9, 17): (255, 165, 0), (2, 15): (255, 0, 0), (1, 16): (255, 0, 0), (2, 16): (255, 0, 0), (1, 17): (255, 0, 0), (0, 13): (0, 0, 255), (1, 13): (0, 0, 255), (1, 14): (0, 0, 255), (1, 15): (0, 0, 255), (3, 16): (128, 0, 128), (2, 17): (128, 0, 128), (3, 17): (128, 0, 128), (3, 18): (128, 0, 128), (5, 15): (0, 255, 255), (5, 16): (0, 255, 255), (5, 17): (0, 255, 255), (5, 18): (0, 255, 255)}

pic5_grid=[[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
           [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
           [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
           [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
           [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
           [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
           [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
           [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (128, 0, 128), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
           [(0, 0, 0), (0, 0, 0), (0, 0, 0), (128, 0, 128), (128, 0, 128), (128, 0, 128), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
           [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
           [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
           [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
           [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
           [(0, 0, 255), (0, 0, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
           [(0, 0, 0), (0, 0, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
           [(0, 0, 0), (0, 0, 255), (255, 0, 0), (0, 0, 0), (0, 0, 0), (0, 255, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
           [(0, 0, 0), (255, 0, 0), (255, 0, 0), (128, 0, 128), (0, 0, 0), (0, 255, 255), (0, 0, 0), (255, 165, 0), (255, 165, 0), (255, 165, 0)],
           [(0, 0, 0), (255, 0, 0), (128, 0, 128), (128, 0, 128), (0, 0, 0), (0, 255, 255), (0, 0, 0), (255, 0, 0), (255, 0, 0), (255, 165, 0)],
           [(0, 0, 0), (0, 255, 0), (0, 255, 0), (128, 0, 128), (0, 0, 0), (0, 255, 255), (0, 0, 0), (255, 165, 0), (255, 0, 0), (255, 0, 0)],
           [(0, 255, 0), (0, 255, 0), (0, 0, 0), (0, 255, 255), (0, 255, 255), (0, 255, 255), (0, 255, 255), (255, 165, 0), (255, 165, 0), (255, 165, 0)]]

test=0
def optimal_position(locked_positions, grid, current_piece):
    sorted_pos = sorted(list(locked_positions), key=lambda x: (x[0], x[1]))                                          #sort locked_positions by coloumn, then by row (recall that the lower the row is the higher on the game board the piece )

    seen = set()
    top_most_pieces = [(a,b) for a, b in sorted_pos if not (a in seen or seen.add(a))]                                  #we use only the top most pieces of each column to find the height difference between each coloumn (recall how sorted_pos was sorted)
    print(top_most_pieces)

    current_piece.x = top_most_pieces[0][0]    #col
    current_piece.y = top_most_pieces[0][1]     #row

    print(current_piece.x, current_piece.y, current_piece.rotation)

    #scrub the current piece from the grid (this is temprary)
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] != (0,0,0) and (col, row) not in locked_positions:
    #            print(grid[row][col], row, col)
                grid[row][col] = (0,0,0)


    if gameUtils.valid_space(shape=current_piece, grid=grid):
        print("valid at", (current_piece.x, current_piece.y))
    else:
        print("invalid at", (current_piece.x, current_piece.y))


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

        #new_event = pygame.event.Event(pygame.locals.KEYDOWN, key=pygame.locals.K_UP, mod=pygame.locals.KMOD_NONE) #create the event
        #pygame.event.post(new_event)

        if (change_piece):
            pass
            #get the game board status

            #determine the optimal position

            #put piece into correct row/col


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
        print(current_piece.x, current_piece.y)
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
        else:
            pygame.init()
            screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
            pygame.display.set_caption("Tetris")
            main_menu(screen)


    except KeyboardInterrupt:
        print("Ctrl-C Exit!")
