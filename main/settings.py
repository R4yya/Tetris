import pygame

COLUMNS = 10
ROWS = 20
CELL_SIZE = 40
GAME_WIDTH, GAME_HEIGHT = COLUMNS * CELL_SIZE, ROWS * CELL_SIZE

SIDEBAR_WIDTH = 200
PREVIEW_HEIGHT_FRACTION = 0.7
SCORE_HEIGHT_FRACTION = 1 - PREVIEW_HEIGHT_FRACTION

PADDING = 20
WINDOW_WIDTH = GAME_WIDTH + SIDEBAR_WIDTH + PADDING * 3
WINDOW_HEIGHT = GAME_HEIGHT + PADDING * 2

UPDATE_START_SPEED = 200
MOVE_WAIT_TIME = 200
ROTATE_WAIT_TIME = 200
BLOCK_OFFSET = pygame.Vector2(COLUMNS // 2, -1)


COLORS = {'YELLOW': '#f1e60d',
          'RED': '#e51b20',
          'BLUE': '#204b9b',
          'GREEN': '#65b32e',
          'PURPLE': '#7b217f',
          'CYAN': '#6cc6d9',
          'ORANGE': '#f07e13',
          'GRAY': '#1c1c1c',
          'WHITE': '#ffffff',
          'PURE_GREEN': '#00ff00'}

TETROMINOS = {'T': {'shape': [(0, 0), (-1, 0), (1, 0), (0, -1)], 'color': COLORS['PURPLE']},
              'O': {'shape': [(0, 0), (0, -1), (1, 0), (1, -1)], 'color': COLORS['YELLOW']},
              'J': {'shape': [(0, 0), (0, -1), (0, 1), (-1, 1)], 'color': COLORS['BLUE']},
              'L': {'shape': [(0, 0), (0, -1), (0, 1), (1, 1)], 'color': COLORS['ORANGE']},
              'I': {'shape': [(0, 0), (0, -1), (0, -2), (0, 1)], 'color': COLORS['CYAN']},
              'S': {'shape': [(0, 0), (-1, 0), (0, -1), (1, -1)], 'color': COLORS['GREEN']},
              'Z': {'shape': [(0, 0), (1, 0), (0, -1), (-1, -1)], 'color': COLORS['RED']}}

SCORE_DATA = {1: 40, 2: 100, 3: 300, 4: 1200}

if __name__ == '__main__':
    pass
