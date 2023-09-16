import pygame


class Field(object):
    def __init__(self, width, height, screen_width, screen_height):
        self.width = width
        self.height = height

        self.grid_color = (100, 100, 100)

        self.grid_spacing_x = screen_width // width
        self.grid_spacing_y = screen_height // height

    def draw_grid(self, screen):
        for x in range(0, self.width * self.grid_spacing_x, self.grid_spacing_x):
            pygame.draw.line(screen, self.grid_color, (x, 0),
                             (x, self.height * self.grid_spacing_y))

        for y in range(0, self.height * self.grid_spacing_y, self.grid_spacing_y):
            pygame.draw.line(screen, self.grid_color, (0, y),
                             (self.width * self.grid_spacing_x, y))

        pygame.draw.line(screen, self.grid_color, (0, self.height * self.grid_spacing_y),
                         (self.width * self.grid_spacing_x, self.height * self.grid_spacing_y))

        pygame.draw.line(screen, self.grid_color, (self.width * self.grid_spacing_x, 0),
                         (self.width * self.grid_spacing_x, self.height * self.grid_spacing_y))
