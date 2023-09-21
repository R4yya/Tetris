import pygame


class Field(object):
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        self.field = [[0 for _ in range(width)] for _ in range(height)]

        self.grid_color = (100, 100, 100)

    def check_lines(self):
        lines_to_remove = []

        for row in range(self.height):
            if all(self.field[row]):
                lines_to_remove.append(row)

        for row in lines_to_remove:
            del self.field[row]
            self.field.insert(0, [0] * self.width)

    def draw_fallen_tetromino(self, screen, tetromino):
        current_shape = tetromino.current_shape
        x, y = tetromino.x, tetromino.y

        for row in range(len(current_shape)):
            for col in range(len(current_shape[0])):
                if current_shape[row][col] == 1:
                    pygame.draw.rect(screen, tetromino.color, (x + col * self.cell_size,
                                                               y + row * self.cell_size, self.cell_size, self.cell_size))

    def update(self, screen, tetromino):
        current_shape = tetromino.current_shape
        x, y = tetromino.x, tetromino.y

        for row in range(len(current_shape)):
            for col in range(len(current_shape[0])):
                if current_shape[row][col] == 1:
                    self.field[y // self.cell_size +
                               row][x // self.cell_size + col] = 1

        self.draw_fallen_tetromino(screen, tetromino)

    def draw_grid(self, screen):
        for x in range(0, self.width * self.cell_size, self.cell_size):
            pygame.draw.line(screen, self.grid_color, (x, 0),
                             (x, self.height * self.cell_size))

        for y in range(0, self.height * self.cell_size, self.cell_size):
            pygame.draw.line(screen, self.grid_color, (0, y),
                             (self.width * self.cell_size, y))

        pygame.draw.line(screen, self.grid_color, (0, self.height * self.cell_size),
                         (self.width * self.cell_size, self.height * self.cell_size))

        pygame.draw.line(screen, self.grid_color, (self.width * self.cell_size, 0),
                         (self.width * self.cell_size, self.height * self.cell_size))
