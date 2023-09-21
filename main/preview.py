from settings import *


class Preview(object):
    def __init__(self):
        self.surface = pygame.Surface(
            (SIDEBAR_WIDTH, GAME_HEIGHT * PREVIEW_HEIGHT_FRACTION))
        self.display_surface = pygame.display.get_surface()

    def run(self):
        self.display_surface.blit(
            self.surface, (PADDING * 2 + GAME_WIDTH, PADDING))


if __name__ == '__main__':
    pass
