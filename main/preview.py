from settings import *
from base_model import BaseModel
from os import path


class Preview(BaseModel):
    def __init__(self, next_shapes):
        self.surface = self.set_surface()
        self.display_surface = self.set_display_surface()

        self.next_shapes = next_shapes
        self.shapes_surfaces = {shape: pygame.image.load(path.join('..', 'graphics', f'{shape}.png')).convert_alpha() for shape in TETROMINOS.keys()}
        self.rect = self.surface.get_rect(topright=(WINDOW_WIDTH - PADDING, PADDING))

    def set_surface(self):
        return pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT * PREVIEW_HEIGHT_FRACTION))

    def set_display_surface(self):
        return pygame.display.get_surface()

    def run(self):
        self.surface.fill(COLORS['GRAY'])
        self.display_surface.blit(self.surface, self.rect)
        pygame.draw.rect(self.display_surface, COLORS['WHITE'], self.rect, 2, 2)


if __name__ == '__main__':
    pass
