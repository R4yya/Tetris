from settings import *

from game import Game
from score import Score
from preview import Preview

from sys import exit
from os import path
from random import choice


class Tetris(object):
    def __init__(self):
        pygame.init()

        self.display_surface = pygame.display.set_mode((Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT))
        self.icon = pygame.image.load(path.join('..', 'icon', 'tetris.png'))
        pygame.display.set_icon(self.icon)
        pygame.display.set_caption('Tetris')

        self.clock = pygame.time.Clock()
        self.running = False

        self.next_shapes = [choice(list(Settings.TETROMINOS.keys())) for shape in range(3)]

        self.default_font = pygame.font.Font(path.join('..', 'graphics', 'Russo_One.ttf'), 30)
        self.small_font = pygame.font.Font(path.join('..', 'graphics', 'Russo_One.ttf'), 24)

        self.game = Game(self.get_next_shape, self.update_score, self.default_font)
        self.score = Score(self.small_font)
        self.preview = Preview()

        self.background_music = pygame.mixer.Sound(path.join('..', 'sound', 'music.wav'))
        self.background_music.set_volume(0.5)
        self.background_music.play(-1)

        self.paused = False

    def toggle_pause(self):
        self.paused = not self.paused

    def handle_events(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    exit()
                case pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.toggle_pause()

    def update_score(self, high_score, lines, score, level):
        self.score.high_score = high_score
        self.score.lines = lines
        self.score.score = score
        self.score.level = level

    def get_next_shape(self):
        next_shape = self.next_shapes.pop(0)
        self.next_shapes.append(choice(list(Settings.TETROMINOS.keys())))

        return next_shape

    def run(self):
        while True:
            self.handle_events()

            if not self.paused:
                if not self.game.game_over:
                    self.display_surface.fill(Settings.COLORS['GRAY'])

                    self.game.run()
                    self.score.run()
                    self.preview.run(self.next_shapes)

                    pygame.display.update()
                    self.clock.tick()
                else:
                    self.score.reset_score()
                    self.game.reset_game()
                    self.game.show_game_over_screen()

                    waiting = True
                    while waiting:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                exit()
                            if event.type == pygame.KEYDOWN:
                                waiting = False
            else:
                self.game.show_pause_screen()


if __name__ == '__main__':
    tetris = Tetris()
    tetris.run()
