from settings import *

from base_model import BaseModel

from os import path


class Preview(BaseModel):
    def __init__(self):
        self.surface = self.set_surface()
        self.display_surface = self.set_display_surface()

        self.shape_surfaces = {shape: pygame.image.load(path.join('..', 'graphics', f'{shape}.png')).convert_alpha() for shape in Settings.TETROMINOS.keys()}
        self.rect = self.surface.get_rect(topright=(Settings.WINDOW_WIDTH - Settings.PADDING, Settings.PADDING))

        self.increment_height = self.surface.get_height() / 3

    def set_surface(self):
        return pygame.Surface((Settings.SIDEBAR_WIDTH, Settings.GAME_HEIGHT * Settings.PREVIEW_HEIGHT_FRACTION))

    def set_display_surface(self):
        return pygame.display.get_surface()

    def display_pieces(self, next_shapes):
        for i, shape in enumerate(next_shapes):
            shape_surface = self.shape_surfaces[shape]
            x = self.surface.get_width() / 2
            y = self.increment_height / 2 + i * self.increment_height
            rect = shape_surface.get_rect(center=(x, y))
            self.surface.blit(shape_surface, rect)

    def run(self, next_shapes):
        self.surface.fill(Settings.COLORS['GRAY'])
        
        self.display_pieces(next_shapes)
        
        self.display_surface.blit(self.surface, self.rect)
        
        pygame.draw.rect(self.display_surface, Settings.COLORS['WHITE'], self.rect, 3, 2)


if __name__ == '__main__':
    pass
