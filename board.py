import pygame
import random

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600

BOARD_WIDTH = 200
BOARD_HEIGHT = 400
BLOCK_SIZE = 20

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)


def draw_grid(screen):
    board_x_start = int((WINDOW_WIDTH-BOARD_WIDTH)/2)
    board_x_end = int((board_x_start + BOARD_WIDTH))

    board_y_start = int((WINDOW_HEIGHT-BOARD_HEIGHT)/2)
    board_y_end = int((board_y_start + BOARD_HEIGHT))
    #print(board_x_start, board_y_start, board_x_end, board_y_end)

    for x in range(board_x_start, board_x_end, BLOCK_SIZE):
        for y in range(board_y_start, board_y_end, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, WHITE, rect,1 )
    return



def main():

    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))



    running = True
    while running:
        screen.fill(BLACK)

        draw_grid(screen=screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Ctrl-C Exit!")
