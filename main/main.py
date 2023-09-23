from settings import *

from game import Game
from score import Score
from preview import Preview

from random import choice


class Tetris(object):
    def __init__(self):
        pygame.init()

        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Tetris')

        self.clock = pygame.time.Clock()

        self.next_shapes = [choice(list(TETROMINOS.keys())) for shape in range(3)]

        self.game = Game(self.get_next_shape, self.update_score)
        self.score = Score()
        self.preview = Preview()

    def handle_quit(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.running = False

    def update_score(self, lines, score, level):
        self.score.lines = lines
        self.score.score = score
        self.score.level = level

    def get_next_shape(self):
        next_shape = self.next_shapes.pop(0)
        self.next_shapes.append(choice(list(TETROMINOS.keys())))

        return next_shape

    def run(self):
        self.running = True

        while self.running:
            self.handle_quit()

            self.display_surface.fill(COLORS['GRAY'])

            self.game.run()
            self.score.run()
            self.preview.run(self.next_shapes)

            pygame.display.update()
            self.clock.tick()


if __name__ == '__main__':
    tetris = Tetris()
    tetris.run()
