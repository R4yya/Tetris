from settings import *

from base_model import BaseModel

from tetromino import Tetromino

from random import choice


class Game(BaseModel):
    def __init__(self):
        self.surface = self.set_surface()
        self.display_surface = self.set_display_surface()

        self.border = self.surface.get_rect(topleft=(PADDING, PADDING))

        self.sprites = pygame.sprite.Group()

        self.line_surface = self.surface.copy()
        self.line_surface.fill(COLORS['PURE_GREEN'])
        self.line_surface.set_colorkey(COLORS['PURE_GREEN'])
        self.line_surface.set_alpha(120)

        self.tetromino = Tetromino(choice(list(TETROMINOS.keys())), self.sprites)

    def set_surface(self):
        return pygame.Surface((GAME_WIDTH, GAME_HEIGHT))

    def set_display_surface(self):
        return pygame.display.get_surface()

    def draw_grid(self):
        for col in range(1, COLUMNS):
            x = col * CELL_SIZE
            pygame.draw.line(
                self.line_surface, COLORS['WHITE'], (x, 0), (x, self.line_surface.get_height()), 1)

        for row in range(1, ROWS):
            y = row * CELL_SIZE
            pygame.draw.line(
                self.line_surface, COLORS['WHITE'], (0, y), (self.line_surface.get_width(), y), 1)

        self.surface.blit(self.line_surface, (0, 0))

    def run(self):

        self.surface.fill(COLORS['GRAY'])

        self.sprites.draw(self.surface)

        self.draw_grid()

        self.display_surface.blit(self.surface, (PADDING, PADDING))

        pygame.draw.rect(self.display_surface,
                         COLORS['WHITE'], self.border, 2, 0)


if __name__ == '__main__':
    pass
