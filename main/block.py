from settings import *


class Block(pygame.sprite.Sprite):
    def __init__(self, group, position, color):
        super().__init__(group)
        self.image = pygame.Surface((Settings.CELL_SIZE, Settings.CELL_SIZE))
        self.image.fill(color)

        self.position = pygame.Vector2(position) + Settings.BLOCK_OFFSET
        self.rect = self.image.get_rect(topleft=self.position * Settings.CELL_SIZE)

    def rotate(self, pivot_position):
        return pivot_position + (self.position - pivot_position).rotate(90)

    def horizontal_collide(self, x, field_data):
        if not 0 <= x < Settings.COLUMNS:
            return True

        if field_data[int(self.position.y)][x]:
            return True

    def vertical_collide(self, y, field_data):
        if y >= Settings.ROWS:
            return True

        if y >= 0 and field_data[y][int(self.position.x)]:
            return True

    def update(self):
        self.rect.topleft = self.position * Settings.CELL_SIZE


if __name__ == '__main__':
    pass
