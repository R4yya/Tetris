from utils.settings import *
from base_model import BaseModel


class Score(BaseModel):
    def __init__(self):
        self.surface = self.set_surface()
        self.rect = self.surface.get_rect(bottomright=(
            WINDOW_WIDTH - PADDING, WINDOW_HEIGHT - PADDING))
        self.display_surface = self.set_display_surface()

    def set_surface(self):
        return pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT * SCORE_HEIGHT_FRACTION - PADDING))

    def set_display_surface(self):
        return pygame.display.get_surface()

    def run(self):
        self.display_surface.blit(self.surface, self.rect)


if __name__ == '__main__':
    pass
