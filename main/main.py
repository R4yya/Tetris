from settings import *


class Main(object):
    def __init__(self):
        pygame.init()

        self.display_surface = pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Tetris')

        self.clock = pygame.time.Clock()

    def handle_events(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.running = False
                case pygame.KEYDOWN:
                    pass

    def update(self):
        pygame.display.update()

    def run(self):
        self.running = True

        while self.running:
            self.handle_events()

            self.display_surface.fill(COLORS['GRAY'])

            self.update()
            self.clock.tick()


if __name__ == '__main__':
    main = Main()
    main.run()
