from settings import *

from base_model import BaseModel


class Score(BaseModel):
    def __init__(self, font):
        self.surface = self.set_surface()
        self.rect = self.surface.get_rect(bottomright=(
            Settings.WINDOW_WIDTH - Settings.PADDING, Settings.WINDOW_HEIGHT - Settings.PADDING))
        self.display_surface = self.set_display_surface()

        self.border = self.surface.get_rect(topleft=(Settings.PADDING, Settings.PADDING))

        self.font = font

        self.increment_height = self.surface.get_height() / 3

        self.lines = 0
        self.score = 0
        self.level = 1

    def set_surface(self):
        return pygame.Surface((Settings.SIDEBAR_WIDTH, Settings.GAME_HEIGHT * Settings.SCORE_HEIGHT_FRACTION - Settings.PADDING))

    def set_display_surface(self):
        return pygame.display.get_surface()

    def reset_score(self):
        self.lines = 0
        self.score = 0
        self.level = 1

    def display_text(self):
        for i, text in enumerate([('Score', self.score), ('Level', self.level), ('Lines', self.lines)]):
            x = self.surface.get_width() / 2
            y = self.increment_height / 2 + i * self.increment_height
            text_surface = self.font.render(f'{text[0]}: {text[1]}', True, Settings.COLORS['WHITE'])
            text_rect = text_surface.get_rect(center=(x, y))
            self.surface.blit(text_surface, text_rect)

    def run(self):
        self.surface.fill(Settings.COLORS['GRAY'])

        self.display_text()

        self.display_surface.blit(self.surface, self.rect)

        pygame.draw.rect(self.display_surface, Settings.COLORS['WHITE'], self.rect, 3, 2)


if __name__ == '__main__':
    pass
