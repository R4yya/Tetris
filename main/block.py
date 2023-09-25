from settings import Settings


class Block(pygame.sprite.Sprite):
    def __init__(self, group, position, color):
        super().__init__(group)
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(color)

        self.position = pygame.Vector2(position) + BLOCK_OFFSET
        self.rect = self.image.get_rect(topleft=self.position * CELL_SIZE)

    def rotate(self, pivot_position):
        return pivot_position + (self.position - pivot_position).rotate(90)

    def horizontal_collide(self, x, field_data):
        if not 0 <= x < COLUMNS:
            return True

        if field_data[int(self.position.y)][x]:
            return True

    def vertical_collide(self, y, field_data):
        if y >= ROWS:
            return True

        if y >= 0 and field_data[y][int(self.position.x)]:
            return True

    def update(self):
        self.rect.topleft = self.position * CELL_SIZE


if __name__ == '__main__':
    pass
