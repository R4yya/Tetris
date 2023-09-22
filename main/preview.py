from utils.settings import *
from base_model import BaseModel


class Preview(BaseModel):
    def __init__(self):
        self.surface = self.set_surface()
        self.display_surface = self.set_display_surface()

    def set_surface(self):
        return pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT * PREVIEW_HEIGHT_FRACTION))

    def set_display_surface(self):
        return pygame.display.get_surface()

    def run(self):
        self.display_surface.blit(
            self.surface, (PADDING * 2 + GAME_WIDTH, PADDING))


if __name__ == '__main__':
    pass
