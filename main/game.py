from settings import *

from base_model import BaseModel

from tetromino import Tetromino
from timer import Timer

from sys import exit
from os import path
from random import choice


class Game(BaseModel):
    def __init__(self, get_next_shape, update_score, font):
        self.surface = self.set_surface()
        self.display_surface = self.set_display_surface()

        self.rect = self.surface.get_rect(topleft=(PADDING, PADDING))

        self.sprites = pygame.sprite.Group()

        self.get_next_shape = get_next_shape

        self.update_score = update_score

        self.line_surface = self.surface.copy()
        self.line_surface.fill(COLORS['PURE_GREEN'])
        self.line_surface.set_colorkey(COLORS['PURE_GREEN'])
        self.line_surface.set_alpha(255)

        self.field_data = [[0 for x in range(COLUMNS)] for y in range(ROWS)]
        self.tetromino = Tetromino(
            choice(list(TETROMINOS.keys())),
            self.sprites,
            self.create_new_teromino,
            self.field_data
        )

        self.down_speed = UPDATE_START_SPEED
        self.down_speed_faster = self.down_speed * 0.1
        self.down_pressed = False

        self.timers = {
            'vertival_move': Timer(self.down_speed, True, self.move_down),
            'horisontal_move': Timer(MOVE_WAIT_TIME),
            'rotate': Timer(ROTATE_WAIT_TIME)
        }
        self.timers['vertival_move'].activate()

        self.current_level = 1
        self.current_score = 0
        self.current_lines = 0

        self.landing_sound = pygame.mixer.Sound(path.join('..', 'sound', 'landing.wav'))
        self.landing_sound.set_volume(0.1)

        self.font = font

        self.game_over = False

    def set_surface(self):
        return pygame.Surface((GAME_WIDTH, GAME_HEIGHT))

    def set_display_surface(self):
        return pygame.display.get_surface()

    def draw_grid(self):
        for col in range(1, COLUMNS):
            x = col * CELL_SIZE
            pygame.draw.line(self.line_surface, COLORS['WHITE'], (x, 0), (x, self.line_surface.get_height()), 2)

        for row in range(1, ROWS):
            y = row * CELL_SIZE
            pygame.draw.line(self.line_surface, COLORS['WHITE'], (0, y), (self.line_surface.get_width(), y), 2)

        self.surface.blit(self.line_surface, (0, 0))

    def reset_game(self):
        self.sprites = pygame.sprite.Group()
        self.field_data = [[0 for x in range(COLUMNS)] for y in range(ROWS)]
        self.down_speed = UPDATE_START_SPEED
        self.down_speed_faster = self.down_speed * 0.1
        self.down_pressed = False
        self.current_level = 1
        self.current_score = 0
        self.current_lines = 0
        self.game_over = False

    def show_game_over_screen(self):
        game_over_surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT), pygame.SRCALPHA)
        game_over_rect = game_over_surface.get_rect()
        
        pygame.draw.rect(game_over_surface, (0, 0, 0, 150), game_over_rect)
        
        game_over_text = self.font.render("Game Over", True, COLORS['WHITE'])
        restart_text = self.font.render("Press any key to restart", True, COLORS['WHITE'])

        game_over_rect = game_over_text.get_rect(center=(GAME_WIDTH // 2 + PADDING, GAME_HEIGHT // 2))
        restart_rect = restart_text.get_rect(center=(GAME_WIDTH // 2 + PADDING, GAME_HEIGHT // 2 + 50))

        self.display_surface.blit(game_over_surface, self.rect)
        self.display_surface.blit(game_over_text, game_over_rect)
        self.display_surface.blit(restart_text, restart_rect)

        pygame.display.flip()

    def check_game_over(self):
        for block in self.tetromino.blocks:
            if block.position.y < 0:
                self.game_over = True

    def create_new_teromino(self):
        self.check_game_over()

        self.check_filled_rows()

        self.landing_sound.play()

        self.tetromino = Tetromino(
            self.get_next_shape(),
            self.sprites,
            self.create_new_teromino,
            self.field_data
        )
        for row in self.field_data:
            print(row)
        print()

    def timers_update(self):
        for timer in self.timers.values():
            timer.update()

    def move_down(self):
        self.tetromino.move_down(1)

    def calculate_score(self, num_lines):
        self.current_lines += num_lines
        self.current_score += SCORE_DATA[num_lines] * self.current_level

        if self.current_lines / 10 > self.current_level:
            self.current_level += 1
            self.down_speed -= INCREACE_SPEED
            self.down_speed_faster = self.down_speed * 0.1

        self.update_score(self.current_lines, self.current_score, self.current_level)

    def check_filled_rows(self):
        filled_rows = []

        for i, row in enumerate(self.field_data):
            if all(row):
                filled_rows.append(i)

        if filled_rows:
            for filled_row in filled_rows:
                for block in self.field_data[filled_row]:
                    block.kill()

                for row in self.field_data:
                    for block in row:
                        if block and block.position.y < filled_row:
                            block.position.y += 1

            self.field_data = [[0 for x in range(COLUMNS)] for y in range(ROWS)]

            for block in self.sprites:
                self.field_data[int(block.position.y)][int(block.position.x)] = block

            self.calculate_score(len(filled_rows))

    def handle_input(self):
        keys = pygame.key.get_pressed()

        if not self.timers['horisontal_move'].active:
            if keys[pygame.K_LEFT]:
                self.tetromino.move_horizontal(-1)
                self.timers['horisontal_move'].activate()
            if keys[pygame.K_RIGHT]:
                self.tetromino.move_horizontal(1)
                self.timers['horisontal_move'].activate()

        if not self.timers['rotate'].active:
            if keys[pygame.K_UP]:
                self.tetromino.rotate()
                self.timers['rotate'].activate()

        if not self.down_pressed and keys[pygame.K_DOWN]:
            self.down_pressed = True
            self.timers['vertival_move'].duration = self.down_speed_faster

        if self.down_pressed and not keys[pygame.K_DOWN]:
            self.down_pressed = False
            self.timers['vertival_move'].duration = self.down_speed

    def run(self):

        self.handle_input()
        self.timers_update()
        self.sprites.update()

        self.surface.fill(COLORS['GRAY'])

        self.sprites.draw(self.surface)

        self.draw_grid()

        self.display_surface.blit(self.surface, (PADDING, PADDING))

        pygame.draw.rect(self.display_surface, COLORS['WHITE'], self.rect, 3, 2)


if __name__ == '__main__':
    pass
