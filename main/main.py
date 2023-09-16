import pygame
from tetromino import Tetromino
from field import Field
from score import Score


class Game(object):
    def __init__(self):
        pygame.init()

        self.screen_width, self.screen_height = 481, 861
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        pygame.display.set_caption('Tetris')

        self.tetromino = Tetromino()
        self.field = Field(
            width=10, height=20, screen_width=self.screen_width, screen_height=self.screen_height)
        self.score = Score()

        self.clock = pygame.time.Clock()

    def handle_events(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.running = False

    def update(self):
        pass

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.field.draw_grid(self.screen)
        pygame.display.flip()

    def run(self):
        self.running = True

        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(30)


if __name__ == '__main__':
    game = Game()
    game.run()
