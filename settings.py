#################################################################################################
## -FILENAME: settings.py                                               -LAST EDITED: 11/26/2020
##
## -DESCRIPTION: Contains constants that are used in this repository
##
## -CREATOR: Hebron Taylor                                             -DATE CREATED: 11/26/2020
#################################################################################################


# Game board information
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600

BOARD_WIDTH = 200
BOARD_HEIGHT = 400
BLOCK_SIZE = 20

BOARD_X_START = 50
BOARD_X_END = int((BOARD_X_START + BOARD_WIDTH))
BOARD_Y_START = 150
BOARD_Y_END = int((BOARD_Y_START + BOARD_HEIGHT))
#BOARD_X_START = int((WINDOW_WIDTH-BOARD_WIDTH)/2)
#BOARD_Y_START = int((WINDOW_HEIGHT-BOARD_HEIGHT)/2)

# Game colors
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


# Game piece formats
S = [['..00.',
      '.00..'],
     ['..0..',
      '..00.',
      '...0.']]


Z = [['.00..',
      '..00.'],
     ['..0..',
      '.00..',
      '.0...']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..'],
     ['0000.']]

O = [['.00..',
      '.00..']]

J = [['.0...',
      '.000.'],
     ['..00.',
      '..0..',
      '..0..'],
     ['.000.',
      '...0.'],
     ['..0..',
      '..0..',
      '.00..']]

L = [['...0.',
      '.000.'],
     ['..0..',
      '..0..',
      '..00.'],
     ['.000.',
      '.0...'],
     ['.00..',
      '..0..',
      '..0..']]

T = [['..0..',
      '.000.'],
     ['..0..',
      '..00.',
      '..0..'],
     ['.000.',
      '..0..'],
     ['..0..',
      '.00..',
      '..0..']]



TETROMINOS = [S, Z, I, O, J, L, T]
TETROMINOS_COLORS = [GREEN, RED, TEAL, YELLOW, ORANGE, BLUE, PURPLE]
