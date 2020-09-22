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

#create a grid in which we will keep track of all the positions that new pieces cannot move to
#note that row == the conventional notion of "y" as rows move in the y direction and
#          col == the conventional notion of "x" as cols move in the x direction hence
# when representing an (x,y) cooridnates as an xy postion on the gameplay grid we use col as x and row as y
#but when accessing the physical python gameplay grid structure we access as grid[row][col]
'''
 _ _ _
| | | |
|_|_|_|
| | | |
|_|_|_|
|x| | |
|_|_|_|

For example row 3 col 1 is the same as x=1, y=3 (if y is more positive as we move down )

'''
def create_grid(locked_positions = {}):
    grid = [[(0,0,0) for _ in range(int(BOARD_WIDTH/BLOCK_SIZE))] for _ in range(int(BOARD_HEIGHT/BLOCK_SIZE))]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if (col, row) in locked_positions:
                grid[row][col] = locked_positions[(col, row)]
    return grid



def draw_grid(screen):
    #
    # for x in range(board_x_start, board_x_end, BLOCK_SIZE):
    #     for y in range(board_y_start, board_y_end, BLOCK_SIZE):
    #         rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
    #         pygame.draw.rect(screen, (211,211,211), rect,1 )

    pygame.draw.rect(screen, SILVER, (board_x_start, board_y_start, BOARD_WIDTH, BOARD_HEIGHT), 2)
    return

def draw_pieces(screen, grid):

    for x in range(len(grid)):
        for y in range(len(grid[x])):
            pygame.draw.rect(screen, grid[x][y], (board_x_start + (BLOCK_SIZE*y),board_y_start + (BLOCK_SIZE*x), BLOCK_SIZE, BLOCK_SIZE))


def get_shape():
    return Piece(2, -1, random.choice(TETROMINOS))


def convert_shape_format(shape):
    positions = []
    format = shape.tetromino[shape.rotation % len(shape.tetromino)]



    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0], pos[1])
    return positions


def valid_space(shape, grid):
    accepted_pos = [[(j,i) for j in range(int(BOARD_WIDTH/BLOCK_SIZE)) if grid[i][j] == (0,0,0)] for i in range(int(BOARD_HEIGHT/BLOCK_SIZE))]
    accepted_pos = [j for sub in accepted_pos for j in sub]

    formatted = convert_shape_format(shape)
    for pos in formatted:
        if pos not in accepted_pos:
            if pos[1] > -1:
                return False
    return True


def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False

def draw_game_stats(screen, next_piece, level, lines, score):
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


def clear_rows(grid, locked_positions):
    inc = 0
    for i in range(len(grid)-1, -1, -1):
        row = grid[i]
        if (0,0,0) not in row:
            inc += 1
            ind = i
            for j in range(len(row)):
                try:
                    del locked_positions[(j, i)]
                except:
                    continue

    if inc > 0:
        for key in sorted(list(locked_positions), key=lambda x: x[1]) [::-1]:
            x, y = key
            if y < ind:
                new_key  = (x, y+inc)
                locked_positions[new_key] = locked_positions.pop(key)
    return inc


def main(screen):


    locked_positions = {}
    grid = create_grid(locked_positions)
    current_piece = get_shape()
    next_piece = get_shape()
    run = True
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = .27
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

        if fall_time / 1000 > fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not(valid_space(current_piece, grid)) or current_piece.y >= BOARD_HEIGHT/BLOCK_SIZE:
                current_piece.y -= 1
                change_piece = True

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


        shape_pos = convert_shape_format(current_piece)

        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

        draw_pieces(screen=screen, grid=grid)
        draw_grid(screen=screen)


        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
            current_lines_cleared = clear_rows(grid=grid, locked_positions=locked_positions)
            total_lines_cleared += current_lines_cleared
            if total_lines_cleared % 10 == 0 and current_lines_cleared > 0:
                level += 1
        else:
            current_lines_cleared = 0




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

        if check_lost(locked_positions):
            run = False


def main_menu(screen):
    main(screen)





if __name__ == '__main__':
    try:
        pygame.init()
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Tetris")
        main_menu(screen)

    except KeyboardInterrupt:
        print("Ctrl-C Exit!")
