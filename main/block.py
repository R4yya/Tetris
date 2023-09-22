from settings import *


class Block(pygame.sprite.Sprite):
    def __init__(self, group, position, color):
        super().__init__(group)
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(color)

        self.position = pygame.Vector2(position) + BLOCK_OFFSET
        x = self.position.x * CELL_SIZE
        y = self.position.y * CELL_SIZE
        self.rect = self.image.get_rect(topleft=(x, y))


if __name__ == '__main__':
    pass
