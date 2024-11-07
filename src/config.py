import pygame

#sizes 
COLUMNS = 10
ROWS = 20
CELL_SIZE = 40
GAME_WIDTH = COLUMNS * CELL_SIZE
GAME_HEIGHT = ROWS * CELL_SIZE

#side bar 
SIDEBAR_WIDTH = 200
PREVIEW_HEIGHT_FRACTION = 0.7
SCORE_HEIGHT_FRACTION = 1 - PREVIEW_HEIGHT_FRACTION

#window
PADDING = 20
WINDOW_WIDTH = GAME_WIDTH + SIDEBAR_WIDTH + PADDING * 3
WINDOW_HEIGHT = GAME_HEIGHT + PADDING * 2

#game
UPDATE_START_SPEED = 800
MOVE_WAIT_TIME = 200
ROTATE_WAIT_TIME = 200
BLOCK_OFFSET = pygame.Vector2(COLUMNS // 2, -1)

#colors

GRAY = '#808080'
YELLOW = '#FFFF00'
GREEN = '#008000'
RED = '#FF0000'
BLUE = '#0000FF'
WITHE = '#FFFFFF'
BLACK = '#000000'
GREY31 = '#4F4F4F'
