import pygame


class Field(object):
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        self.field = [[0 for _ in range(width)] for _ in range(height)]

        self.grid_color = (100, 100, 100)

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
