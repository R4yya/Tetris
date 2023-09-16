from random import choice
import pygame


class Tetromino(object):
    def __init__(self, cell_size):
        self.shapes = [
            [[1, 1, 1, 1]],  # I

            [[1, 1],         # O
             [1, 1]],

            [[1, 1, 1],      # T
             [0, 1, 0]],

            [[1, 1, 0],      # Z
             [0, 1, 1]],

            [[0, 1, 1],      # S
             [1, 1, 0]],

            [[0, 1],         # J
             [0, 1],
             [1, 1]],

            [[1, 0],         # L
             [1, 0],
             [1, 1]]]

        self.colors = [
            (187, 75, 187),
            (57, 41, 118),
            (70, 174, 153),
            (19, 120, 44),
            (191, 194, 0),
            (209, 98, 0),
            (130, 0, 0)]

        self.current_shape = choice(self.shapes)

        self.x = 0
        self.y = 0

        self.cell_size = cell_size

    def draw(self, screen):
        for row in range(len(self.current_shape)):
            for col in range(len(self.current_shape[0])):
                if self.current_shape[row][col] == 1:
                    pygame.draw.rect(screen, (255, 0, 0), (self.x + col * self.cell_size,
                                                           self.y + row * self.cell_size, self.cell_size, self.cell_size))

    def move_left(self):
        self.x -= self.cell_size

    def move_right(self):
        self.x += self.cell_size

    def move_down(self):
        self.y += self.cell_size

    def rotate(self):
        self.current_shape = list(zip(*self.current_shape[::-1]))

    def check_collision(self):
        pass
