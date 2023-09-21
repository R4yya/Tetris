import pygame

columns = 10
rows = 20
cell_size = 40
game_width, game_height = columns * cell_size, rows * cell_size

sidebar_width = 200
preview_height_fraction = 0.7
score_preview_fraction = 1 - preview_height_fraction

padding = 20
window_width = game_width + sidebar_width + padding * 3
window_height = game_height + padding * 2

update_start_speed = 800
move_wait_time = 200
rotate_wait_time = 200
block_offset = pygame.Vector2(columns // 2, -1)

colors = {'yellow': '#f1e60d',
          'red': '#e51b20',
          'blue': '#204b9b',
          'green': '#65b32e',
          'purple': '#7b217f',
          'cyan': '#6cc6d9',
          'orange': '#f07',
          'gray': '#1c1c1c',
          'white': '#ffffff'}

tetrominos = {'T': {'shape': [(0, 0), (-1, 0), (1, 0), (0, -1)], 'color': colors['purple']},
              'O': {'shape': [(0, 0), (0, -1), (1, 0), (1, -1)], 'color': colors['yellow']},
              'J': {'shape': [(0, 0), (0, -1), (0, 1), (-1, 1)], 'color': colors['blue']},
              'L': {'shape': [(0, 0), (0, -1), (0, 1), (1, 1)], 'color': colors['orange']},
              'I': {'shape': [(0, 0), (0, -1), (0, -2), (0, 1)], 'color': colors['cyan']},
              'S': {'shape': [(0, 0), (-1, 0), (0, -1), (1, -1)], 'color': colors['green']},
              'Z': {'shape': [(0, 0), (1, 0), (0, -1), (-1, -1)], 'color': colors['red']}}

score_data = {1: 40, 2: 100, 3: 300, 4: 1200}

if __name__ == '__main__':
    pass
