import pygame
from tetromino import Tetromino
from field import Field
from score import Score


class Game(object):
    def __init__(self):
        pygame.init()

        self.screen_width, self.screen_height = 481, 861
        self.cell_size = self.screen_width // 10
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        pygame.display.set_caption('Tetris')

        self.current_tetromino = Tetromino(self.cell_size)
        self.field = Field(
            width=10, height=20, cell_size=self.cell_size)
        self.score = Score()

        self.clock = pygame.time.Clock()

    def place_tetromino(self):
        current_shape = self.current_tetromino.current_shape
        x, y = self.current_tetromino.x, self.current_tetromino.y

        for row in range(len(current_shape)):
            for col in range(len(current_shape[0])):
                if current_shape[row][col] == 1:
                    self.field.field[y // self.cell_size +
                                     row][x // self.cell_size + col] = 1

        self.current_tetromino = Tetromino(self.cell_size)

    def check_collision(self):
        current_shape = self.current_tetromino.current_shape
        x, y = self.current_tetromino.x, self.current_tetromino.y

        for row in range(len(current_shape)):
            for col in range(len(current_shape[0])):
                if current_shape[row][col] == 1:
                    if (y // self.cell_size + row >= self.field.height or
                        x // self.cell_size + col >= self.field.width or
                            self.field.field[y // self.cell_size + row][x // self.cell_size + col] == 1):
                        return True

        if y + len(current_shape) * self.cell_size >= self.screen_height:
            return True

        return False

    def handle_events(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.running = False
                case pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.current_tetromino.move_left()
                    elif event.key == pygame.K_RIGHT:
                        self.current_tetromino.move_right()
                    elif event.key == pygame.K_DOWN:
                        self.current_tetromino.move_down()
                    elif event.key == pygame.K_UP:
                        self.current_tetromino.rotate()

    def update(self):
        if self.check_collision():
            self.place_tetromino()
        else:
            self.current_tetromino.move_down()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.current_tetromino.draw(self.screen)
        self.field.draw_grid(self.screen)
        
        pygame.display.flip()

    def run(self):
        self.running = True

        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(1)


if __name__ == '__main__':
    game = Game()
    game.run()
