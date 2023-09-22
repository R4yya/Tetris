from settings import *


class Block(pygame.sprite.Sprite):
    def __init__(self, group, position, color):
        super().__init__(group)
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(color)

        self.position = pygame.Vector2(position) + BLOCK_OFFSET
        self.rect = self.image.get_rect(topleft=self.position * CELL_SIZE)

    def horizontal_collide(self, x):
        if not 0 <= x < COLUMNS:
            return True
        else:
            return False

    def vertical_collide(self, y):
        if not y < ROWS:
            return True
        else:
            return False

    def update(self):
        self.rect.topleft = self.position * CELL_SIZE


if __name__ == '__main__':
    pass
